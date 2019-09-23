package mitm

import collection.JavaConverters._
import java.nio.charset.StandardCharsets
import java.nio.file.{Paths, Files}
import java.util.logging.Level
import org.openqa.selenium._
import org.openqa.selenium.chrome._
import org.openqa.selenium.logging._
import org.openqa.selenium.remote._
import scala.sys.process._

object TestMitm {
  def createNoJsProfile(): Unit = {
    Process("rm -rf /tmp/noJsProfile").!
    new java.io.File("/tmp/noJsProfile/Default/").mkdirs
    Files.write(
      Paths.get("/tmp/noJsProfile/Default/Preferences"),
      """{"profile":{"default_content_setting_values":{"javascript":2},"default_content_settings":{"javascript":2}}}"""
        .getBytes(StandardCharsets.UTF_8)
    )
  }

  def killAllLocalServer(): Unit = {
    Process("sudo pkill -f python3").!
  }

  def startAllLocalServer(): Unit = {
    Process("sudo python3 /mitm_test/server.py 80").run
    Process("sudo python3 /mitm_test/server.py 443").run
  }

  def setUpTest(): Unit = {
    createNoJsProfile

    killAllLocalServer
    Process("echo 127.0.0.42 testsite") #| Process("sudo tee -a /etc/hosts") #| Process(
      "true") !

    Process("echo 127.0.0.42 mitm.ssl.testsite") #| Process(
      "sudo tee -a /etc/hosts") #| Process("true") !

    Process("echo 127.0.0.42 testsite.http") #| Process(
      "sudo tee -a /etc/hosts") #| Process("true") !

    Process("echo 127.0.0.42 testsite.https") #| Process(
      "sudo tee -a /etc/hosts") #| Process("true") !

    startAllLocalServer
    Thread sleep 3123
  }

  def testRedirectSetsCookie(): Unit = {
    val d = getChrome("http://testsite.ssl/redirect")
    assertPageContains(d, "self.path|/redirected")
    assertPageContains(d, "Cookie|test=magic")
    d.close()
  }

  def testLinksAreRewritten(): Unit = {
    val d = getChrome("http://testsite.ssl/link")
    assertPageContains(d, "https://testsite/target")
    d.findElementById("mylink").click()
    assertPageContains(d, "Referer|https://testsite/link")
    assertPageContains(d, "self.path|/target")
    d.close()
  }

  def testPost(): Unit = {
    val d = getChrome("http://testsite.ssl/postform")
    d.findElementById("mybutton").click()
    assertPageContains(d, "Origin|https://testsite")
    assertPageContains(d, "Referer|https://testsite/postform")
    assertPageContains(
      d,
      "post_data|thetext=some+text%0D%0A&continue=https%3A%2F%2Ftestsite%2Fsomelink")
    assertPageContains(d, "Content-Type|application/x-www-form-urlencoded")
    assertPageContains(d, "self.path|/posted")
    d.close()
  }

  def testTeepot(): Unit = {
    val d = getChrome("https://testsite/postform")
    assertPageContains(d, "ERR_TUNNEL_CONNECTION_FAILED")
    d.close()
  }

  def testHttpsFollowed(): Unit = {
    val d = getChrome("http://testsite/redirect")
    assert(d.getCurrentUrl == "http://testsite.ssl/redirected")
    d.close()
  }

  def testHttpsForced(): Unit = {
    val d = getChrome("http://testsite/redirect",
                      List("--proxy-server=127.0.0.42:8081"))
    assertPageContains(d, "Host|testsite")
    d.close()
  }

  def test404(): Unit = {
    val d =
      getChrome("http://testsite/xxx.pdf",
                List("--proxy-server=127.0.0.42:8082"))
    val logs = d.manage().logs().get("performance");
    val x = logs.asScala
      .filter(_.toString().contains("404"))
      .filter(_.toString().contains("GET http://testsite/xxx.pdf HTTP/1.1"))
    assert(x.size == 1)
    d.close()
  }

  def testPdf(): Unit = {
    val r1 = (Process(
      "curl -v http://127.0.0.1:1234/testsite/valami.pdf --proxy 127.0.0.42:8083") #| Process(
      "grep BZON75HQ6NDR")).!
    assert(r1 == 0)
    val d =
      getChrome("http://testsite/valami.pdf",
                List("--proxy-server=127.0.0.42:8083"))
    assert(d.getCurrentUrl == "http://127.0.0.1:1234/testsite/valami.pdf")
    //assertPageContains(d, "Random BZON75HQ6NDR text in a PDF file")
    d.close()
    val r2 =
      (Process("curl -v http://127.0.0.1:1234/testsite/valami.pdf") #| Process(
        "grep BZON75HQ6NDR")).!
    assert(r2 == 0)
  }

  def testJson(): Unit = {
    val d = getChrome("http://testsite/json")
    assertPageContains(d, "twitter.com.ssl")
    d.close()
  }

  def testSslHostname(): Unit = {
    val d = getChrome("http://mitm.ssl.testsite/stg.ssl/other",
                      List("--proxy-server=127.0.0.42:8081"))
    assertPageContains(d, "self.path|/stg.ssl/other")
    assert(d.getCurrentUrl == "http://mitm.ssl.testsite.ssl/stg.ssl/other")
    d.close()
  }

  def killServer(port: Int): Unit = {
    val cmd1r = Process("ps -ef").!!
    val r2 = cmd1r.split("\n").filter(_ matches (".* " + port))(1)
    val r3 = r2.split(" ").filter(_ != "")(1)
    val killres = Process("sudo", Seq("kill", r3)).!
    assert(killres == 0)
  }

  def allLocalMitmTest(): Unit = {
    setUpTest

    testRedirectSetsCookie
    testLinksAreRewritten
    testPost
    testTeepot
    testHttpsFollowed
    testHttpsForced
    test404
    testPdf
    testJson
    testSslHostname

    //Kill the port 80 server, and observe that it is gone!
    killServer(80)
    testHttpsForced
    //TODO: test around testHttpsFollowed

    //TODO: add a TC for http-only service
    //TODO: binary data either a) gets in unaltered or b) gets filtered (404)
    //TODO: 'src=https://' as in https://www.gsmarena.com/samsung_galaxy_a3-6762.php

    killAllLocalServer
  }

  def runAllLocalMitmTest(): Unit = {
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_start")
    allLocalMitmTest
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_collect")
    println("TestMitm.runAllLocalMitmTest() SUCCESS")
  }

  def testTwitter(): Unit = {
    val d = TestMitm.getChrome("http://www.whatismybrowser.com.ssl/",
                               List("--proxy-server=127.0.0.42:8080",
                                    "--user-data-dir=/tmp/noJsProfile"))
    assertPageContains(d, "No - JavaScript is not enabled")
    val turl = "http://twitter.com.ssl/httpseverywhere/"
    d.navigate().to(turl)
    mySleep(1300)
    assert(d.getCurrentUrl == turl)
    d.close()
  }

  def runAllMitmTest(): Unit = {
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_start")
    allLocalMitmTest
    testTwitter
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_collect")
    println("TestMitm.runAllMitmTest() SUCCESS")
  }

  def runTestHttp(): Unit = {
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_start_http")
    setUpTest

    val d1 = getChrome("http://testsite.http/link")
    assertPageContains(d1, "misconfiguration")
    d1.close()
    val d2 = getChrome("http://testsite.http/link",
                       List("--proxy-server=127.0.0.42:8081"))
    assertPageContains(d2, "https://testsite/target")
    d2.close()

    val d3 = getChrome("http://testsite:8080/link", List())
    assertPageContains(d3, "HTTP ERROR 418")
    d3.close()

    killAllLocalServer
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_collect_http")
    println("TestMitm.runTestHttp() SUCCESS")
  }

  def runTestUp(): Unit = {
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_start_up")
    setUpTest

    killServer(443)
    val d1 = getChrome("http://testsite/link")
    assertPageContains(d1, "ERR_SSL_PROTOCOL_ERROR")
    d1.close()
    val d2 = getChrome("http://testsite/link")
    assertPageContains(d2, "mitm seen before")
    d2.close()
    //TODO: ignoreHosts
    //TODO: downgrade redirect does not work

    killAllLocalServer
    scala.io.Source.fromURL("http://127.0.0.42:4280/coverage_collect_up")
    println("TestMitm.runTestUp() SUCCESS")
  }

  def runAllLocalTest(): Unit = {
    runAllLocalMitmTest
    runTestUp
    runTestHttp
  }

  def getChrome(page: String): ChromeDriver = {
    getChrome(page, List("--proxy-server=127.0.0.42:8080"))
  }

  def getChrome(page: String, argOpt: List[String]): ChromeDriver = {
    val opt = new ChromeOptions()
    opt.addArguments("--no-sandbox")
    opt.addArguments("--disable-smooth-scrolling")
    argOpt.map(opt.addArguments(_))

    val cap = DesiredCapabilities.chrome()
    cap.setCapability(ChromeOptions.CAPABILITY, opt)
    val logPrefs = new LoggingPreferences()
    logPrefs.enable(LogType.PERFORMANCE, Level.ALL)
    cap.setCapability(CapabilityType.LOGGING_PREFS, logPrefs)

    val driver = new ChromeDriver(cap)
    driver.get(page)
    mySleep(50)
    driver
  }

  def assertPageContains(d: ChromeDriver, text: String): Unit = {
    val resp = d.findElementByXPath("/html").getText
    if (!resp.contains(text)) {
      printPage(d)
      assert(false)
    }
  }

  def printPage(d: ChromeDriver): Unit =
    println(d.findElementByXPath("/html").getText)

  def mySleep(t: Long): Unit = {
    Thread sleep t
  }

  def testMitmDisconnect(): Unit = {
    val opt = new ChromeOptions()
    opt.addArguments("--no-sandbox")
    opt.addArguments("--disable-smooth-scrolling")
    opt.addArguments("--proxy-server=127.0.0.42:8080")
    opt.addArguments("--user-data-dir=/tmp/noJsProfile")
    val driver = new ChromeDriver(opt)
    driver.get("http://ipv6-test.com/validate.php")
    var trials = 47
    var error502 = 0 //Bad Gateway
    for (a <- 1 to trials) {
      val resp = driver.findElementByXPath("/html").getText
      val isError = resp.contains("HttpReadDisconnect('Server disconnected'")
      println(isError)
      if (isError) error502 += 1
      Thread sleep 345
      driver.navigate().refresh()
    }
    driver.close()
    println(s"$error502 error out of $trials trials")
  }
}

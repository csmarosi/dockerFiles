.PHONY : all clean

all: clean
	ln -s /bin/true /tmp/bTestaa750145402ddf8c9bc7acd17f3b65ba
# Create a new profile
	coverage run -p --branch --source . chromium.py
# Use that profile
	coverage run -p --branch --source . chromium.py
	grep -q 'safebrowsing": {"enabled": false' chromium_py/Default/Preferences

	coverage run -p --branch --source . chromiumTest.py

	coverage combine && coverage report && coverage html
	pyflakes *py
	pycodestyle *py
	find . -type f -name '*.py' | xargs yapf -i

clean:
	rm -rf htmlcov/ .coverage* __pycache__/
	rm -rf derived/ chromium_py/ /tmp/bTestaa750145402ddf8c9bc7acd17f3b65ba

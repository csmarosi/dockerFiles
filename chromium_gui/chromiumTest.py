#!/usr/bin/env python3
import json
import chromium


class ChromiumTest(chromium.ChromiumBase):
    def __init__(self):
        super(ChromiumTest, self).__init__()

    def changePreferences(self):
        return {"translate": {"derivedTest": 42}}


def main():
    o = ChromiumTest()
    o.myClassMain('derived')
    with open('derived/Default/Preferences', 'r') as data_file:
        prefData = json.load(data_file)
        assert prefData['translate'] == {'derivedTest': 42, 'enabled': False}


if __name__ == '__main__':
    main()

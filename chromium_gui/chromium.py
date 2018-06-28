#!/usr/bin/env python3
"""Base class for creating Chrom(e|ium) profiles

This creates First Run Preferences file for Chrom(e|ium)
"""

import sys
import subprocess
import os
import json


def getDefaultPreferences():
    default_search_provider_data = {
        "template_url_data": {
            "short_name": "DuckDuckGo",
            "url": "https://duckduckgo.com/html?q={searchTerms}",
            "keyword": "duckduckgo.com"
        }
    }
    pref = {
        "safebrowsing": {
            "enabled": False
        },
        "default_search_provider_data": default_search_provider_data,
        "download": {
            "prompt_for_download": True
        },
        "translate": {
            "enabled": False
        },
        "search": {
            "suggest_enabled": False
        },
        "net": {
            "network_prediction_options": 2
        },
        # Use a web service to help resolve navigation errors
        "alternate_error_pages": {
            "enabled": False
        },
        # Google Cloud Print
        "local_discovery": {
            "notifications_enabled": False
        },
        "dns_prefetching": {
            "enabled": False
        },
        "extensions": {
            # Prevent calling home like https://new.gcm.hostname:5228
            "settings": {
                "pafkbggdmjlpgkdkcbjmhmfcdpncadgh": {
                    "state": 0
                }
            },
            "theme": {
                "use_system": True
            }
        },
        "bookmark_bar": {
            "show_on_all_tabs": True,
            "show_apps_shortcut": False
        }
    }
    return pref


def mergePreferences(destination, source):
    for key in source:
        if isinstance(source[key], dict):
            if key not in destination:
                destination[key] = {}
            mergePreferences(destination[key], source[key])
        else:
            destination[key] = source[key]


class ChromiumBase(object):
    def __init__(self):
        super(ChromiumBase, self).__init__()
        self.arguments = ['--no-sandbox', '--disable-smooth-scrolling']

    def getExePath(self):
        guesses = [
            '/usr/bin/google-chrome',
            '/tmp/bTestaa750145402ddf8c9bc7acd17f3b65ba',
            '/usr/bin/chromium',
            '/usr/bin/chromium-browser',
        ]
        for guess in guesses:
            if os.path.isfile(guess):
                self.exe = guess
                return

    def createProfilePath(self):
        subprocess.call(['mkdir', '-p', self.profilePath + '/Default/'])
        self.arguments.append('--user-data-dir=' + self.profilePath)

        profileName = self.profilePath.strip('/').split('/')[-1]
        cachePath = '/tmp/{0}-cache/'.format(profileName)
        subprocess.call(['rm', '-rf', cachePath])
        subprocess.call(['mkdir', '-p', cachePath])
        self.arguments.append('--disk-cache-dir=' + cachePath)

    def createFistRun(self):
        subprocess.call(['touch', self.profilePath + '/First Run'])

    def createPreferences(self):
        self.Preferences = getDefaultPreferences()

    def changePreferences(self):
        return {}

    def writePreferences(self):
        prefFile = self.profilePath + '/Default/Preferences'
        prefData = {}
        try:
            with open(prefFile, 'r') as data_file:
                prefData = json.load(data_file)
            prefData["default_search_provider_data"]["template_url_data"] = {}
        except (IOError, KeyError):
            pass

        mergePreferences(self.Preferences, self.changePreferences())
        mergePreferences(prefData, self.Preferences)
        with open(prefFile, 'w') as data_file:
            json.dump(prefData, data_file)

    def writeLocalState(self):
        prefFile = self.profilePath + '/Local State'
        prefData = {}
        try:
            with open(prefFile, 'r') as data_file:
                prefData = json.load(data_file)
        except (IOError, KeyError):
            pass
        noHwAccel = {"hardware_acceleration_mode": {"enabled": False}}
        mergePreferences(prefData, noHwAccel)
        with open(prefFile, 'w') as data_file:
            json.dump(prefData, data_file)

    def execBrowser(self):
        subprocess.call([self.exe] + self.arguments)

    def getProfilePath(self, profileName):
        realPath = os.path.realpath(sys.argv[0])
        realDir = os.path.dirname(realPath) + '/'
        if not profileName:
            profileName = sys.argv[0].split('/')[-1]
        self.profilePath = realDir + profileName.replace('.', '_')

    def myClassMain(self, profileName=None):
        self.getProfilePath(profileName)
        self.getExePath()
        self.createProfilePath()
        self.createFistRun()
        self.createPreferences()
        self.writePreferences()
        self.writeLocalState()
        self.execBrowser()


def main():
    o = ChromiumBase()
    o.myClassMain()


if __name__ == '__main__':
    main()

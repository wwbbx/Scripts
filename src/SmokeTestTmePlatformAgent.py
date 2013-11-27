# Smoke test TMEPlatformAgent is executing smoke test for TMEPlatformAgent
# setup package simple verification.

# Pre-requirements:
# Service Data Access needs to be installed.
# SDA version must higher than 5.0.4.
# Get setup package from remote shared folder.
# Get TME application's latest version from TME application web.
# Parse TMEPlatformAgent version number based on its setup package name.
# Check current installed software version "TMEPlatformAgent"
# Execute smoke test in specified computer with sufficent user name and pass.
# Upgrade if current version is smaller.
# Install if there is no current version.
# Validate SDA Platform Agent Manager service is started.
# Validate C:\ProgramData\Agilent Technologies\Service Data Access\
# PlatformAgents\System\TMEPlatformAgent.dll exist.
# Check its parent folder has TMERun and it has sufficent dll and config files.

import sys
import argparse
import subprocess


def ParseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host')
    parser.add_argument('--user')
    parser.add_argument('--pass')

    argjson = parser.parse_args()
    args = vars(argjson)

    return args


def GetWmicFullPath():
    return r'C:\Windows\System32\wbem\WMIC.exe'


def GetCurrentPlatformAgentVersion(host, user, pass):
    wmic = GetWmicFullPath()
    command = wmic + ' /node:{0} product where' \
              + ' name="TMEPlatformAgent" list status'
    command
    proc = subprocess.Popen(command, stdout=subprocess.PIPE)
    out,err = proc.communicate()

    lines = out.splitlines()

    for line in lines:
        if "TMEPlatformAgent" in line:





args = ParseArguments()

smokeTestComputer = args['host'] if args['host'] else 'localhost'
smokeTestUser = args['user'] if args['user'] else 'xiwang'
smokeTestUserPassword = args['pass'] if args['pass'] else 'hp53131a$'

#print(smokeTestComputer)
#print(smokeTestUser)
#print(smokeTestUserPassword)


currentTmePlatformAgentVersion = \
    GetCurrentTmePlatformAgentVersion( smokeTestComputer, \
        smokeTestUser, smokeTestUserPassword)

latestTmePlatformAgentSetupPackage = GetLatestSetupPackage()

#latestTmePlatformAgentVersion =
#    ParseLatestTmePlatformAgentVersion(latestTmePlatformAgentSetupPackage)
#
#if latestTmePlatformAgentVersion <= currentTmePlatformAgentVersion:
#	UninstallTmePlatformAgent()
#
#InstallTmePlatformAgent(latestTmePlatformAgentSetupPackage)
#
#VerifyTmePlatformAgentDll()
#VerifyTmePlatformAgentConfigFiles()
#VerifyTmePlatformAgentStrategyDlls()

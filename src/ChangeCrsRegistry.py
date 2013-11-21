import os
import sys
import re
import time
import _winreg
import subprocess
import Registry
import WindowsService

# This script will change CRS registry values to given parameters.
def ShowHelp():
    print 'Usage: ChangeCrsRegistry -host tme-bj-hub1.chn.agilent.com -office 8370'
    print 'Change CRS registry setting.'

def ValidateArgument(argv):
    # lenth should be 5
    if not len(argv) == 5:
        return False

    # second argument is -host
    if not argv[1] == '-host':
        return False

    # forth argument is -office
    if not argv[3] == '-office':
        return False

    return True

if not ValidateArgument(sys.argv):
    ShowHelp()
    exit

hubDataIntegSvrName = 'Hub Data Integration'
hubDataIntegProcessName = 'HubDataIntegrationService'
sdaManagerSvrName = 'SDA Platform Agent Manager'

# kill process
if WindowsService.IsProcessRunning(hubDataIntegProcessName):
    print 'Killing {0} ...'.format(hubDataIntegSvrName)
    WindowsService.KillProcess(hubDataIntegProcessName)

print 'Stopping {0} ...'.format(sdaManagerSvrName)
WindowsService.StopService(sdaManagerSvrName)
time.sleep(0.5)

# change value in registry
hostName = sys.argv[2]
officeNumber = sys.argv[4]

officePathInRegistry = r'SOFTWARE\Wow6432Node\Agilent Technologies\Service Data Access\Configuration\System'
hubBrokerPathInRegistry = r'SOFTWARE\Wow6432Node\Agilent Technologies\Service Data Access\Configuration\System\HubBroker'
officeEntityName = 'Entity'
hubBrokerName = 'HostName'

print 'Changing Registry value for Hub Broker to be: {0}.'.format(hostName)
print 'Changing Registry value for office number to be: {0}.'.format(officeNumber)
Registry.ChangeRegValue(officePathInRegistry, officeEntityName, officeNumber)
Registry.ChangeRegValue(hubBrokerPathInRegistry, hubBrokerName, hostName)

# restart Hub Data Integration Windows service
print 'Restarting Hub Data Integration service ..'
WindowsService.StartService(hubDataIntegSvrName)
time.sleep(1)
print 'Restarting SDA PlatformAgent Manager service.'
WindowsService.StartService(sdaManagerSvrName)


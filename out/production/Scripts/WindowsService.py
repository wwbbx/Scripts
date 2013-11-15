__author__ = 'nixin'

import subprocess
import re

def IsProcessRunning(processName):
    # check given process is running or not
    checkCmd = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE)
    for info in checkCmd.stdout:
        if re.search(processName, info):
            return True

    return False

def IsServiceRunning(serviceName):
    # check service running status
    # true for running
    # false for stopped.
    psService = r'.\MSTools\psservice.exe'
    command = "{0} query \"{1}\"".format(psService, serviceName)

    output = subprocess.check_output(command, shell=True)

    if re.search("RUNNING", output):
        return True
    else:
        return False

def KillProcess(processName):
    # kill one windows process
    psKill = r'.\MSTools\pskill.exe'
    subprocess.call("{0} -t \"{1}\"".format(psKill, processName), shell=True)

def StopService(serviceName):
    # stop given windows service.
    psService = r'.\MSTools\psservice.exe'
    subprocess.call("{0} stop \"{1}\"".format(psService, serviceName), shell=True)

def StartService(serviceName):
    # start windows service.
    psService = r'.\MSTools\psservice.exe'
    subprocess.call("{0} start \"{1}\"".format(psService, serviceName), shell=True)

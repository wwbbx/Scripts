__author__ = 'nixin'

import subprocess
import re
import os
import Configuration
import time


class WindowsService:
    MSTOOLS_PATH = os.path.join(Configuration.Config.ROOT_PATH, r'src\MSTools')

    def IsProcessRunning(processName):
        # check given process is running or not
        checkCmd = subprocess.Popen("tasklist", shell=True, stdout=subprocess.PIPE)
        for info in checkCmd.stdout:
            if re.search(processName, str(info)):
                return True

        return False

    def IsServiceRunning(serviceName):
        # check service running status
        # true for running
        # false for stopped.
        psService = os.path.join(WindowsService.MSTOOLS_PATH, 'psservice.exe')
        command = "{0} query \"{1}\"".format(psService, serviceName)

        checkCmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        for info in checkCmd.stdout:
            match = re.search("RUNNING", str(info))
            if match:
                return True

        return False

    def KillProcess(processName):
        # kill one windows process
        psKill = os.path.join(WindowsService.MSTOOLS_PATH, 'pskill.exe')
        subprocess.call("{0} -t \"{1}\"".format(psKill, processName), shell=True)

    def StopService(serviceName):
        # stop given windows service.
        if WindowsService.IsServiceRunning(serviceName):
            psService = os.path.join(WindowsService.MSTOOLS_PATH, 'psservice.exe')
            subprocess.call("{0} stop \"{1}\"".format(psService, serviceName), shell=True)

    def StartService(serviceName):
        # start windows service.
        if not WindowsService.IsServiceRunning(serviceName):
            psService = os.path.join(WindowsService.MSTOOLS_PATH, 'psservice.exe')
            subprocess.call("{0} start \"{1}\"".format(psService, serviceName), shell=True)
            time.sleep(2)

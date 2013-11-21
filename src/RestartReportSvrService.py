import subprocess
import sys

# parse argument to get report server host name.
# clean up shared \\ReportServer\Report Data directory.
# restart Hub Data Integration service remotely.
# restart SDA Platform Agent Manager service remotely.


def ExecutePsExeccommand(action, serviceName):
    command = r'{0} \\{1} "{2}" {3}'.format(
        GetPsExecCommand(),
        GetRemoteComputerName(),
        netCommand,
        '{0} \"{1}\"'.format(action, serviceName))

    print(command)
    subprocess.call(command, shell=True)


def GetRemoteComputerName():
    return sys.argv[1]


def GetPsExecCommand():
    return r'.\MSTools\psexec.exe'


def GetReportDataFolder():
    return r'C:\ProgramData\Agilent Technologies\Service Data Access\Report Data'


def DeleteReportDataOnRemoteServer(serverName):
    delCommand = r'{0} \\{1} cmd /c del /F /Q "{2}\*.*"'.format(
        GetPsExecCommand(),
        GetRemoteComputerName(),
        GetReportDataFolder())

    print(delCommand)

    subprocess.call(delCommand, shell=True)


if len(sys.argv) < 1:
    print("Please provide computer name.")
else:
    netCommand = r'C:\Windows\System32\net.exe'

    hubDataIntegrationService = "Hub Data Integration"
    sdaPlatformAgentService = "SDA Platform Agent Manager"

    stopAction = 'stop'
    startAction = 'start'

    # stop SDA Platform Agent Manager
    ExecutePsExeccommand(stopAction, sdaPlatformAgentService)

    # stop Hub Data Integration service
    ExecutePsExeccommand(stopAction, hubDataIntegrationService)

    # delete existing report data on remote report server.
    DeleteReportDataOnRemoteServer(GetRemoteComputerName())

    # start Hub Data Integration service
    ExecutePsExeccommand(startAction, hubDataIntegrationService)

    # start SDA Platform Agent Manager service
    ExecutePsExeccommand(startAction, sdaPlatformAgentService)


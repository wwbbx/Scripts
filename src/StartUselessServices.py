import subprocess
import ServicesList

for service in ServicesList.Services:
    command = "net start \"{0}\"".format(service)
    subprocess.call(command, shell=True)


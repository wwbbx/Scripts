# net start servic to start Windows service
# net stop service to stop Windows service
# net pause service to pause Wineows service
# net continue service to continue Windows service

# This script collect services that I think they are not necessary
# and con be stopped if we want to make computer most high performance.

import subprocess
import ServicesList

for service in ServicesList.Services:
    command = "net stop \"{0}\"".format(service)
    subprocess.call(command, shell=True)



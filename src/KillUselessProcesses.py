# kill useless processes to improve performance
# process list are listed in ProcessesList.py.

# There is another Python script which is response
# for recorving all killed processes.

# "tasklist" to view all processes.
# "taskkill" to kill processes.

# example: taskkill /IM chrome.exe /F
# /IM is image name, /F is force to terminate.

import subprocess
import ProcessesList

for process in ProcessesList.Processes:
    command = "taskkill /IM {0} /F".format(process)
    subprocess.call(command, shell=True)


import subprocess

hubBroker = 'testhubbroker.germany.agilent.com'
office = '8370'

command = 'ipy .\ChangeCrsRegistry.py -host {0} -office {1}'.format(hubBroker, office)
subprocess.call(command, shell=True)
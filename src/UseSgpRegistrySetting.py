import subprocess

hubBroker = 'tme-bj-hub1.chn.agilent.com'
office = '7500'

command = 'ipy .\ChangeCrsRegistry.py -host {0} -office {1}'.format(hubBroker, office)
subprocess.call(command, shell=True)
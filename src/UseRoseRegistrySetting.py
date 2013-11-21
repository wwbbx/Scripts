import subprocess

hubBroker = 'lhdevhubbroker.cos.agilent.com'
office = '24br'

command = 'ipy .\ChangeCrsRegistry.py -host {0} -office {1}'.format(hubBroker, office)
subprocess.call(command, shell=True)
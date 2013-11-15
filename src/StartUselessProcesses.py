# this script will bring back all killed processes
# to let Windows running in safe mode rather than
# high performance mode.

import subprocess

Processes = [
    # adcist.exe
    r'C:\agilent\adci\adcist.exe',
    # CITICibnkmtf.exe
    r'"C:\Program Files (x86)\CNCB\PerCiticMate\CITICibnkmtf.exe" -/PerBS',
    # citic_certd.exe
    r'"C:\Program Files (x86)\CITICBank\FeiTian\citic_certd.exe" -r -a',
    # ICBCEBankAssist.exe
    r'"C:\Program Files\ICBCEbankTools\ICBCSetupIntegration\ICBCEBankAssist.exe"',
    # lpOverUsbSvc.exe
    r'"C:\Program Files (x86)\Common Files\Microsoft Shared\Phone Tools\CoreCon\11.0\Bin\lpOverUsbSvc.exe"',
    # iproc8491.exe
    r'"C:\Program Files\Agilent\IO Libraries Suite\bin\iproc8491.exe"',
    # iprocsvr.exe
    r'"C:\Program Files\Agilent\IO Libraries Suite\bin\iprocsvr.exe" -o',
    # jusched.exe
    r'"C:\Program Files (x86)\Common Files\Java\Java Update\jusched.exe"',
    # TSVNCache.exe
    r'"C:\Program Files\TortoiseSVN\bin\TSVNCache.exe"'
    ]

for command in Processes:
    subprocess.call(command, shell=True)

import _winreg

def ChangeRegValue(regKey, name, value):
    # change registry setting.
    try:
        key=_winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,
                            regKey, 0, _winreg.KEY_ALL_ACCESS)
    except:
        key=_winreg.CreateKey(_winreg.HKEY_LOCAL_MACHINE, regKey)

    _winreg.SetValueEx(key, name, 0, _winreg.REG_SZ, value)
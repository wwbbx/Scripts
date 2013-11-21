import unittest
import time
import _winreg
import subprocess
import Registry

class TestRegistry(unittest.TestCase):

    def test_change_registry_value(self):
        keyPath = r'SOFTWARE\Wow6432Node\Agilent Technologies\Service Data Access\Configuration\System'

        expectedValue = '24BR'
        Registry.ChangeRegValue(keyPath, 'Entity', expectedValue)

        # read it back for validation.
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,keyPath)
        actualValue = _winreg.QueryValueEx(key, 'Entity')

        self.assertTrue(expectedValue in actualValue)

    def test_read_reg_key(self):
        keyPath = r'SOFTWARE\Wow6432Node\Agilent Technologies\Service Data Access\Configuration\System'
        
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, keyPath)
        officeValue = _winreg.QueryValueEx(key, 'Entity')
        self.assertTrue('24BR' in officeValue)
        print officeValue

if __name__ == '__main__':
    unittest.main()

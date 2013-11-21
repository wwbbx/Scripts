import unittest
import time
import _winreg
import subprocess
import WindowsService

class TestWindowsService(unittest.TestCase):

    def test_IsServiceRunning_return_true_for_running_service(self):
        serviceName = 'SDA Platform Agent Manager'
        # start this service
        WindowsService.StartService(serviceName)
        time.sleep(1)

        serviceStatus = WindowsService.IsServiceRunning(serviceName)
        self.assertEqual(True, serviceStatus)


    def test_IsServiceRunning_return_false_for_stopped_service(self):
        serviceName = r'SDA Platform Agent Manager'
        WindowsService.StopService(serviceName)
        
        time.sleep(1)

        serviceStatus = WindowsService.IsServiceRunning(serviceName)
        self.assertFalse(serviceStatus)

    def test_IsProcessRunning_return_true_for_Desktop_Window_Manager(self):
        processName = "tasklist.exe"
        actual = WindowsService.IsProcessRunning(processName)

        self.assertTrue(actual)

if __name__ == '__main__':
    unittest.main()

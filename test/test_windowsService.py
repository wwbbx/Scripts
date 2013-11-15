from unittest import TestCase

__author__ = 'nixin'

import WindowsServiceModule


class TestWindowsService(TestCase):

    SERVICE_NAME = "SDA Platform Agent Manager"

    def test_IsProcessRunning(self):
        processName = "tasklist"

        actual = WindowsServiceModule.WindowsService.IsProcessRunning(processName)

        self.assertTrue(actual)

    def test_IsServiceRunning(self):
        serviceName = TestWindowsService.SERVICE_NAME

        actual = WindowsServiceModule.WindowsService.IsServiceRunning(serviceName)

        self.assertTrue(actual)


    def test_StopService(self):
        serviceName = TestWindowsService.SERVICE_NAME

        # stop this service.
        WindowsServiceModule.WindowsService.StopService(serviceName)

        # get service status
        status = WindowsServiceModule.WindowsService.IsServiceRunning(serviceName)

        self.assertFalse(status)

    def test_StartService(self):
        serviceName = TestWindowsService.SERVICE_NAME

        # start this service
        WindowsServiceModule.WindowsService.StartService(serviceName)

        # get status
        status = WindowsServiceModule.WindowsService.IsServiceRunning(serviceName)

        self.assertTrue(status)



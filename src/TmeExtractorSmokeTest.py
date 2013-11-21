# This module will execute smoke test cases for TMEPlatformAgent
# package.
#
# The smoke testing should be executed on one virtual machine.
# Below are detailed steps for smoke testing.
# 1. Revert virtual machine image to desired snapshot
# 2. Get the package from shared drive.
# 3. Validate existing installed version is a older one.
# 4. Install setup package to upgrade it to latest version.
# 5. Validate smoke test cases.
# 6. Uninstall this setup package.
# 7. Clean up installation target folder.
# 8. Install setup package as refresh installation.
# 9. Validate smoke test cases.
#
# Smoke test cases may include below items:
# 1. Desired files are exist in target installation folder.
# 2. DLLs are the expected version.
# 3. SDAPlatformAgent service is started.
# 4. If possible, copy TME DB, then control TME to export one CSO
#    then validate C:\temp directory for output raw CalServiceResults.

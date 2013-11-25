import os
import subprocess


def GetSvnRoot():
    svnRoot = r'C:\SVN\HubDataServices\Trunk'

    if(os.path.exists(svnRoot)):
        return svnRoot

    svnRoot = r'D:\SVN\HubDataServices\Trunk'

    if(os.path.exists(svnRoot)):
        return svnRoot


def GetSharedDirectory():
    return r'\\fas3000-b.chn.agilent.com\v6\WCSS_Eng_STE\TME_EXTRACTOR\SOFTWARES'


def GetVersion():
    f = open(os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\TMEPlatformAgentSetup.vdproj'))
    for line in f:
        if "ProductVersion" in line:
            version = line[line.index('"8:')+3:-2]
            return version


def BuildSetupPackage():
    devenv = r'C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE\devenv.com'
    solutionFile = os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TmePlatformAgentWin7\TmePlatformAgentWin7.sln')
    setupProject = os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\TMEPlatformAgentSetup.vdproj')

    packageFile = os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\Debug\TMEPlatformAgent.msi')

    if(os.path.isfile(packageFile)):
        print("Delete previous built tmePlatformAgentSetup.msi file.")
        subprocess.call("del {0}".format(packageFile), shell=True)

    command = "\"{0}\" \"{1}\" /Project \"{2}\" /Rebuild Debug".format(devenv, solutionFile, setupProject)
    print(command)
    subprocess.call(command, shell=True)

    # need to give devenv.exe about 30 seconds to finish the building


    if os.path.isfile(packageFile):
        print('Successfully built {0}!'.format(packageFile))
        return True

    return False


def CopyFile(source, destination):
    command = "copy /Y /V {0} {1}".format(source, destination)

    if os.path.isfile(source):
        subprocess.call(command, shell=True)
    else:
        print("{0} doesn't exists. Can't copy.".format(source))

    if os.path.isfile(destination):
        print('Successfully copied {0}!'.format(destination))


def CopyPackage(version):
    source = os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TMEPlatformAgentSetup\Debug\TMEPlatformAgent.msi')
    destination = os.path.join(GetSharedDirectory(), r'TMEPlatformAgent_{0}.msi'.format(version))

    CopyFile(source, destination)


def CopyReleaseNote():
    source = os.path.join(GetSvnRoot(), r'Platforms\TME\PlatformAgent\TMEPlatformAgent\ReleaseNote.txt')
    destination = os.path.join(GetSharedDirectory(), r'ReleaseNote.txt')

    CopyFile(source, destination)


def MoveOldPackage():
    # move old TMEPlatformAgent package from \\fas3000 to
    # its TMEPlatformAgent directory.

    # get all files starts with "TMEPlatformAgent"
    # exclude the one we just copied
    # move all others into its "TMEPlatformAgent" sub directory

    softwarePath = GetSharedDirectory()
    tmePlatformAgentSetupFiles = sorted([f for f in os.listdir(softwarePath) if 'TMEPlatformAgent_' in f])

    if len(tmePlatformAgentSetupFiles) > 1:
        # keep the latest one not archived.
        del tmePlatformAgentSetupFiles[-1]
        print('{0} will be archived!'.format(tmePlatformAgentSetupFiles))
        # move all old packages
        archiveFolder = os.path.join(softwarePath, r'TMEPlatformAgent')
        for f in tmePlatformAgentSetupFiles:
            destinationFile = os.path.join(archiveFolder, f)
            os.rename(os.path.join(softwarePath, f), destinationFile)
            print('Archived {0}.'.format(destinationFile))

version = GetVersion()
if BuildSetupPackage():
    CopyPackage(version)
    CopyReleaseNote()
    MoveOldPackage()
else:
    print("Can't proceed because build is failed.")

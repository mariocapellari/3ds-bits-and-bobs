-- add dvs code folder location to custom plugin setup

baseDir = pathConfig.removePathLeaf(getDir C:\\dvs)
iniFile = baseDir + "\\Plugin.UserSettings.ini"
setIniSetting iniFile "Directories" "DVS Code" "C:\\dvs\code"

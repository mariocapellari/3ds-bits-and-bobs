/* this is the default file to place in 3ds Max's default folder
   location. 
   it will set the custom PlugIns path to point to our DVS-Tools 
   folder location and load any *.ms scripts on startup
*/

-- set the custom plugins path
python.executeFile("C:\\Users\\dreamview\\Documents\\GitHub\\3ds-bits-and-bobs\\DVS_Setup.py")
python.executeFile("C:\\Users\\dreamview\\Documents\\GitHub\\3ds-bits-and-bobs\\createDVSMenu.py")



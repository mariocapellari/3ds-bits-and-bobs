'''
     Scaffolding to built out DVS Auto Loader for 3ds Max
'''
import MaxPlus
import sys
sys.path.append('Q:\\Shared drives\\DVS_Production\\Software\\DVS\\3DSMax\\python\\')
#sys.path.append('Q:\Shared drives\DVS_Production\Software\\DVS\3DSMax\python')

def outputMenuItem(item, recurse=True, indent=''):
    text = item.GetTitle()
    print indent, text if text else "----"
    if item.HasSubMenu and recurse:
        outputMenu(item.SubMenu, recurse, indent + '   ')


def outputMenu(menu, recurse=True, indent=''):
    for i in menu.Items:
        outputMenuItem(i, recurse, indent)

somethingHappened = False


def doSomething():
    global somethingHappened
    somethingHappened = True
    print 'Something happened'

action = MaxPlus.ActionFactory.Create(
    'Do something', 'Python demos', doSomething)
    
def doUI_Test():
    print 'This is create_DVS_Menu calling UI_Test'
    import UI_Test
    print dir(UI_Test)
    UI_Test.main()
    #~ print sys.path[-1]
    
action = MaxPlus.ActionFactory.Create(
    'Do something', 'UI_Test.py', doUI_Test)
    


def createTestMenu(name):
    if not MaxPlus.MenuManager.MenuExists(name):
        mb = MaxPlus.MenuBuilder(name)
        if action._IsValidWrapper():
            print "Created action"
        else:
            print "Failed to create action"
        mb.AddItem(action)
        mb.AddSeparator()
        menu = mb.Create(MaxPlus.MenuManager.GetMainMenu())
        print 'menu created', menu.Title
    else:
        print 'The menu ', name, ' already exists'


def getLastMenuItem(menu=MaxPlus.MenuManager.GetMainMenu()):
    return list(menu.Items)[-1]
    


def testLastItem(text):
    assert(getLastMenuItem().Title == text)

def main():
    print "Seriously, I AM MAIN!!!"
    
    print "Removing any previously left 'menu items'"
    MaxPlus.MenuManager.UnregisterMenu(u"DVS")
    
    print "Creating a new menu"
    createTestMenu(u"DVS")
    outputMenu(MaxPlus.MenuManager.GetMainMenu(), False)
    testLastItem(u"DVS")

    # assert(not somethingHappened)
    # mi = getLastMenuItem()
    # mi = list(mi.SubMenu.Items)[0]
    # ai = mi.ActionItem
    # ai.Execute()
    # assert(somethingHappened)

    # print "Unregistering the 'test' menu"
    # MaxPlus.MenuManager.UnregisterMenu(u"Test")
    # outputMenu(MaxPlus.MenuManager.GetMainMenu(), False)
    # testLastItem(u"&Help")


if __name__ == '__main__':
    main()

import os

def openLink():
    theLink = 'cmd /c "start explorer https://meet.google.com"'
    os.system(theLink)

def openLink(linkText):
    linkText = 'cmd /c "start explorer '+linkText+'"'
    os.system()

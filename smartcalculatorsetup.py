from cx_Freeze import *

includefiles = ['cal.ico']
base = Nope
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFloder", #Directory_
     "My Calculator", #name
     "TARGERDIR", #Component_
     "[TARGETDIR]\Smartcalculator.exe", #Target
     None, #arguments
     None, #description
     None, #Hotkey
     None, #Icon
     None, #IconIndex
     None, #ShowCmd
     "TARGETDIR", #WkDir
      )
]

msi_data = ("Shortcut": shortcut_table)

#change some default MSI options and specify the use of the above defined tables














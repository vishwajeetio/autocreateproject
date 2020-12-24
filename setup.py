import sys
from cx_Freeze import *


build_exe_options = {
    "packages":[
        "tkinter",
        "subprocess",
        "os",
        "json",
        "sys"
    ],
    "include_files":[
        "logo.png",
        "logo.ico"
    ]
}


# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Create Project",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]autoCreate.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]
# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}
# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {'data': msi_data}



base = None
if sys.platform == 'win32':
    base = "Win32GUI"

setup(
    name = 'Create Project',
    version = '0.01',
    author = 'visl.me',
    description = 'Create new python project with all the reqired files',
    options = {
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables = [
        Executable(
            'autoCreate.py',
            base = base,
            icon = 'logo.ico'
            # shortcutName = 'stock',
            # shortcutDir = 'DesktopFolder'
        )
    ]
)
import sys
import os
from cx_Freeze import setup, Executable

# Add the files directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'files'))

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'packages': [],
    'excludes': [],
    'include_files': [
        'files/',
        'static/',
        'templates/',
        'config.json'
    ],
    'bin_excludes': ['libcrypto-1_1.dll', 'libssl-1_1.dll'],  # Exclude problematic DLLs
}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable(
        'main.py', 
        base=base, 
        target_name='md-profi.exe', 
        icon='icon.ico',
        shortcut_name='MD Profi',
        shortcut_dir='DesktopFolder'
    )
]

setup(
    name='md-profi',
    version='1.0',
    description='Markdown Previewer',
    options={'build_exe': build_options},
    executables=executables
)
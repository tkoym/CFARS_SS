"""PyInstaller hook to include "hidden" sklearn modules"""

from PyInstaller.utils.hooks import collect_submodules
hiddenimports = collect_submodules('sklearn') 

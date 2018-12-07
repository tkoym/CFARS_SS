# -*- mode: python -*-
"""This PyInstaller spec file will create a "one dir" executable.
A folder containing the exe and all supporting files will be
created inside the dist directory.

The hookspath will pull in custom hooks (e.g., hook-sklearn.py).

To use:
`pyinstaller --clean onedir.spec`
"""

block_cipher = None


a = Analysis(['CFARS_SS_Phase1_Analysis.py'],
             pathex=['C:\\Users\\todd.koym\\Documents\\GitHub\\CFARS_SS'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['.'],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='CFARS_SS_Phase1_Analysis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='CFARS_SS_Phase1_Analysis')

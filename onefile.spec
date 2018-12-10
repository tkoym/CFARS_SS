# -*- mode: python -*-

"""This PyInstaller spec file will create a "one file" executable.
A single exe with statically-linked libraries will be created.
The user only needs this single file.

The hookspath will pull in custom hooks (e.g., hook-sklearn.py).

To use:
`pyinstaller --clean onefile.spec`
"""

block_cipher = None


a = Analysis(['CFARS_SS_Phase1_Analysis.py'],
             pathex=['.'],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='CFARS_SS_Phase1_Analysis',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )

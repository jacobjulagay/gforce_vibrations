# -*- mode: python ; coding: utf-8 -*-



block_cipher = None
#added_files = [
#   ('C:\\Users\\jacob\\Documents\\GitHub\\gforce_vibrations\\2021_01_22_202641_PowerMaster_ShockVibe.csv','.'),
#]

a = Analysis(['python_gui.py'],
             pathex=['C:\\Users\\jacob\\Documents\\GitHub\\gforce_vibrations'],
             binaries=[],
             datas=[],
             hiddenimports=['pandas','numpy','os','tkinter','sys','pathlib','matplotlib.pyplot'],
             hookspath=[],
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
          name='python_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )

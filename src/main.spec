# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import site
import os

a = Analysis(['main.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[('assets/styles.css', 'assets/'), ('assets/positive.csv', 'assets/'), ('assets/negative.csv', 'assets/')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pymzml_dir = os.sep.join([site.getsitepackages()[0], 'lib' , 'site-packages' ,'pymzml', 'version.txt'])
print('DIR', pymzml_dir)

a.datas += [('pymzml' + os.sep +'version.txt', pymzml_dir, 'DATA')]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
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
               upx_exclude=[],
               name='main')

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

import site
import os
import pymzml


def dir_files(path, rel):
    ret = []
    for p, d, f in os.walk(path):
        relpath = p.replace(path, '')[1:]
        for fname in f:
            ret.append((os.path.join(rel, relpath, fname),
                        os.path.join(p, fname), 'DATA'))
    return ret


a = Analysis(['main.py'],
             pathex=[os.getcwd()],
             binaries=[],
             datas=[('assets/styles.css', 'assets/'), ('assets/positive.csv', 'assets/'), ('assets/negative.csv', 'assets/')],
             hiddenimports=['pymzml','pymzml.run', 'pymzml.plot', 'pymzml.obo'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)


pymzml_dir = os.sep.join([site.getsitepackages()[0], 'lib' , 'site-packages' ,'pymzml', 'version.txt'])


a.datas += [('pymzml' + os.sep +'version.txt', pymzml_dir, 'DATA')]
a.datas.extend(dir_files(os.path.join(os.path.dirname(pymzml.__file__), 'obo'), 'obo'))


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


app = BUNDLE(exe,
         name='LipidIsotopeInference.app',
         icon=None,
         bundle_identifier=None)

         
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')

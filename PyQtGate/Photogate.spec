# -*- mode: python -*-
a = Analysis(['Photogate.pyw'],
             pathex=['/usr/lib/python2.7/dist-packages/PyQt4/', '/home/joco/Mercury/Codigos/Python/Photogate'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Photogate',
          debug=False,
          strip=None,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=None,
               upx=True,
               name='Photogate')

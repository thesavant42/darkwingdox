# darkwing_dox.spec
# PyInstaller spec file for Darkwing Dox v3.3

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

a = Analysis(
    ['darkwing_dox.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'pytesseract',
        'docx',
        *collect_submodules('docx'),
        'PIL.Image',
        'tkinter'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='darkwing_dox_v3.3',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='unsupervised.ico',  # Use your DW-themed icon here
    onefile=True
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='darkwing_dox'
)

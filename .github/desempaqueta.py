import os, glob, shutil, struct
os.makedirs('_site/f', exist_ok=True)
for f in ('index.html', 'app.enc'): shutil.copy(f, '_site/' + f)
open('_site/.nojekyll', 'w').close()
for p in glob.glob('p/*.bin'):
    b = open(p, 'rb').read(); i = 0
    while i < len(b):
        h = b[i:i + 40].decode(); n = struct.unpack('>I', b[i + 40:i + 44])[0]
        open('_site/f/' + h + '.enc', 'wb').write(b[i + 44:i + 44 + n]); i += 44 + n

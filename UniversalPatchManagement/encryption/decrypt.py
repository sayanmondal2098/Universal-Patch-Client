import gnupg
import os

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

path = os.path.expanduser('~/Code/Patch/Universal-Patch-Client/UniversalPatchManagement/encryption/test')
ptfile = '/a.txt.encrypted'

with open(path + ptfile, 'rb') as f:
    status = gpg.decrypt_file(f,
                              output= path  + ".decrypted")

print(status)
print(status.ok)
print(status.stderr)
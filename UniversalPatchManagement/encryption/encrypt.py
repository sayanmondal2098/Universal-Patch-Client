import gnupg
import os

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

path = os.path.expanduser('~/Code/Patch/Universal-Patch-Client/UniversalPatchManagement/encryption/test/')
ptfile = '/a.txt'

with open(path + ptfile , 'rb') as f:
    status = gpg.encrypt_file(f,
                              recipients=['test@test.com'],
                              output= path  + ".encrypted")
                              
print(status)
print(status.ok)
print(status.stderr)
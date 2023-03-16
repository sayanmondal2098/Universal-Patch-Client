import sys 

import getRemoteConfig.Test as test


sys.path.append('../')

sysdetails = test.getAllNetWorkInfo()

print(sysdetails)
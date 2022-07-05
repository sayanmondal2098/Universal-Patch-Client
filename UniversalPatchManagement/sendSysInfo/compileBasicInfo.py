import os
import sys 
sys.path.append('../')


import getRemoteConfig.Test as test


sysdetails = test.getAllNetWorkInfo()

print(sysdetails)
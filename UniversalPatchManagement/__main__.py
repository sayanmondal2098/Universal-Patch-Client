import platform
import sys
import os
from sysnet import get_network_interface_info, get_network_interfaces, get_gateway_info, getAllNetWorkInfo
from systemidentification import get_system_details
from syscmd import run_cmd
 
def main(args=sys.argv[1:]):
    """
    Main function.
    """
    print("System Details:")
    # print(platform.python_version())
    # print(os.getcwd())
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(platform.platform())
    # print(platform.system())
    # print(platform.release())
    # print(platform.machine())
    # print(platform.architecture())
    # print(platform.uname())
    # print(platform.version())
    # print(platform.python_build())
    # print(platform.python_compiler())
    # print(platform.python_branch())
    # print(platform.python_implementation())
    # print(platform.python_revision())
    # print(platform.python_version_tuple())



if __name__ == '__main__':
    main()
    print(getAllNetWorkInfo())
    print("*"*50)   
    print(run_cmd('ifconfig'))
    
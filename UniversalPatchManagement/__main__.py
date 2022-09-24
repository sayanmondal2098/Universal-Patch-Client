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
    print("Hello World!")


if __name__ == '__main__':
    #main()
    print(getAllNetWorkInfo())
    print("*"*50)  
    print(get_gateway_info())
    print("*"*50)   
    print(run_cmd('ifconfig'))
    print(run_cmd('ipconfig'))
    
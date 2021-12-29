import socket
import netifaces
import subprocess
import platform

# Return a list of network interface information
def get_network_interface_info(interface):
    """
    Returns a list of network interface information.
    """
    return socket.getaddrinfo(interface,None)

def get_network_interfaces():
    """
    Returns a list of network interfaces.
    """
    return socket.if_nameindex()

def get_gateway_info():
    """
    Returns a list of gateway information.
    """
    return netifaces.gateways()



def getAllNetWorkInfo():
    """
    Returns a list of network information.
    """
# cheeck the systrem operating system
    if platform.system() == 'Windows':
        data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
    else:
        data = subprocess.check_output(['ifconfig']).decode('utf-8').split('\n')
    return data
import sys 
import os
import platform

# Get System details
def get_system_details():
    """
    Returns a list of system details.
    """
    return (platform.uname() 
    + "/n" +(platform.python_version())
    + "/n" +(os.getcwd())
    + "/n" +(os.path.dirname(os.path.realpath(__file__)))
    + "/n" +(platform.platform())
    + "/n" +(platform.system())
    + "/n" +(platform.release())
    + "/n" +(platform.machine())
    + "/n" +(platform.architecture())
    + "/n" +(platform.uname())
    + "/n" +(platform.version())
    + "/n" +(platform.python_build())
    + "/n" +(platform.python_compiler())
    + "/n" +(platform.python_branch())
    + "/n" +(platform.python_implementation())
    + "/n" +(platform.python_revision())
    + "/n" +(platform.python_version_tuple()))



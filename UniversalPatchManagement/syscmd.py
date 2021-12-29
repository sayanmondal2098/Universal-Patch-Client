import cmd
import os

# run some command 
def run_cmd(cmd):
    """
    Runs a command and returns the output.
    """
    p = os.popen(cmd)
    return p.read()

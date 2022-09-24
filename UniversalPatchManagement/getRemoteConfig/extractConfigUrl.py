#read the config file
# with open('Source.config', 'r')
#      
f = open("Source.config", "r")

#print(f.read())
def strip_comments(item, *, token='#'):
    """Generator. Strips comments and whitespace from input lines.
    
    This generator strips comments, leading/trailing whitespace, and
    blank lines from its input.
    
    Arguments:
        item (obj):  Object to strip comments from.
        token (str, optional):  Comment delimiter.  Defaults to ``#``.
    
    Yields:
        str:  Next uncommented non-blank line from ``item`` with
            comments and leading/trailing whitespace stripped.
    
    """
    
    for line in item:
        s = line.split(token, 1)[0].strip()
        if s:
            yield s
    

line = strip_comments(f)
#print('\n'.join(h for h in line))

config_dict = {}
for line in line:
    print(line.split('=')[0])
    config_dict[line.split('=')[0]] = line.split('=')[1]

print(config_dict)

def getConfigDictfromSource():
    config_dict
import os
def create_file(name, perm):
    cleanup_file(name)
    with open(name, 'w') as f:
        f.write("")
    os.chmod(name, perm)

def cleanup_file(name):
    if name and os.access(name, os.F_OK):
        try:
            os.remove(name)
        except:
            pass
        
create_file('blim.py', 0444)
try:
    import studentMain
except:
    raise
finally:
    cleanup_file('blim.py')

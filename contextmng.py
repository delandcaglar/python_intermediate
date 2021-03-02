


with open('notes.txt','w') as file:
    file.write('some todoo.......')

file = open('notes.txt','w')

try:
    file.write('some todooo...')
finally:
    file.close()
    

class ManagedFile:
    def __init__(self,filename):
        self.filename = filename
    def __enter__(self):
        print('enter')
        self.file = open(self.filename,'w')
        return self.file
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handeled')
        print('exc:', exc_type, exc_val)
        print('exit')
        return True
        
with ManagedFile('notes.txt') as file:
    print('do some stuff')
    file.write("hahaha oldu mu lo")
    file.somemethod()
print('continuing')

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename,'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('haha lolo')


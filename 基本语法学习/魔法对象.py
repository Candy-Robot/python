"""
class FileObject:
    def __init__(self,filename = 'text.txt'):
        self.new_file = open(filename,'r+')
        
    def __del__(self):
        self.new_file.close()
        del self.new_file
"""
class C2F(float):
    def __new__(cls,temp=0.0):
        return float.__new__(cls,temp*1.8 + 32)
    

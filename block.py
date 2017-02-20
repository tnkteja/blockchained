import md5

class HashFunction(object):
    def __init__(self):
       self.method=self.__class__.__name__[:-12]
    
    def hash(data):
        return None
        

class Md5HashFunction(HashFunction):
    def __init__(self):
        super(self,Md5HashFunction).__init__()
        
    def hash(data):
        o=md5()
        o.update(data)
        return o.digest()
        
class Hashers(object):
    def __init__(self):
        self.map={
            "md5": None,
            "sha1": None
        }
        self.default=None
    
    def addHashFunction(self, hf, default=False):
        self.map[hf.method]=hf
        
 
class block(object):
   def __init__(self):
       self.
   
   def chain(self,other):
       pass
   
   def mine(self, hashers):
       pass

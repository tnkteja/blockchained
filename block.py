from md5 import md5

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
        self.hashType=None
        self.database=None
        self.previous=None
        self.next=None
        self.language=None
    
    def chain(self,other):
        self.next=other
        other.previous=self

    def mine(self, hashers):
        pass

 """
 MIT License

Copyright (c) 2017 Neela Krishna Teja Tadikonda

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 """
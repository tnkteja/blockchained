from md5 import md5
from sqlite import sqlite

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
        self.hashValue=None
        self.fact=None
        self.previous=None
        self.next=None
        self.language=None
    
    def chain(self,other):
        self.next=other
        other.previous=self

    def createConsensus(self):
        pass
    
class PersistantFactBlock(block):
    def __init_(self,persistantFact):
        super(PersistantFactBlock,self).__init__(self)
        self.persistantFact=None
        
class SmartContract(PersistantFactBlock):
    class ChainCode(object):
        class CodeType:
            INTREPRETED:0
                
        class Model(object):
            def __init__(self, kwargs={}):
                self.accessSpecifiers={}
                self.inheritPermissions=False
                self.__dict__.update(kwargs)
                self.parent=None
                self.children=[]
        
        class Controller(object):
            def __init__(self):
                self.permissions=None
            
            def create(self):
                pass
            
            def update(self):
                pass
            
            def delete(self):
                pass
            
            def onCreateHook(self):
                pass

            def OnUpdateHook(self):
                pass

            def OnDeleteHook(self):
                pass
        
        class View(object):
            def __init__(self):
                self.permissions=None
                
        def __init__(self):
            pass
        
    def __init__(self, initialData={"permissions":"all", "data":}, persistingCode, type=SmartContract.CodeType.INTERPRETED intrepreter="C:\Python27\python.exe"):
        super(SmartContract, self).__init__()
        
    def 
        
class Currency(block):
    POW=0
    def __init__(self):
        super(Currency,self).__init__()
        self.consensusType=Currency.POW
    
    def mine(self):
        pass
    
    def createConsensus(self):
        mine()
        
        
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

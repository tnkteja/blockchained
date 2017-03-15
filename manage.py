#!/usr/bin/python

import argparse
from json import dump, load
from os import remove, rename, system

parser = argparse.ArgumentParser(description='This tool is Chaincode Development Manager.')
parser.add_argument("--init", action="store_true",help="Initialise the Chaincode environment")
# parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
# parser.add_argument('--bootstrap', dest='bootstrap', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()


############################### UTILS #############################
def bash(cmd):
    print '\n'+'%'*32,"BASHING-BEGINS-HERE",'%'*32,'\n'

    print "Command: ",cmd,'\n'

    print "Output:\n"

    system(cmd)

    print '\n'

    print '%'*32,"BASHING-ENDS-HERE",'%'*32,'\n'

####################################################################

specification_template={
    "specification":{   
        "participants":[],
        "ccis": {
            "init": {
            },
            "invoke": {
            },
            "query": {
            }
        },
        "models": {
        }
    },
    "hashes": {
        "specification":'',
        "entities.go":'',  
        "ccis.go":''
    }
}

init=False
if args.init:
    name=raw_input()
    author=raw_input()
    with open("specification.json","w") as f:
        dump(specification_template,f)

specification=None
# hashes=None
# with open("specification.json","r") as f:
#     dic=load(f)
#     specification=dic["specification"]
#     hashes=dic["hashes"]


generate=False
if generate:
    pass

struct="""\
type %s struct {
%s
}
"""   

# with open("tmp_entities.go","w") as f:
#     print >> f, "package main\n"
#     for entity,attributes in models.items():
#         print >> f, struct%(entity,'')

# for file in ["tmp_entities.go"]:
#     system("gofmt "+file)
#     remove(file[4:])
#     rename(file,file[4:])

#setup=True
if setup:
    

#build=True
if build:
    print "You know this is not really required, but just running for Knitty Gritty."
    bash("go tool fix -r .")

#test=True
if test:
    print "Starting Unittests."
    bash("go test -v")
    print "Generating Test Coverage reports."
    bash("go tool cover -html=count.out -o test/coverage.html")
    browser=''
    bash(browser+" test/coverage.out")

credits=True
if credits:
    print """\
##########################################################################
################ HYPERLEDGER CHAINCODE DEVLOPMENT MANAGER ################
##########################################################################

Author: Neela Krishna Teja Tadikonda

Thanks to my team for the procurement project for the support and encouragement.
        * 
        *
        *
        *
        *
        *
        *
        *
        *
        *
        *
        *
        *
        * 

Finally special thanks to itpc - Mohan (CTO) and Sai (CEO) for supporting and encouraging me with the development of this tool.
"""

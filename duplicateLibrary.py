import collections
import os
def listorfile(user):
    """return if user is file or list"""
    try:
        if  os.path.exists(user+".txt") is True:
            return "File"
    except:
        return "list"

def lista(user):
    """return list without duplicate"""
    while 1:
        s=[item for item, count in collections.Counter(user).items() if count > 1]#found duplicate 
        if len(s)==0:
            return user
            break
        else:
            extract=0
            user.reverse()
            while len(s)-1>=extract:
                user.remove(s[extract])#remove duplicate from original list
                extract+=1
        user.reverse()
def file(user):
    """return if user a list of no duplicate elements in a file"""
    try:
        p=open(user+".txt","r")
        a=p.readlines()
        p.close()
        original=len(a)
        start_time = time.time()
        while 1:
            s=[item for item, count in collections.Counter(a).items() if count > 1]#found duplicate 
            if len(s)==0:
                return a
            else:
                extract=0
                a.reverse()
                while len(s)-1>=extract:
                    a.remove(s[extract])#remove duplicate from original list
                    extract+=1
            a.reverse()
    except:
        return "error"

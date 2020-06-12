import collections
import os
def listorfile(user):
    """Return if user is file or list!"""
    if  os.path.exists(user+".txt") is True:
        return "File"
    else:
        return "list"


       
def ListaDeleteLista2(lista,Lista2):
    contatore=0
    ricontatore=len(Lista2)
    while contatore!=ricontatore:
        if Lista2[contatore] in lista:
            eliminare=0
            while eliminare!=len(lista):
                if lista[eliminare]==Lista2[contatore]:
                    lista.pop(eliminare)
                    eliminare-=1
                eliminare+=1
        contatore+=1
        
    return lista   



def lista(user):
    """Return list without duplicate!"""
    while 1:
        
        s=[item for item, count in collections.Counter(user).items() if count > 1] #found duplicate 
        if len(s)==0:
            return user
            break
        else:
            extract=0
            user.reverse()
            while len(s)-1>=extract:
                user.remove(s[extract]) #remove duplicate from original list
                extract+=1
        user.reverse()
    
    
        
def file(user):
    """Return if user a list of no duplicate elements in a file!"""
    try:
        p=open(user+".txt","r")
        a=p.readlines()
        p.close()
        while 1:
            
            s=[item for item, count in collections.Counter(a).items() if count > 1] #found duplicate 
            if len(s)==0:
                return a
            else:
                extract=0
                a.reverse()
                while len(s)-1>=extract:
                    a.remove(s[extract]) #remove duplicate from original list
                    extract+=1
            a.reverse()
    except:
        return "error"

def listaduplicate(user):
    """Return only duplicate in a list!"""
    l=[]
    while 1:
        
        s=[item for item, count in collections.Counter(user).items() if count > 1] #found duplicate 
        if len(s)==0:
            return l
            break
        else:
            extract=0
            user.reverse()
            while len(s)-1>=extract:
                user.remove(s[extract]) #remove duplicate from original list
                l.append(s[extract])
                extract+=1
        user.reverse()

        
def duplicatefile(user):
    """Return if user a list of  duplicate elements in a file!"""
    m=[]
    try:
        p=open(user+".txt","r")
        a=p.readlines()
        p.close()
        while 1:
            
            s=[item for item, count in collections.Counter(a).items() if count > 1] #found duplicate 
            if len(s)==0:
                return m
            else:
                extract=0
                a.reverse()
                while len(s)-1>=extract:
                    a.remove(s[extract])#remove duplicate from original list
                    m.append(s[extract])
                    extract+=1
            a.reverse()
    except:
        return "error"

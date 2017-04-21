#check if all strings are unique

#s=raw_input().strip().split('i')

sas=raw_input()



def uniqcharacter(s):
    if len(s)>128:
        return False
    newar = [False]*128
    for char in s:
        #print newar[ord(char)]
        if newar[ord(char)]==False:
            newar[ord(char)]=True
        else:
            return False
    return True


#print uniqcharacter(sas)


def removedup(s):
    return ''.join([j for i,j in enumerate(s) if j not in s[:i]])

def checkanagrams(s):
    sas2 = raw_input()
    sl =sorted(s)
    s2l=sorted(sas2)
    if sl!=s2l:
        return False
    return True

def replaceme(s, sub, sub2):
    n = s.count(sub)
    print "number of replace %d"%n
    return s.replace(sub,sub2,n)


print replaceme(sas,'asd','A')
orderedPairsSet = set()

def sum(x,y):
    return x + y

def div(x,y):
    if (x % y == 0):
        return True
    else:
        return False

def checkPair(x,y,p,q):
    if(sum(x,y) > p and sum(x,y) < q and div(y,x)==True):
        #print "True: %d %d" % (x,y)
        orderedPairsSet.add((x,y))
        return True
    else: 
        #print "False: %d %d" % (x,y) 
        return False


def myRelation(p,q):
    if(p < q and p > 3 and q > 4):
        print "myRelation(%d, %d)" % (p,q)
        x = 1 # always odd
        y = 2 # always even

        # get ordered pairs incrementing y first
        checkPair(x,y,p,q)
        while (x <= p and y <= q):
            if (y+2 > q): # y cap
                y = 2
                x = x+2
                checkPair(x,y,p,q)
            else:
                y = y+2
                checkPair(x,y,p,q)
                
        print "List:" 
        print sorted(orderedPairsSet)
        #print "\n"

    else:
        print "invalid input"

myRelation(5,10) # expected: (1,6) (1,8) (3,6)
myRelation(6,15) # expected: (1,6) (1,8) (1,10) (1,12) (3,6)

'''
myRelation(5,10):
(1,6) (1,8) (3,6)

x odd
y even
(x+y) > p
(x+y) < q
x % y = 0

myRelation(6,15):
(1,6) (1,8) (1,10) (1,12) (3,6)
'''
#class Game:

allInfo={}
#Add new player to the allInfo dictionary
def createPlayer(player):
    allInfo.update({player:{'xPos':0,'yPos':0,'dir':0,'inv':{}}})


def movePlayer(player,distance):
    if allInfo.get(player) == None: #Check if player has already been created. If not, then declare player stats
        createPlayer(player)
    
    #Update player position based on distance and direction   
    if allInfo[player]['dir'] == 0:
        allInfo[player]['yPos']+=distance
    elif allInfo[player]['dir'] == 1:
        allInfo[player]['xPos']+=distance
    elif allInfo[player]['dir'] == 2:
        allInfo[player]['yPos']-=distance
    elif allInfo[player]['dir'] == 3:
        allInfo[player]['xPos']-=distance


def turnPlayer(player,direction):
    if allInfo.get(player)==None: #Check if player has already been created. If not, then declare player stats
        createPlayer(player)
    
    #Update player direction
    if direction=='right':
        if allInfo[player]['dir']==3:
            allInfo[player]['dir']=0
        else:
            allInfo[player]['dir']+=1
    elif direction=='left':
        if allInfo[player]['dir']==0:
            allInfo[player]['dir']=3
        else:
            allInfo[player]['dir']-=1


def mineItem(player,item):
    if allInfo.get(player)!=None:   #If player already exists
        if item in allInfo[player]['inv']:  #If item already exists
            allInfo[player]['inv'][item]+=1
        else:
            allInfo[player]['inv'][item]=1
    
    else:  #If player hasn't been created
        createPlayer(player)


def lookupInventory(player):
    x={}
    for inv_nm,inv_ct in allInfo[player]['inv'].items():
        x[inv_nm]=inv_ct
        print(inv_nm,":",inv_ct,end=' ')
    return x

def lookupItemOwners(item):
    x=[]
    for player,info in allInfo.items():
        if item in info['inv']:
            x.append(player)
            print(player,end=' ')
    return x

#To check distance between two players
def lookupDistance1(player1,player2):
    xd = abs(allInfo[player1]['xPos']-allInfo[player2]['xPos'])
    yd = abs(allInfo[player1]['yPos']-allInfo[player2]['yPos'])
    dist = xd+yd
    print (dist)
    return dist

#Function overloading works for different number of parameters
#To check distance between a player and given coordinates
def lookupDistance(player,xcoord,ycoord):
    xd = abs(allInfo[player]['xPos']-xcoord)
    yd = abs(allInfo[player]['yPos']-ycoord) 
    dist = xd+yd
    print (dist)
    return dist

#class Driver(Game):

def readandwrite():
    fr = open("input_file.txt")
    fw = open("output_file.txt","a")
    for line in fr:
        parts=line.split(':')
        inputs=parts[1].split(',')
        if parts[0] == 'movePlayer':
            inp=(inputs[0],int(inputs[1]))
            movePlayer(inp[0],inp[1])
            
        elif parts[0] == 'turnPlayer':
            turnPlayer(inputs[0],inputs[1])
            
        elif parts[0] == 'mineItem':
            mineItem(inputs[0],inputs[1].rstrip())
            
        elif parts[0] == 'lookupInventory':
            inv=lookupInventory(inputs[0].rstrip())
            for nm,ct in inv.items():
                fw.write(nm)
                fw.write(",")
                fw.write(str(ct))
                fw.write(" ")
            fw.write("\n")
            
        elif parts[0] == 'lookupItemOwners':
            owners=lookupItemOwners(inputs[0].rstrip())
            for i in owners:
                fw.write(i)
                fw.write(",")
            fw.write("\n")
            
        elif parts[0] == 'lookupDistance':
            try:
                (inputs[1])
                inp=(inputs[0].rstrip(),int(inputs[1]),int(inputs[2]))
                dist=lookupDistance(inp[0],inp[1],inp[2])
                fw.write(str(dist))
                fw.write("\n")
            except:
                dist=lookupDistance1(inputs[0].rstrip(),inputs[1].rstrip())
                fw.write(str(dist))
                fw.write("\n")
            
readandwrite()
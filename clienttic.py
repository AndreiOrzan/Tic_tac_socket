import socket


mat =[]


def matrix(mat):
    if mat[0][0]==mat[1][1]==mat[2][2]!=0:
        return mat[0][0]
    if mat[0][2]==mat[1][1]==mat[2][0]!=0:
        return mat[1][1]
    for i in range (3):
        if mat[i][0]==mat[i][1]==mat[i][2]!=0:
            return mat[i][0]
        if mat[0][i]==mat[1][i]==mat[2][i]!=0:
            return mat[0][i]
            

def win_check(dic):
    if dic["Win"][1] == 8: #remiza check
        dic["Win"][0] = 3
    
    if matrix(dic["mat"])==1 or matrix(dic["mat"])==2:
        dic["Win"][0] = matrix(dic["mat"])

        
def print_win(dic,soc,player,test):

    win_check(dic)
    
    if dic["Win"][0] != 0:
        if dic["Win"][0] == player :
            #soc.send(str(dic))
            print "You have won"
            test = 1
            dic["restart"] = True
            print dic
            
            
            #dic = {"id":1,"mat":[[0,0,0],[0,0,0],[0,0,0]],"Win":[0,0],"restart":True}
            
            


        elif dic["Win"][0] == 3:
            print "Draw"
        else:
            print "You have lost"
            print dic
            if dic["restart"] == True:# restarting and 
                dic["Win"]=[0,0]
                dic["mat"]=[[0,0,0],[0,0,0],[0,0,0]]
            print dic
            
            
                
            
def draw(mat):
    xy=[" ","X","O"]
    print ".___"*3+"."
    for i in range(3):
            #print " ____ "*3
            print "|_"+xy[mat[i][0]]+"_|_"+xy[mat[i][1]]+"_|_"+xy[mat[i][2]]+"_|"
            #print "|_",xy[mat[i][0]],"_|","|_",xy[mat[i][1]],"_|","|_",xy[mat[i][2]],"_|"

def client():
    HOST = 'localhost'    # The remote host
    PORT = 50007              # The same port as used by the server
    
    soc =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    soc.connect((HOST, PORT))
    
    test = 1
    
    while True:
        i,j = 0,0
        dic = eval(soc.recv(1024))
        
        
        if test == 1 :
            player = dic["id"]
            print "You are player ",dic["id"]
            if player == 1:
                other = 2
            else:
                other = 1 
            test = 0
            

        else:
            print_win(dic,soc,player,test)
            mat = dic["mat"]
            
            draw(dic["mat"])

                
            while True:
                

                
                while i < 1 or i > 3 :
                    try: 
                        i = int(raw_input("row :"))
                    except: 
                        print "please type in a valid input "
                    
                i = i - 1
                
                while j < 1 or j > 3:
                    try: 
                        j = int(raw_input("column :"))
                    except: 
                        print "please type in a valid input "
                j = j - 1
                
                if mat[i][j] == 0:
                    mat[i][j] = player
                    break
                else:
                    print "Position is occupied"
                    
            dic["mat"] = mat
            print_win(dic,soc,player,test)
            
            if dic["Win"][0] == 0:
                print "\n It is Player "+str(other)+"'s turn, please wait..\n"

            
            
            
            soc.send(str(dic))
            
client()

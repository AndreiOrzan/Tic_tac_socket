import socket

#def again(dic,soc):
#    restart =  raw_input("PLay again? Y/N")
#    if restart == "Y":
#        dic={"id":1,"mat":[[0,0,0],[0,0,0],[0,0,0]],"Win":0,"restart":"Y" }
#        print dic
#        soc.send(str(dic))

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
    test = 1
    soc =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    soc.connect((HOST, PORT))
    
    while True:
        
        dic = eval(soc.recv(1024))
        
        if test == 1 :
            player = dic["id"]
            print "You are player ",dic["id"]
            test = 0
        else:
        
            mat = dic["mat"]
            if dic["Win"] != 0:
                if dic["Win"] == player :
                    print "You have won"


                elif dic["Win"] == 3:
                    print "Draw"
                else:
                    print "You have lost"
                   
                soc.send(str(dic))
                
                    
            draw(mat)
            if dic["Win"] != 0:
                break
            while True:
                i = int(raw_input("row :"))
                while i < 1 or i > 3 :
                    i = int(raw_input("row :"))
                i = i - 1
                j = int(raw_input("column :"))
                while j < 1 or j > 3:
                    j = int(raw_input("column :"))
                j = j - 1
                if mat[i][j] == 0:
                    mat[i][j] = player
                    break
                else:
                    print "Position is occupied"
            
            dic["mat"] = mat
            soc.send(str(dic))
client()
import socket

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

def server():
    Host = ""
    Port = 50007
    dic={"id":1,"mat":[[0,0,0],[0,0,0],[0,0,0]],"Win":0}
    
    soc = socket.socket()
    soc.bind((Host,Port))
    soc.listen(2)
    
    test = []

    
    for i in range(2):
        conn,addr=soc.accept()
        print conn,"connected"
        test.append(conn)
        conn.sendall(str(dic))
       
        dic["id"]+=1
    dic["id"] = 1
    j = 0
    test[0].sendall(str(dic))
    remiza = 0
    for remiza in range(9):
        print "testing..."
        dic = eval(test[j].recv(1024))
        print "received", dic
        mat = dic["mat"]
        if remiza== 8:
            dic["Win"] = 3
        
        if matrix(mat)==1 or matrix(mat)==2:
            dic["Win"] = matrix(mat)
        if dic["id"] == 1:
            dic["id"] = 2
            j = 1
        else:
            dic["id"] = 1
            j = 0
            
        
        test[j].sendall(str(dic))
        
    
        
server()
    
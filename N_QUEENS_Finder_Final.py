import Finding_N_QUEENS as fq
import sys
def leftdiagonal(arr,row,col,n):
        j=col+1 
        i=row+1
        while i<n and j<n:
            if arr[i][j]!='Q':
                i+=1
                j+=1
            else:
                return 're'
        return 'pl'
def rightdiagonal(arr,row,col):
    j=col-1
    i=row+1
    while j>=0 and i<n:
        #print(i,j)
        if arr[i][j]!='Q':
            j-=1
            i+=1
        else:
            return 're'
    return 'pl'
def uprightdiagonal(arr,row,col):
    i=row-1
    j=col+1
    while i>=0 and j<n:
        if arr[i][j]!='Q':
            i-=1
            j+=1
        else:
            return 're'
    return 'pl'
def upleftdiagonal(arr,row,col):
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        #print(i,j)
        if arr[i][j]!='Q':
            i-=1
            j-=1
        else:
            return 're'
    return 'pl'
def colcheck(arr,col):
    i=0
    while i<n:
        if arr[i][col]!='Q':
            i+=1
        else:
            return 're'
    return 'pl'

def pos(arr,row,n):
    i=0
    temp=[]
    while i<n:
        colchk=colcheck(chess,i)
        lftd=leftdiagonal(chess,row,i,n)
        rgtd=rightdiagonal(chess,row,i)
        uprgtd=uprightdiagonal(chess,row,i)
        uplftd=upleftdiagonal(chess,row,i)
        if colchk=='pl'and lftd=='pl'and rgtd=='pl'and uprgtd=='pl'and uplftd=='pl':
            temp.append(i)
        i+=1
    return temp

def queens(n):
    que=[]
    for _ in range(0,n):
        que.append('Q')
    return que

def makearray(n):
    board=[]
    for _ in range(0,n):
        temp=[]
        for k in range(0,n):
            temp.append('.')
        board.append(temp)
    return board
n=int(input("Enter the size of the board to find the N-QUEENS:"))
if n<=5:
        fq.find(n)
        sys.exit()
#n=9
i=0
j=1
ans=[]
while i<n:
    chess=makearray(n)
    qu=queens(n)
    chess[0][i]='Q'
    qu.pop(0)
    while j<n:
        cf=pos(chess,j,n)
        for r in cf:
            chess[j][r]='Q'
            qu.pop(0)
            k=j+1
            while k<n:
                cf1=pos(chess,k,n)
                for r1 in cf1:
                    chess[k][r1]='Q'
                    qu.pop(0)
                    l=k+1
                    while l<n:
                        cf2=pos(chess,l,n)
                        for r2 in cf2:
                            chess[l][r2]='Q'
                            qu.pop(0)
                            m=l+1
                            while m<n:
                                cf3=pos(chess,m,n)
                                for r3 in cf3:
                                    chess[m][r3]='Q'
                                    qu.pop(0)
                                    p=m+1
                                    while p<n:
                                        cf4=pos(chess,p,n)
                                        for r4 in cf4:
                                            chess[p][r4]='Q'
                                            qu.pop(0)
                                            h=1
                                            g=0
                                            while h<n:
                                                while g<n:
                                                    if h!=j and h!=k and h!=l and h!=m and h!=p:
                                                        colchk=colcheck(chess,g)
                                                        lftd=leftdiagonal(chess,h,g,n)
                                                        rgtd=rightdiagonal(chess,h,g)
                                                        uprgtd=uprightdiagonal(chess,h,g)
                                                        uplftd=upleftdiagonal(chess,h,g)
                                                        if colchk=='pl'and lftd=='pl'and rgtd=='pl'and uprgtd=='pl'and uplftd=='pl':
                                                            chess[h][g]='Q'
                                                            qu.pop(0)
                                                            break
                                                        else:
                                                            g+=1
                                                    else:
                                                        break
                                                h+=1
                                                g=0
                                            if len(qu)==0:
                                                if chess not in ans:
                                                    ans.append(chess)
                                            chess=makearray(n)
                                            chess[0][i]='Q'
                                            chess[j][r]='Q'
                                            chess[k][r1]='Q'
                                            chess[l][r2]='Q'
                                            chess[m][r3]='Q'
                                            qu=queens(n)
                                            qu.pop(0)
                                            qu.pop(0)
                                            qu.pop(0)
                                            qu.pop(0)
                                            qu.pop(0)
                                        p+=1
                                    chess=makearray(n)
                                    chess[0][i]='Q'
                                    chess[j][r]='Q'
                                    chess[k][r1]='Q'
                                    chess[l][r2]='Q'
                                    qu=queens(n)
                                    qu.pop(0)
                                    qu.pop(0)
                                    qu.pop(0)
                                    qu.pop(0)
                                m+=1
                            chess=makearray(n)
                            chess[0][i]='Q'
                            chess[j][r]='Q'
                            chess[k][r1]='Q'
                            qu=queens(n)
                            qu.pop(0)
                            qu.pop(0)
                            qu.pop(0)
                        l+=1
                    chess=makearray(n)
                    chess[0][i]='Q'
                    chess[j][r]='Q'
                    qu=queens(n)
                    qu.pop(0)
                    qu.pop(0)
                k+=1
            chess=makearray(n)
            chess[0][i]='Q'
            qu=queens(n)
            qu.pop(0)
        j+=1
    i+=1
    j=1

for d in ans:
    for y in d:
        print(y)
    print('\n')

print(len(ans))

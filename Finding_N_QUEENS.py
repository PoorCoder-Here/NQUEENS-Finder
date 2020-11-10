def find(inp):
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
        n=inp
        #n=9
        i=0
        j=1
        k=2
        l=3
        ans=[]
        while i<n:
            chess=makearray(n)
            qu=queens(n)
            chess[0][i]='Q'
            qu.pop(0)
            while j<n:
                constant_fill=pos(chess,j,n)
                #print("constant_fill",constant_fill,j)
                for r in constant_fill:
                    #print("row",j,"fill",r)
                    chess[j][r]='Q'
                    qu.pop(0)
                    h=1
                    g=0
                    while h<n:
                        while g<n:
                            if h!=j:
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
                    #print("qu",qu)
                    if len(qu)==0:
                        if chess not in ans:
                            ans.append(chess)
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

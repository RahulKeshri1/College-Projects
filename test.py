def check(arr,row,col):
    sym=0
    skw=0
    for i in range(row):
        for j in range(col):
            if arr[i][j]==0:
                skw+=1
            elif arr[i][j]==-arr[j][i]:
                skw+=1
            elif arr[i][j]!=arr[j][i]:
                break
        if arr[i][j]!=arr[j][i]:
            break

    if skw==row*col:
        return "The Matrix is Skew Symmetric Matrix!"
    else:
        return "The Matrix is neither Symmetric Matrix nor Skew Symmetric Matrix."

import numpy as np
arr=np.zeros((3,3))
for i in range(3):
    for j in range(3):
        arr[i][j]=input()

print(arr)
ans=check(arr,3,3)
print(ans)
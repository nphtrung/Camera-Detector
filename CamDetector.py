class minHeap:
    def __init__(self):
        self.array= [0]
        self.size=0
    def insert(self,x,flag):
        self.array.append(x)
        self.size+= 1
        flag[x[0]]=self.size ##store position in heap
        i= self.size
        while i//2 >0:
            if self.array[i][2] < self.array[i//2][2]:
                #update position in flag and heap
                flag[self.array[i][0]],flag[self.array[i//2][0]]=flag[self.array[i//2][0]],flag[self.array[i][0]]
                self.array[i],self.array[i//2]=self.array[i//2],self.array[i]
            i=i//2

    def percDown(self,i,flag): #rearrange in heap
        while i*2 <=self.size:
            mc=self.minchild(i)
            if self.array[i][2]>self.array[mc][2]:
                #update position in flag and heap
                flag[self.array[i][0]], flag[self.array[mc][0]]=flag[self.array[mc][0]],flag[self.array[i][0]]
                self.array[i],self.array[mc]=self.array[mc],self.array[i]
            i=mc

    def delete(self,flag):
        element= self.array[1]
        self.array[1]=self.array[self.size]
        self.size -=1
        self.array.pop()
        self.percDown(1,flag)
        return element #return position of the vertice in heap

    def minchild(self,i):
        if i*2+1 > self.size:
            return i*2
        else:
            if self.array[i*2][2]<self.array[i*2+1][2]:
                return i*2
            else:
                return i*2 + 1


f = open("vertices.txt","r")
g = open("edges.txt","r")
edges=[[]for j in range(6105)]
cam = [0 for i in range(6105)]
for line in g:
    a = line.split()
    if len(a)== 3:
        edges[int(a[0])].append([int(a[1]),float(a[2])])
        edges[int(a[1])].append([int(a[0]),float(a[2])])

for line in f:
    a = line.split()
    cam[int(a[0])]=1 # store camera list in a binary list

start = int(input('Enter your location: '))
k = int(input('Enter k: '))

if cam[start]==1:
    print('Oops! Too late to help!!! Please smile for the camera')
else:
    discovered=minHeap()
    finalized=[]
    flag=[-2 for i in range(6105)]
    discovered.insert([start,start,0],flag) #Starting point
    flag[start]= -1 #finalized flag
    while len(discovered.array) > 1:
        distance = discovered.array[1][2] #shortest distance
        prever = discovered.array[1][0]

        if cam[discovered.array[1][0]]==1:
            finalized.append(discovered.array[1])
            flag[discovered.array[1][0]]=-1 #finalized flag
            discovered.delete(flag)
            continue

        flag[discovered.array[1][0]]=1 #update: discovered flag
        for j in edges[discovered.array[1][0]]:
            if flag[j[0]] == -2: #check not discovered flag
                discovered.insert([j[0],prever,j[1]+ distance],flag) #Insert to discovered list
            elif cam[j[0]]==1: # if camera, skip
                continue
            else:
                if discovered.array[flag[j[0]]][2]> j[1] + distance:
                    if flag[j[0]]> 0:
                        discovered.array[flag[j[0]]][2] = j[1] + distance
                        discovered.array[flag[j[0]]][1] = prever
                        discovered.percDown(flag[j[0]],flag)
        tmp=discovered.delete(flag)
        finalized.append(tmp)
        flag[tmp[0]]= -1 #finalized flag
    count=0
    path=[]

    for i in range(len(finalized)):
        if cam[finalized[i][0]]==1:
            if count < k:
                count+=1
                camera = finalized[i][0]
                dist = finalized[i][2]
                now = finalized[i]
                while dist!=0:
                    path.append(now[0])
                    next=now[1]
                    for current in range(i): # trace to next vertex

                        if finalized[current][0]==next:
                            dist = finalized[current][2]
                            now = finalized[current]

                print('Camera',count,':',camera, 'Distance from your location:',finalized[i][2])
                print('Shortest path:',end=" ")
                print(start,end=' ')
                for i in range(len(path)-1,-1,-1):
                    print('-->',path[i],end=' ')
                print('\n')
                path=[]
            else:
                break

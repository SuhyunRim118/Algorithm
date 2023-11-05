computerN = int(input())
connectionN = int(input())

connectionList = list()
connect1 = set()
connect1.add(1)

for c in range(connectionN):
    connect = list(map(int, input().split()))
    connectionList.append(connect)
    
for c in range(connectionN):
    for connect in connectionList:
        if connect[0] in connect1 or connect[1] in connect1:
            connect1.add(connect[0])
            connect1.add(connect[1])

print(len(connect1)-1)
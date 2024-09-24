import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dragon_curve():
    add_dragon = []
    add_dragon.append((dragon_set[-1][0],dragon_set[-1][1]))
    for i in range(len(dragon_set)-1,0,-1):
        x,y = dragon_set[i]
        nx,ny = dragon_set[i-1]
        for j in range(4):
            if x-nx == dir[j][0] and y-ny == dir[j][1]:
                if j == 0:
                    direction = 3
                else:
                    direction = j-1
                break
        add_dragon.append((add_dragon[-1][0]-dir[direction][0], add_dragon[-1][1]-dir[direction][1]))
    dragon_set.extend(add_dragon[1:])


n = int(input())

dir = [(0,-1),(1,0),(0,1),(-1,0)]
total_set = set()
answer = 0

for _ in range(n):
    x,y,d,g = map(int,input().split())
    dragon_set = []
    dragon_set.append((x,y))
    dx,dy = dir[d]
    dragon_set.append((x-dx,y-dy))
    for _ in range(g):
        dragon_curve()
    total_set.update(dragon_set)

for x,y in total_set:
    if (x,y+1) in total_set and (x+1,y) in total_set and (x+1,y+1) in total_set:
        answer += 1

print(answer)
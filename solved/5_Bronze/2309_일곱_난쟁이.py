import sys
sys.stdin = open('./input.txt', 'r')

seven = [int(sys.stdin.readline()) for _ in range(9)]
sum = 0
real_seven = [0]*7
visited = [False]*9
result = []

def perm(start, cnt):
    if cnt == 7:
        print('순열 끝')
        for k in real_seven:
            result.append(seven[k])
        result.sort()
        for _ in result:
            print(_)
        exit(0)
        return
    for i in range(start, 9):
        real_seven[cnt] = i
        perm(i+1, cnt+1)

perm(0,0)

def comb(cnt, sum):
    if cnt == 7:
        if sum == 100:
            for k in real_seven:
                result.append(seven[k])
            result.sort()
            for _ in result:
                print(_)
            exit(0)
        return
    for i in range(9):
        if visited[i]: continue
        visited[i] = True
        real_seven[cnt] = i
        comb(cnt+1, sum+seven[i])
        visited[i] = False

#comb(0,0)


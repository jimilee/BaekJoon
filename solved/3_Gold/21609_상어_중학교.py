import sys
from collections import deque

input = sys.stdin.readline
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def search(board, N):
    visited = [[False] * N for _ in range(N)]
    selected_blocks = []
    rainbow_cnt = 0
    start_block_x, start_block_y = -1, -1
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0 and visited[i][j] == False:
                tmp_selected_blocks = []
                tmp_rainbow_cnt = 0
                rainbows = []
                deq = deque([(i, j)])
                while deq:
                    x, y = deq.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < N and 0 <= ny < N:
                            if (board[nx][ny] == 0 and (nx, ny) not in rainbows) or (board[nx][ny] == board[i][j] and visited[nx][ny] == False):
                                if board[nx][ny] == 0:
                                    tmp_rainbow_cnt += 1
                                    rainbows.append((nx, ny))
                                else:
                                    visited[nx][ny] = True
                                deq.append((nx, ny))
                                tmp_selected_blocks.append((nx, ny))

                if len(tmp_selected_blocks) < len(selected_blocks):
                    continue
                elif len(tmp_selected_blocks) == len(selected_blocks):
                    if tmp_rainbow_cnt < rainbow_cnt:
                        continue
                    elif tmp_rainbow_cnt == rainbow_cnt:
                        if i < start_block_x:
                            continue
                        elif i == start_block_x:
                            if j < start_block_y:
                                continue
                rainbow_cnt = tmp_rainbow_cnt
                start_block_x, start_block_y = i, j
                selected_blocks = tmp_selected_blocks

    return selected_blocks, len(selected_blocks)


def delete_block(tmp_arr, blocks):
    for x, y in blocks:
        tmp_arr[x][y] = -5
    return tmp_arr


def gravity(tmp_arr):
    for j in range(N - 1, -1, -1):
        for i in range(N):
            if tmp_arr[j][i] == -5:
                move_x, move_y = i, j
                while 0 <= move_y - 1 and tmp_arr[move_y - 1][move_x] != -1:
                    move_y -= 1
                    if tmp_arr[move_y][move_x] >= 0: break
                if move_y != j:
                    tmp_arr[j][i] = tmp_arr[move_y][i]
                    tmp_arr[move_y][i] = -5
    return tmp_arr


def rotate(tmp):
    for _ in range(3):
        tmp = [list(_) for _ in zip(*tmp[::-1])]
    return tmp

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
while True:
    selected_blocks, selected_length = search(arr, N)
    if selected_length < 2: break
    result += selected_length ** 2
    arr = gravity(rotate(gravity(delete_block(arr, selected_blocks))))
print(result)
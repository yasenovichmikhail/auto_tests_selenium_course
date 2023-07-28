n, m = input().split()
n = int(n)
m = int(m)

def chess_board(n, m):
    board = [[0] * m for i in range(n)]
    for j in range(m):
        for i in range(n):
            if (j+i) % 2 != 0:
                board[i][j] = '*'
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                board[i][j] = '.'
    for row in board:
        print(*row)   
    
chess_board(n, m)
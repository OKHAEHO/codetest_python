array = [[0] * 8 for _ in range(8)]
#print(array)

knight = input("나이트의 위치를 쓰세요(a~h,1~8) : ")

row = int(knight[1])
col = int(ord(knight[0])) - int(ord('a'))+1
moves = [(-2,-1),(-2,1),(1,2),(1,-2),(2,1),(2,-1),(-1,2),(-1,-2)]
count = 0

for move in moves :
    move_row = row + move[0]
    move_col = col + move[1]
    if move_row >= 1 and move_row <= 8 and move_col >= 1 and move_row <= 8:
        count += 1

print(count)
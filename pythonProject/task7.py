# 7) Требуется определить, бьет ли ладья, стоящая на клетке с указанными координатами (номер строки и номер столбца),
# фигуру, стоящую на другой указанной клетке.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("YES")
else:
    print("NO")
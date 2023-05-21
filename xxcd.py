n = int(input())
matrix = []
up = 0
right = 0
dn = 0
left = 0

for i in range(n):
    matrix.append([0]*n)

for j in range(n):
    matrix[j] = input().split(" ")

for a in range(n):
    for b in range(n):
        if a < b and a < n - b - 1:
            up += int(matrix[a][b])
        elif a < b and a > n - b - 1:
            right += int(matrix[a][b])
        elif a > b and b > n - a - 1:
            dn += int(matrix[a][b])
        elif a > b and a < n - b - 1:
            left += int(matrix[a][b])
print("Верхняя четверть:", up)
print("Правая четверть:", right)
print("Нижняя четверть:", dn)
print("Левая четверть:", left)
n = int(input())
min_sum = 4

# 첫번째 수
for a in range(int(n**0.5), int((n//4)**0.5), -1):
    if a*a == n:
        min_sum = 1
        break
    else:
        temp = n - a*a
        # 두번째 수
        for b in range(int(temp**0.5), int((temp//3)**0.5), -1):
            if a*a + b*b == n:
                min_sum = min(min_sum, 2)
                continue
            else:
                temp = n - a*a - b*b
                # 세번째 수
                for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
                    if n == a*a + b*b + c*c:
                        # 여기까지 못 왔으면 답은 4
                        min_sum = min(min_sum, 3)

print(min_sum)
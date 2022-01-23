from sys import stdin

n = int(stdin.readline())

dp = [0, 1, 3, 5, 9, 15, 25, 41, 67, 109]
p = [0, 2, 2, 4, 6, 10, 16, 26, 42]

for _ in range(100):
    temp = (p[-1] + p[-2]) % 1000000007
    p.append(temp % 1000000007)
    dp.append((dp[-1] + temp) % 1000000007)

print(dp[])


"""
n=int(input())
dp=[0]*(n+1)
try:dp[0]=dp[1]=1
except:dp[0]=1
for i in range(2,n+1):
    dp[i]=(dp[i-1]+dp[i-2]+1)%int(1e9+7) #이부분을 1000000007로 바꾸니 AC나왔습니다
print(dp[n])
"""
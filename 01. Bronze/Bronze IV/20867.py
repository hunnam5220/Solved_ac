from sys import stdin

nums = {
    0: ['#', '#', '#', '#', '#', '#', '.', '.', '.', '#', '#', '#', '#', '#', '#'],
    1: ['#', '#', '#', '#', '#'],
    2: ['#', '.', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '.', '#'],
    3: ['#', '.', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
    4: ['#', '#', '#', '.', '.', '.', '.', '#', '.', '.', '#', '#', '#', '#', '#'],
    5: ['#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '.', '#', '#', '#'],
    6: ['#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '.', '#', '#', '#'],
    7: ['#', '.', '.', '.', '.', '#', '.', '.', '.', '.', '#', '#', '#', '#', '#'],
    8: ['#', '#', '#', '#', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
    9: ['#', '#', '#', '.', '#', '#', '.', '#', '.', '#', '#', '#', '#', '#', '#'],
    -1: ['.', '.', '.', '.', '.']}

n = int(stdin.readline())
data = list(stdin.readline().rstrip())
length = len(data)

number = [data[i * (length // 5): (i + 1) * (length // 5)] for i in
          range((length + (length // 5) - 1) // (length // 5))]
temp = []
ans = []
for i in range(length // 5):
    for j in range(5):
        temp.append(number[j][i])
        # 0과 1 구분해준다.
        if temp == nums[0]:
            ans.append(0)
            temp = []
        elif temp == nums[1] and i < (length // 5) - 1:
            if number[j][i + 1] == '.':
                ans.append(1)
                temp = []
        elif temp == nums[1] and i == (length // 5) - 1 and j == 4:
            ans.append(1)
            temp = []
        elif temp == nums[2]:
            ans.append(2)
            temp = []
        elif temp == nums[3]:
            ans.append(3)
            temp = []
        elif temp == nums[4]:
            ans.append(4)
            temp = []
        elif temp == nums[5]:
            ans.append(5)
            temp = []
        elif temp == nums[6]:
            ans.append(6)
            temp = []
        elif temp == nums[7]:
            ans.append(7)
            temp = []
        elif temp == nums[8]:
            ans.append(8)
            temp = []
        elif temp == nums[9]:
            ans.append(9)
            temp = []
        elif temp == nums[-1]:
            temp = []
for i in ans:
    print(int(i), end="")

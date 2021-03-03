from sys import stdin
key = {
    'E': 'I', 'I': 'E', 'S': 'N', 'N': 'S',
    'T': 'F', 'F': 'T', 'J': 'P', 'P': 'J'
}
result = ''
for step in list(str(stdin.readline().rstrip())):
    result += key[step]
print(result)
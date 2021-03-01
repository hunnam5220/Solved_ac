from sys import stdin

ml, mr, tl, tr = stdin.readline().rstrip().split()
msg = '?'

if (ml == 'R' and tl == 'S' and tr == 'S') or (ml == 'S' and tl == 'P' and tr == 'P') or (ml == 'P' and tl == 'R' and tr == 'R'):
    msg = 'MS'
if (mr == 'R' and tl == 'S' and tr == 'S') or (mr == 'S' and tl == 'P' and tr == 'P') or (mr == 'P' and tl == 'R' and tr == 'R'):
    msg = 'MS'

if (tl == 'R' and ml == 'S' and mr == 'S') or (tl == 'S' and ml == 'P' and mr == 'P') or (tl == 'P' and ml == 'R' and mr == 'R'):
    msg = 'TK'
if (tr == 'R' and ml == 'S' and mr == 'S') or (tr == 'S' and ml == 'P' and mr == 'P') or (tr == 'P' and ml == 'R' and mr == 'R'):
    msg = 'TK'

print(msg)
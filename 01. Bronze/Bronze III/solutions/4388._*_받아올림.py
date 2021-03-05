from sys import stdin


while 1:
    result = 0

    a, b = stdin.readline().rstrip().split()

    if int(a) == 0 and int(b) == 0:
        break

    else:
        a_ = list(reversed(a))
        b_ = list(reversed(b))

        if len(a_) >= len(b_):
            for x in range(len(a_)):
                try:
                    i = a_[x]
                    k = b_[x]

                    if int(a_[x]) + int(b_[x]) >= 10:
                        result += 1
                        try:
                            a_[x + 1] = str(int(a_[x]) + 1)
                        except:
                            pass
                    else:
                        continue
                except:
                    i = a_[x]

                    if int(a_[x]) >= 10:
                        result += 1
                        try:
                            a_[x + 1] = str(int(a_[x]) + 1)
                        except:
                            pass
                    else:
                        break
        else:
            for x in range(len(b_)):
                try:
                    i = b_[x]
                    k = a_[x]

                    if int(a_[x]) + int(b_[x]) >= 10:
                        result += 1
                        try:
                            b_[x + 1] = str(int(b_[x]) + 1)
                        except:
                            pass

                    else:
                        continue

                except:
                    i = b_[x]

                    if int(b_[x]) >= 10:
                        result += 1
                        try:
                            b_[x + 1] = str(int(b_[x]) + 1)
                        except:
                            pass
                    else:
                        break

        print(result)
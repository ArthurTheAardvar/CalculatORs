import sys

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return result / 10**n_digits

n_cases = int(input())
for _ in range(n_cases):
    # write your code starting here. replace these lines as needed:
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")

    a = float(line[0])
    b = line[1] 
    c = float(line[2])

    if b == "+":
        print(a + c, c + a)

    elif b == "-":
        print(a - c, c - a)

    elif b == "*":
        print(a * c, c * a)

    elif b == "/":
        d = better_round(a / c, 1)
        e = better_round(c / a, 1)
        print(d, e)
        
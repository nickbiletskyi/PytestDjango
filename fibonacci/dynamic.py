

def dynamic_fibo(n: int):
    f_list = [0, 1]

    for item in range(1, n+1):

        f_list.append(f_list[item]+f_list[item-1])

    return f_list[n]


def dynamic_fibo_v2(n: int):
    f_1, f_2 = 0, 1
    for item in range(1, n + 1):
        fib = f_1 + f_2
        f_1, f_2 = f_2, fib

    return fib
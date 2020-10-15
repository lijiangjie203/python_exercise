# 斐波那契数列模块

def fib1(n):
    """
    定义小于等于n的斐波那契数列
    :param n: 可能最大的 斐波那契数
    :return:
    """
    a, b = 0, 1
    while b < n:
        print(b, end=" ")
        a, b = b, a + b
    # print()


def fib2(n):
    """
    定义小于等于n的斐波那契数列
    :param n:  可能最大的 斐波那契数
    :return:    所有的 斐波那契数
    """
    a, b = 0, 1
    result=[ ]
    while b<n:
        result.append(b)
        a,b=b,a+b
    return result
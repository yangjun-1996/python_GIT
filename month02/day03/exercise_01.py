#!/usr/bin/python3

"""
求100000以内质数之和
"""

# 判断n是否为质数
def isPrime(n:int):
    if n <= 1:
        return False
    for i in range(2,n // 2 + 1):
        if n % i == 0:
            return False
    return True

def sum_prime(num):
    prime = [] # 存放质数
    for i in range(1,num + 1):
        if isPrime(i):
            prime.append(i)
    return sum(prime)

print(sum_prime(10000))





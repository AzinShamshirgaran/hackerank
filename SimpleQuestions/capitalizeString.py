#Given a full name, your task is to capitalize the name appropriately.

def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


if __name__ == '__main__':

    s = input()
    result = solve(s)
    print(result)

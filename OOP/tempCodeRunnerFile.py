n = input()
e = list(map(int, input().split()))
b = input()
f= list(map(int, input().split()))
common = e & f
full = e | f
one = full - common
print(len(one))

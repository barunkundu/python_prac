# n = int(input("enter a positive number: "))


# if n%2 != 0:
#     print("Weird")
# elif (n%2) == 0 and 2<= n <=5:
#     print("Not Weird")
# elif (n%2) == 0 and 6<= n <=20:
#     print("Weird")
# elif (n%2) == 0 and n>20:
#     print("Not Weird")
# else:
#     print("the number is odd and gater then 20")
                        

# a = int(input())
# b = int(input())

# print(a//b)
# print(a/b)

# n = int(input())
# for i in range(0,n):
#     print(i**2)

# n = int(input())

# print(n % 10)
# # if 1<=n<=150:
#     for i in range(1, n+1):
#         print(i)


# def mutate_string(string , position , character):
#     return string[:position] + character + string[position+1:]
# print(mutate_string("abracadabra", 5, "k"))


# def count_substring(string, sub_string):
#     count = 0
#     if 1<= len(string) <= 200:
#         for i in range(len(string)-len(sub_string)+1):
#             if string[i:i+len(sub_string)] == sub_string:
#                 count = count+1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)


# s = "1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# if 0<len(s)<1000:   
#     print(any(c.isalnum() for c in s))
#     print(any(a.isalpha()for a in s))
#     print(any(b.isdigit()for b in s))
#     print(any(d.islower()for d in s))
#     print(any(e.isupper()for e in s))

# s = input()

# # 1st line: Any alphanumeric character
# print(any(c.isalnum() for c in s))

# # 2nd line: Any alphabetical character
# print(any(c.isalpha() for c in s))


# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     arr= list(arr)
#     unique = list(set(arr))
#     unique.sort()

# print(unique[-2])


'''The provided code stub will read in a dictionary containing
     key/value pairs of name:[marks] for a list of students. 
        Print the average of the marks array for the student name provided, 
            showing 2 places after the decimal.'''           

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     beta = sum(student_marks[query_name])/len(student_marks[query_name])
#     print("{:.2f}".format(beta))


# if __name__ == '__main__':
#     s = input()
#     count = {}
#     for i in s:
#         if i.isalpha():
#             if i in count:
#                 count[i] = count[i] + 1
#             else:
#                 count[i] = 1
#     filtered = {k: v for k, v in count.items() if v > 1}
#     sorted_items = sorted(filtered.items(), key=lambda x: (-x[1], x[0]))
#     for char, count in sorted_items:
#         print(char, count)

# n = input()
# def convert(n):
#     result = "".join([char.lower() if char.isupper() else char for char in n])
#     return result

# n = input()
# def split_to_join(n):
#     result = "".join([n.split()],"-")
#     return result


# def print_full_name(first, last):
#     print(f"Hello {first_name} {last_name}! You just devlop into python.")
#     return


# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)

# m= input()
# a = m.split()
# lis1 =  list(map(int , a))


# n= input()
# # b = n.split()
# lis2 =  list(map(int , n.split()))
# print(lis2)

# d1 = (set(lis1) - set(lis2))
# d2 = (set(lis2) - set(lis1))
# print(d1)
# print(d2)
# u_re = sorted(d1 | d2)

# for number in u_re:
#     print(number)



# n = int(input("Enter number of elements: "))
# A = list(map(int, input("Enter the integers: ").split()))

# x = int(input("Enter the number to search for: "))

# if x in A:
#     print(f"{x} belongs to the set A")
# else:
#     print(f"{x} does not belong to the set A")


# m = int(input("Enter number of integers in each set (0 to 100000): "))

# if 0 <= m <= 10**5:
#     # First set: numbers from 0 to m-1
#     set1 = set(range(m))
    
#     # Second set: numbers from m to 2m-1 (non-overlapping)
#     set2 = set(range(m, 2*m))

#     print("Set 1 (first 10 elements):", list(set1)[:10])
#     print("Set 2 (first 10 elements):", list(set2)[:10])
#     print("Are sets disjoint?", set1.isdisjoint(set2))
# else:
#     print("Invalid input. m must be between 0 and 100000.")


# n= int(input("enter n number: "))
# if 1<= n <= 10**5:
#     arr = list(map(int, input("enter n value: ").split()))
#     # print(arr)

# A = list(map(int, input("enter A list: ").split()))
# B = set(arr) - set(A)

# m= int(input("enter m number: "))
# if 1<= m <= 10**5:
#     for i in range(m): 
#         c = list(map(int, input("your list: ").split()))
#         print(c)


# happiness = 0
# for c in len(c)+1:
#     for value in c:
#         if value in A:
#             happiness += 1
#         elif value in B:
#             happiness -= 1
# print(happiness)


# N = int(input())
# s = set()
# count= 0
# if 0<N<1000:
#     for i in range(N):
#         c = input()
#         s.add(c)
#         count += 1
# print(count)


# s = {1,2,3,4,5,6,7,8,9,0}
# print (s.pop())
# # print(s.remove(s[:]))
# print(s)

# print()


n = input()
e = list(map(int, input().split()))
b = input()
f= list(map(int, input().split()))
common = set(e) & set(f)
full = set(e) | set(f)
one = full - common
print(len(one))



# question_a
for i in range(0, 100, 10):
    print(i, end=' ')
print()

# question_b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# question_c
star = int(input("Number of stars: "))
for i in range(1, star + 1):
    print("*", end="")
print()

# question_d
line = int(input("Number of stars: "))
for i in range(1, line + 1):
    for j in range(i):
        print("*", end="")
    print()

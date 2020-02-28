import random

while True:
    global a
    a = [random.randint(-10, 10), random.randint(-10, 10)]
    global b
    b = [random.randint(-10, 10), random.randint(-10,10)]

    if a[0] == a[1]:
        print(str(a[0]) + ' and ' + str(a[1]) + ' are equal!')
        continue
    if b[0] == b[1]:
        print(str(b[0]) + ' and ' + str(b[1]) + ' are equal!')
        continue
    else:
        break

print(a)
print(b)
print()

length_a = len(a)
length_b = len(b)

print(length_a)
print(length_b)
print()

check = 2

a.sort()
b.sort()

start_a = -a[length_a - 1]
end_a = a[length_a - 1]

if start_a > end_a:
    start_a = a[length_a - 1]
    end_a = -a[length_a - 1]

print(start_a)
print(end_a)
print()

start_b = -b[length_b - 1]
end_b = b[length_b - 1]

if start_b > end_b:
    start_b = b[length_b - 1]
    end_b = -b[length_b - 1]

print(start_b)
print(end_b)
print()

a_span = list(range(start_a, end_a))
b_span = list(range(start_b, end_b))

length_a_span = len(a_span)
length_b_span = len(b_span)

print(a_span)
print(b_span)

if end_b > end_a:
    global summe
    summe = random.randint(-end_b, end_b)
    print(summe)

if end_a > end_b:
    summe = random.randint(-end_a, end_a)
    print(str(summe) + ' is the searched number.')

print()

for i in range(0, length_a_span - 1):
    global num_a
    num_a = a_span[i]
    for x in range(0, length_b_span - 1):
        num_b = b_span[x]
        if num_a + num_b == summe:
            print('Index ' + str(i) + ' in list a sorted, which is ' + str(num_a) + ', added with Index ' + str(x) +
                  ' in list b sorted, which is ' + str(num_b) + ' equal ' + str(summe))
            check = 1
if check == 2:
    print('There are no numbers in both lists, that add up to summe ' + str(summe) + '!')

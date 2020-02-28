a = [0, 0, -5, 8, -10, 1013, -100, 1]
b = [-10, 40, -3, 9, 8, 0, -5]
v = -15

length_a = len(a)
length_b = len(b)

a.sort()
b.sort()

print('This is list a = '+ str(a) + ' sorted.')
print('This is list b = '+ str(b) + ' sorted.')

check = 2

for i in range(0, length_a):
    global num_a
    num_a = a[i]
    for x in range(0, length_b):
        num_b = b[x]
        if num_a + num_b == v:
            print('Index ' + str(i) +' in list a sorted, which is ' + str(num_a) + ', added with Index ' + str(x) +
                  ' in list b sorted, which is ' + str(num_b) + ' equal ' + str(v))
            check = 1
if check == 2:
    print('There are no numbers in both lists, that add up to v !')






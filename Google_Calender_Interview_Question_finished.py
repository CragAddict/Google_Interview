schedule1 = [['10:00', '11:30'], ['12:00', '13:30'], ['13:30', '14:00'], ['14:15', '15:00'], ['15:30', '17:00']]

amount1 = len(schedule1)

schedule2 = [['09:00', '10:30'], ['12:00', '12:30'], ['12:30', '14:30'], ['14:45', '16:00'], ['17:00', '17:30']]

amount2 = len(schedule2)

time_required = 30

variable1 = 0
variable2 = 0

def Overlap():

    possible_time1 = freetime1[0]
    (h, m) = possible_time1.split(':')
    result1 = int(h) * 60 + int(m)   #person 1 free time start
    result1_inint = freetime1[0]

    possible_time12 = freetime1[1]
    (h, m) = possible_time12.split(':')
    result11 = int(h) * 60 + int(m)   #person 1 free time end
    result11_inint = freetime1[1]

    possible_time2 = freetime2[0]
    (h, m) = possible_time2.split(':')
    result2 = int(h) * 60 + int(m)  #person 2 free time start
    result2_inint = freetime2[0]

    possible_time22 = freetime2[1]
    (h, m) = possible_time22.split(':')
    result22 = int(h) * 60 + int(m) #person 2 free time end
    result22_inint = freetime2[1]

    list1 = list(range(result1, result11))
    list2 = list(range(result2, result22))

    for i in list1:

        if i == result2:
            #print('Your start time is in the other persons schedule')
            if result11 - result2 >= time_required:
                list12 = [result2_inint, result11_inint]
                print('You can have a meeting with person1, at '+ str(list12))
            else:
                print('Your free times are overlapping, but the time is not enough for a meeting!')

        if i == result22:
            #print('Your end time is in the other persons schedule')
            if result22 - result1 >= time_required:
                list21 = [result1_inint, result22_inint]
                print('You can have a meeting with person1, at '+ str(list21))
            else:
                print('Your free times are overlapping, but the time is not enough for a meeting!')

    for a in list2:
        if a == result1:
            #print('Your start time is in the other persons schedule')
            if result22 - result1 >= time_required:
                list21 = [result1_inint, result22_inint]
                print('You can have a meeting with person2, at ' + str(list21))
            else:
                print('Your free times are overlapping, but the time is not enough for a meeting!')

        if a == result11:
            #print('Your end time is in the other persons schedule')
            if result11 - result2 >= time_required:
                list12 = [result2_inint, result11_inint]
                print('You can have a meeting with person2, at '+ str(list12))
            else:
                print('Your free times are overlapping, but the time is not enough for a meeting!')
    scheduleOverlap1()

def scheduleOverlap1():


    for i in range(0, amount1):

        global  variable1
        #variable1 = 0

        v1 = variable1 + i

        if v1 == amount1 - 1:
            break

        time1 = schedule1[v1]
        time_span1 = time1[1]
        (h, m) = time_span1.split(':')
        result1 = int(h) * 60 + int(m)
        #print(result1)

        time2 = schedule1[v1 + 1]
        time_span2 = time2[0]
        (h, m) = time_span2.split(':')
        result2 = int(h) * 60 + int(m)
        #print(result2)

        if time1[1] == time2[0]:
            continue

        if time_required > result2 - result1:
            continue

        global freetime1
        freetime1 = [time1[1], time2[0]]
        print(freetime1)

        #global variable1
        variable1 = v1 + 1
        scheduleOverlap2()
        break


def scheduleOverlap2():



    for a in range(0, amount2):

        global variable2
        #variable2 = 0

        v2 = variable2 + a

        if v2 == amount2 - 1:
            break

        time1 = schedule2[v2]
        time_span1 = time1[1]
        (h, m) = time_span1.split(':')
        result1 = int(h) * 60 + int(m)
        #print(result1)

        time2 = schedule2[v2 + 1]
        time_span2 = time2[0]
        (h, m) = time_span2.split(':')
        result2 = int(h) * 60 + int(m)
        #print(result2)

        if time1[1] == time2[0]:
            continue

        if time_required > result2 - result1:
            continue

        global  freetime2
        freetime2 = [time1[1], time2[0]]
        print(freetime2)

        #global variable2
        variable2 = v2 + 1
        Overlap()
        break

scheduleOverlap1()








schedule1 = [['10:00', '11:30'], ['12:00', '13:30'], ['13:30', '14:00'], ['14:15', '15:00'], ['15:30', '17:00']]

amount1 = len(schedule1)

schedule2 = [['09:00', '10:30'], ['12:00', '12:30'], ['12:30', '14:30'], ['14:45', '16:00'], ['17:00', '17:30']]

amount2 = len(schedule2)

time_required = 30

variable1 = 0
variable2 = 0

def Overlap():
    print('fek')
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








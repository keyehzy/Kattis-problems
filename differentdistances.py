if(__name__ == '__main__'):
    while(True):
        test_case = list(map(float, input().split()))
        if(len(test_case) > 1):
            x1, y1 = test_case.pop(0), test_case.pop(0)
            x2, y2 = test_case.pop(0), test_case.pop(0)
            p = test_case.pop(0)
            num = str(round((abs(x1 - x2)**p + abs(y1-y2)**p)**(1/p),10))
            j = len(num.split('.')[0])
            result = ['0']*(10+1+j)
            for i in range(min(len(num),len(result))):
                result[i] = num[i]
            print(''.join(result))
        else:
            break

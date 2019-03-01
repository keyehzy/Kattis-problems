import math
def alphabetspam():
    spam  = input()
    
    a, l = [0]*4, len(spam)

    for s in spam:
        if s == '_':
            a[0] += 1.0 / l
        elif s.islower():
            a[1] += 1.0 / l
        elif s.isupper():
            a[2] += 1.0 / l
        elif not s.isalpha():
            a[3] += 1.0 / l
    for n in a:
        tol = math.pow(10,-15)
        print(abs(1 - round(n,15)/n) < tol)
        if abs(1 - round(n,15)/n) < tol:
            print(format(n, '.15f'))
        else:
            print(format(n, '.16f'))
    return

                
if __name__ == '__main__':
    alphabetspam()


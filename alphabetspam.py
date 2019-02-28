def alphabetspam():
    spam  = input()
    l = len(spam)
    
    white = 0.0
    lower = 0.0
    upper = 0.0
    symbols = 0.0
    for s in spam:
        if s == '_':
            white += 1.0 / l
        elif s.islower():
            lower += 1.0 / l
        elif s.isupper():
            upper += 1.0 / l
        elif not s.isalpha():
            symbols += 1.0 / l
    print(str('%.16f' % round(lower,17)))
    prin(lower - (lower - round(lower,16)))
    print(upper - (upper - round(upper,16)))
    print(symbols - (symbols - round(symbols,16)))
    return
    
                
if __name__ == '__main__':
    alphabetspam()


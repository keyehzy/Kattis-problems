def drmmessages(alpha):
    enc_message = input()
    s1 = list(enc_message[:len(enc_message)//2])
    s2 = list(enc_message[len(enc_message)//2:])

    p, q = rotate(s1, s2, alpha)
    for i, c in enumerate(p):
        k = (alpha[c] + alpha[q[i]]) % 26
        p[i] = chr(k + 65)

    print(''.join(p))
    return


def rotate(s1, s2, alpha):
    rotation_value1 = 0
    rotation_value2 = 0

    for i in range(len(s1)):
        rotation_value1 += alpha[s1[i]]
        rotation_value2 += alpha[s2[i]]
    
    for i in range(len(s1)):
        p = (alpha[s1[i]] + rotation_value1) % 26
        q = (alpha[s2[i]] + rotation_value2) % 26
        s1[i] = chr(p + 65)
        s2[i] = chr(q + 65)
    return s1, s2


if __name__ == '__main__':
    alpha =  {chr(i+65):i for i in range(0,26)} #alphabet dictionary
    drmmessages(alpha)



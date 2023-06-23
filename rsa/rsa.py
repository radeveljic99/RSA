import random


def miller_rabin(num):

    if num % 2 == 0:
        return False

    # Miller-Rabin primality test
    k = 0
    q = num - 1
    while q % 2 == 0:
        k += 1
        q //= 2

    for _ in range(20):
        a = random.randint(2, num - 2)
        x = pow(a, q, num)
        if x == 1 or x == num - 1:
            continue
        for _ in range(k - 1):
            x = pow(x, 2, num)
            if x == num - 1:
                break
        else:
            return False

    return True


def num_find(k):
    lower_bound = 10 ** (k - 1)
    upper_bound = (10 ** k) - 1

    while True:
        num = random.randint(lower_bound, upper_bound)
        if miller_rabin(num):
            return num


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1


def rsa_set(k):
    p = num_find(k)
    q = num_find(k)
    N = p*q
    fi_N = (p-1)*(q-1)
    e = 0

    while True:
        e = random.randint(2, fi_N)
        if is_coprime(e, fi_N):
            break

    d = pow(e, -1, fi_N)

    return p, q, N, e, d, fi_N


def rsa_enc(m, N, e):
    return [pow(ord(char), e, N) for char in m]


def rsa_dec(d, N, c):
    decripted =  [pow(char, d, N) for char in c]
    decripted_message = ""
    for i in range(len(decripted)):
        if decripted[i] > 127:
            decripted_message += chr(random.randint(1, 127))
        else:
            decripted_message += chr(decripted[i])
   
    return decripted_message         
        
            

p, q, N, e, d, fi_N = rsa_set(5)
encrypted_message = rsa_enc('Rade Veljic Adnan Cokovic Predrag Zunjic', N, e)
print(encrypted_message)
decrypted_message = rsa_dec(d, N, encrypted_message)
print(decrypted_message)

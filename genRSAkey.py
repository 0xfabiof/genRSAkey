import random as rand

def genRSAkey(length):

    factorLength=(length/2)          #Dividimos length em bits pretendida do n por 2 - obtemos a length pretendida para os factores p e q
    
    p=num_gen(factorLength +1)
    while(not is_probable_prime(p,64)):
        p+=2

    dif=length//2
    q=num_gen(factorLength +1)+dif      #Somamos dif a q para impedir uma ataque de Faulty key generation
    while(not is_probable_prime(q,64) or q==p):
        q+=2

    n=p*q
    f=(p-1)*(q-1)
    e=65537                        #Valor suficientemente grande para impedir ataques contra expoentes pequenos
                                   #Valor com grande eficiencia computacional pois trata-se de 2^16 + 1

    d=mulinv(e,f)                  #Calculo do inverso multiplicativo para obtencao do expoente privado d

    tuplo=(n,p,q,e,d)
    return tuplo

def num_gen(length):
    '''Bit mais significativo do length colocado a 1 de modo a garantir
    um p e q com o tamanho certo, o bit menos significativo a 1 para ser um
    valor impar'''

    p='1'
    i=0
    while(i<length-2):
        p+=str(rand.randint(0,1))
        i+=1

    p+='1'
    p=int(p,2)
    return p

def divisil_primos(n):
    '''Verifica de n e divisivel por uma lista de divisores comuns'''
    primos=[3,5,7,11,13,17,19]
    for i in primos:
        if n%i==0:
            return False
    return True

def is_probable_prime(n, k):
    '''Algoritmo Miller-Rabin para testar se um numero e primo'''
    if not divisil_primos(n):
        return False

    s, d = 0, n - 1
    while d & 1 == 0:
        s, d = s + 1, d >> 1

    for _ in xrange(k):
        a=rand.randrange(2,n-2)
        x = binpowmod(a, d, n)
        if x != 1 and x + 1 != n:
            for r in xrange(1, s):
                x = binpowmod(x, 2, n)
                if x == 1:
                    return False  # Nao e primo
                elif x == n - 1:
                    a = 0
                    break
            if a:
                return False  # Nao e primo
    return True  # Provavelmente e primo

def binpow(a, b) :
    '''Algoritmo de exponenciacao binaria, retorna a elevado a b'''
    res = 1
    while b > 0:
        if b & 1:
            res *= a
        a *= a
        b >>= 1

    return res

def binpowmod(a, b, m) :
    '''Algoritmo de exponenciacao modular, retorna a elevado a b modulo m'''
    res = 1
    a %= m
    while b > 0:
        if b & 1:
            res = res * a % m
        a = a * a % m
        b >>= 1
    return res

def mulinv(b, n):
    '''Retorna o inverso multiplicativo'''
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n

def egcd(a, b):
    '''Algoritmo de Euclides estendido'''
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

print(genRSAkey(2**12))

print("Sahil's Code\n")

p=int(input("Enter any prime number you like for p:"))
q=int(input("Enter any prime number you like for q:"))

def check(ip):
    if ip>1:
        for i in range(2,ip):
            if(ip%i)==0:
                return False
        else:
            return True
    else:
        return False

check_p=check(p)
check_q=check(q)
if (check_p==True) and (check_q==True):
    n=p*q
    r = (p -1) * (q-1)
    def egcd(e, r):
        while (r != 0):
            e, r = r, e % r
        return e
    for i in range(1, 1000):
        if (egcd(i, r) == 1):
            e = i
    def eugcd(e, r):
        for i in range(1, r):
            while (e != 0):
                a, b = r // e, r % e
                if (b != 0):
                    print(r," = ",a,"*",e," + ",b)
                r = e
                e = b
    def eea(a, b):
        if (a % b == 0):
            return (b, 0, 1)
        else:
            gcd, s, t = eea(b, a%b)
            s = s - ((a // b) * t)
            print(gcd," = ",a,"*",t,"+",s,"*",b )
            return (gcd, t, s)


    def inv(e, r):
        gcd, s,_ = eea(e, r)
        if (gcd != 1):
            return None
        else:
            if (s < 0):
                print("s=",s,". Since ",s," is less than 0, s = s(modr), i.e., s=",s % r)
            elif (s > 0):
                print("s=",s)
            return s % r


    def encrypt(p_k, n_txt):
        e, n = p_k
        x = []
        m = 0
        for i in n_txt:
            if (i.isupper()):
                m = ord(i) - 65
                c = (m ** e) % n
                x.append(c)
            elif (i.islower()):
                m = ord(i) - 97
                c = (m ** e) % n
                x.append(c)
            elif (i.isspace()):
                x.append(400)
        return x


    def decrypt(pr_k, c_txt):
        d, n = pr_k
        txt = c_txt.split(',')
        x = ''
        for i in txt:
            if (i == '400'):
                x += ' '
            else:
                m = (int(i) ** d) % n
                m += 65
                c = chr(m)
                x += c
        return x

    print("RSA ENCRYPTOR/DECRYPTOR")
    print("RSA Modulus is:", n)
    print("Euler's Toitent is:", r)
    print("The value of e is:", e)
    print("EUCLID'S ALGORITHM:")
    eugcd(e, r)
    d = inv(e, r)
    print("The value of d is:", d)
    public = (e, n)
    private = (d, n)
    print("Private Key is:", private)
    print("Public Key is:", public)
    mssg=input("Enter the comment,Separate numbers with ',' for below decryption:")
    ch=input("1->Encryption\n"
             "2->Decryption:")
    if (ch=="1"):
        en_msg=encrypt(public,mssg)
        print("encrypted message is:", en_msg)
    elif (ch=="2"):
        print("decrypted message is:", decrypt(private, mssg))
    else:
        print("Wrong option")
else:
    print("The values are invalid")

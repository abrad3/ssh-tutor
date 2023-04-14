import math
import functools
import operator
import time
import sys
def fun_print(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    print()
fun_print("Which positive integer would you consider your magic number? (and no, 0 and 1 are not acceptable!)")
magic_number=int(input())
fun_print("Thanks! "+str(magic_number)+" is a lovely number.")
fun_print("To perform encryption, we'll need to find the prime factors of this magic number.")
fun_print("Prime numbers are very special, since we (...or at least I) know that every integer greater than 1 is either a prime,")
fun_print("or can be written as a UNIQUE product of primes. This is called the... actually- maybe you know.")
fun_print("What is the name of this theorem? The...")
x=input()
if (x== "fundamental theorem of arithmetic") or (x=="Fundamental Theorem of Arithmetic") or (x=="FUNDAMENTAL THEOREM OF ARITHMETIC"):
    fun_print("Wow! You get a gold star! I like you.")
else:
    fun_print("Aww... it's okay, life is hard for a squishy brain like yours.")
    fun_print("It's called the FUNDAMENTAL THEOREM OF ARITHMETIC.") 
fun_print("Anyway, we can use this theorem to ensure that our magic number's factors are unique.")

def prime_finder(n):
    prime_factors=[]
    while (n % 2 == 0):
        prime_factors.append(2)
        n = n//2
    for i in range(3, int(math.sqrt(n))+2):
        while (n % i == 0):
            prime_factors.append(i)
            n = n//i
        i += 2
    if (n > 2):
        prime_factors.append(n)
    return prime_factors
factors =  prime_finder(magic_number)
time.sleep(1)
fun_print("The prime factors of your magic number are "+str(factors))
fun_print("We can then use these prime numbers to find the totient of your magic number.")
fun_print("The totient represents how many coprimes your magic number has.")
fun_print("...Do you know what coprime means? You look a bit glazed over.")
x=input()
if (x=="yes") or (x=="y") or (x=="Yes"): 
    fun_print("Cool beans, let's move on then.")
else: 
    fun_print("...I see. Well, if a number 'a' is coprime to a number 'b', their greatest commmon denominator is 1.")
    fun_print("This means that they share no prime factors (and thus, any factors!).")
    fun_print("Does that make sense?")
    x=input()
    if (x=="yes") or (x=="y") or (x=="Yes"):
        fun_print("Hooray, you learned something! Why stop there- let's keep learning!")
    else:
        fun_print("Really? Go google it then, and come back when it does make sense.")
        quit() 
fun_print("So the totient represents how many coprimes of your magic number there are in the set s = {1...magic number}.")
fun_print("It's defined as \"t= (p1-1)(p2-1)...(pn-1)\", where pi is the i-th prime factor of the magic number.")
totient = functools.reduce(operator.mul, [x-1 for x in factors],1)
time.sleep(1)
fun_print("Your magic number's totient is "+str(totient))
if totient <1:
    fun_print("This means we can't perform the encryption. Bummer. This script will now self-destruct in sadness")
    quit()
fun_print("We will next use the totient to find the ENCRYPTION and DECRYPTION numbers. The ENCRYPTION number is part of")
fun_print("the public key, while the DECRYPTION number is part of the private key.")
fun_print("I am too lazy to find the coprime for you. Input a number strictly between 1 and "+str(totient)+" and I'll let you know if it's coprime-")
fun_print("I believe in you!!")

coprime=totient
while (math.gcd(coprime, totient)!=1):
    coprime=int(input())
    if (math.gcd(coprime, totient)!=1):
        fun_print("That is not corpime to the totient "+str(totient)+". Try again.")
    else: 
        fun_print("Nice, "+str(coprime)+" is a valid coprime!")

fun_print("Next we need to find the multiplicative inverse of that coprime. I'm a bit busy watching Alex the Honking Bird, so could you guess one?")
fun_print("It'll be a number strictly between 1 and your totient.")
inverse=totient
while (math.gcd(inverse*coprime, totient)!=1):
    inverse=int(input())
    if (math.gcd(inverse, totient)!=1):
        fun_print("That is not the multiplicative inverse to the corpime mod by the totient "+str(totient)+".")
    if (inverse==1): fun_print("You can't pick one! Grrr, don't you care about security?")
    else: 
        fun_print("Wow, you found one?! Cool, let's get encrypting with your ENCRYPTION number "+str(inverse))

fun_print("Now we are ready to use the key lemma of RSA encryption:")
fun_print("a^(de) = a mod n,")
fun_print("where a is our message, represented by any positive integer,") 
fun_print("e is our ENCRYPTING coprime,") 
fun_print("d is the DECRYPTING inverse,") 
fun_print("and n is the magic number you chose at the very beginning. What a journey.")
fun_print("Now suppose I want to talk with you... privately ;) ")
fun_print("We first perform some kind of handshake that convinces you that I am the hot single in your area that you think I am.")
fun_print("Next, you give me your magic number n and the encrypting coprime e. It doesn't matter if other people find out about these numbers- they make up the PUBLIC KEY.")
fun_print("You keep the prime factors of your n secret, as well as the totient. I was able to calculate them from your n pretty easily, but in practice you would use a huge prime number (which I hope you didn't), which makes factorising very hard.")
fun_print("Now suppose I want to send you the message: \"Hey cutie!\", which in my encoding, looks like the number 6. Very realistic examples here.")
fun_print("Then the encrypted value is: 6^e = 6^"+str(coprime)+" = "+str(6**coprime))
fun_print("I send this value to you. You then raise it to the power of the decrypting number d:")
fun_print("(6^e)^d = (6^"+str(coprime)+")^"+str(inverse)+" = "+str(6**(coprime*inverse)))
fun_print("Finally, we find the modulo of this with respect to the magic number from the beginning:")
fun_print(str(6**(coprime*inverse))+" mod n="+str(6**(coprime*inverse))+" mod "+str(magic_number)+" = "+str(6**(coprime*inverse)%magic_number))
if ((6**(coprime*inverse))%magic_number==6):
    fun_print("Ta-da! This is my original flirty salutation!")
else:
    fun_print("Uh-oh, we should have gotten my original message (6) back. It's likely that this didn't work because you chose a magic number n smaller than my message. This is one of the flaws of this encryption- since if your message is larger than n, we can't fully recover the message, since a mod n might be several different numbers.")
fun_print("Woohoo, you learned! Did you enjoy it?")
x=input()
if (x=="yes") or (x=="y") or (x=="Yes"):
    fun_print("<3 Please tell my senpai Apollo they are the best then.")
else: fun_print(">:(")

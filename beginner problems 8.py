#1.1
import random
x = random.randint(1, 100)
A = False
e = 0
while not A:
    a = int(input("Enter a number: "))
    if a == x:
        print("You guessed it right!")
        e += 1
        print("It took you", e, "tries.")
        A = True
    elif a < x:
        print("Too low!")
        e += 1
    else:
        print("Too high!")
        e += 1

#1.2
a =int(input("What number stop are you at?"))
b = int(input("What number stop are you going to?"))
f =((b-a)*2.5+5)
print(f"The fare from stop {a} to stop {b} is ${f}")

#1.3
p = input("Enter your password: ")
s = 0
if len(p) > 7:
    s += 1
if any(c.isupper() for c in p):
    s += 1
if any(c.islower() for c in p):
    s += 1
if any(c.isdigit() for c in p):
    s += 1
if any(not c.isalnum() for c in p):
    s += 1
if s == 5:
    t = "Strong"
elif 3 <= s <= 4:
    t = "Moderately Strong"
else:
    t = "Weak"
print(t)

#1.4
import random
x = random.randint(1, 26)
A = False
e = 0
while not A:
    a = input("Enter a letter: ").strip().lower()
    g = ord(a) - ord('a') + 1
    e += 1
    if g == x:
        A = True
print(f"You guessed {e} times.")
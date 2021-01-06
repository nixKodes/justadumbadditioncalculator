print("Welcome to Nix's Addition Calculator")
print("Enter a number after the prompt firstnumber and hit enter,")
print("then enter a number after secondnumber and hit enter and so on.")
print("Enter up to 10 digits. If you need less then 10 inputs,")
print("Enter 0 for the remaining numbers")
x = input('firstnumber:')
y = input('secondnumber:')
z = input('thirdnumber: ')
a = input('fourthnumber: ')
b = input('fifthnumber: ')
c = input('sixthnumber: ')
d = input('seventhnumber: ')
e = input('eighthnumber: ')
f = input('ninthnumber: ')
g = input('tenthnumber: ')
print(
    int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) +
    int(f) + int(g))

if 9999 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 100000: 
  print("(It's in the ten-thousands)")

if 99999 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 1000000:  
  print("(It's in the hundred-thousands)")

if 1000000 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 10000000:  
  print("(It's in the millions)")

if 10000000 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 100000000:  
  print("(It's in the ten-millions)")

if 100000000 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 1000000000:  
  print("(It's in the hundred-millions)")

if 1000000000 < int(x) + int(y) + int(z) + int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) < 10000000000:  
  print("(It's in the billions)")
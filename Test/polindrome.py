x = "malayalam"
w = ""
for i in x:
    w = i + w

if (x == w):
    print("This is palindrome")
else:
    print("This is not palindrome")


#########

def palindrome(text):
    x = list(text)
    y = []
    y.extend(x)
    x.reverse()
    if (x == y):
        print("Palindorme")
    else:
        print("Not palindrome")


palindrome("sakthi")

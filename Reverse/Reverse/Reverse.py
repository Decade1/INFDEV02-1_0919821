rev = raw_input("What sentence should be reversed? ")

i = len(rev)

while i >= 1:
    print "\b" + rev[i - 1],
    i -= 1
print
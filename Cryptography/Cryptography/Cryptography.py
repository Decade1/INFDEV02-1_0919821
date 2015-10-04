sentence = raw_input("What word should be encrypted? ")
digi = False

while digi == False:
    shift = raw_input("And how many steps? ")
    if int(shift):
        digi = True

i = 0

while i < len(sentence):
    step = ord(sentence[i]) + int(shift)
    if step > ord('z'):
        step -= 26
    elif step < ord('a'):
        step += 26
    print "\b" + chr(step),
    i += 1
print
pw = raw_input("Pleas type in the password to check: ")

if pw.count(" ") >= 3:
    print "Here I kneel before you, oh mighty Passlord! \nYou have a strong password. "
elif len(pw) <= 4 or pw.islower() or pw.isupper() or pw.isdigit():
    print "Waaaaaaaaaaaaaay too weak (and probably short). \nTry adding both capitalized and lower case letters."
else:
    print "You're getting there! \nYour password is of medium strength."


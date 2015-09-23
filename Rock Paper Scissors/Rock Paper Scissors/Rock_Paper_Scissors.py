rps1 = raw_input("Player 1: rock, paper or scissors? ")
rps2 = raw_input("Player 2: rock, paper or scissors? ")
p1 = 0
p2 = 0

if rps1 in ("rock", "paper", "scissors"):
    if rps1 == "rock":
        p1 = 1
    if rps1 == "paper":
        p1 = 2
    if rps1 == "scissors":
        p1 = 3
else:
    print "Player 1, pick one!"

if rps2 in ("rock", "paper", "scissors"):
    if rps2 == "rock":
        p2 = 1
    if rps2 == "paper":
        p2 = 2
    if rps2 == "scissors":
        p2 = 3
else:
    print "Player 2, pick one!"

if p1 != 0 and p2 != 0:
    if p1 == 1 and p2 == 1:
        print "Both rock!"
    if p1 == 2 and p2 == 2:
        print "Both paper!"
    if p1 == 3 and p2 == 3:
        print "Both scissors!"
    if p1 == 2 and p2 == 1:
        print "Paper covers rock! Player 1 wins!"
    if p1 == 1 and p2 == 2:
        print "Paper covers rock! Player 2 wins!"
    if p1 == 1 and p2 == 3:
        print "Rock smashes scissors! Player 1 wins!"
    if p1 == 3 and p2 == 1:
        print "Rock smashes scissors! Player 2 wins!"
    if p1 == 3 and p2 == 2:
        print "Scissors cut paper! Player 1 wins!"
    if p1 == 2 and p2 == 3:
        print "Scissors cut paper! Player 2 wins!"
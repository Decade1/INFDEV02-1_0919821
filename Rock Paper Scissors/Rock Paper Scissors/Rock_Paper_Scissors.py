p1 = 0
p2 = 0

while p1 == 0:
    rps1 = raw_input("Player 1: rock, paper, scissors, lizard or Spock? ").lower()
    if rps1 in ("rock", "paper", "scissors", "lizard", "spock"):
        if rps1 == "scissors":
            p1 = 1
        if rps1 == "paper":
            p1 = 2
        if rps1 == "rock":
            p1 = 3
        if rps1 == "lizard":
            p1 = 4
        if rps1 == "spock":
            p1 = 5
    else:
        print "Player 1, pick one!"

while p2 == 0:
    rps2 = raw_input("Player 2: rock, paper, scissors, lizard or Spock? ").lower()
    if rps2 in ("rock", "paper", "scissors", "lizard", "spock"):
        if rps2 == "scissors":
            p2 = 1
        if rps2 == "paper":
            p2 = 2
        if rps2 == "rock":
            p2 = 3
        if rps2 == "lizard":
            p2 = 4
        if rps2 == "spock":
            p2 = 5
    else:
        print "Player 2, pick one!"

if p1 == p2:    
    if p1 == 1:
        print "Both scissors!"
    if p1 == 2:
        print "Both paper!"
    if p1 == 3:
        print "Both rock!"
    if p1 == 4:
        print "Both lizard!"
    if p1 == 5:
        print "Both Spock!"

if p1 != p2:
    if p1 == 2 and p2 == 3:
        print "Paper covers rock! Player 1 wins!"
    if p1 == 3 and p2 == 2:
        print "Paper covers rock! Player 2 wins!"
    if p1 == 3 and p2 == 1:
        print "Rock crushes scissors! Player 1 wins!"
    if p1 == 1 and p2 == 3:
        print "Rock crushes scissors! Player 2 wins!"
    if p1 == 1 and p2 == 2:
        print "Scissors cut paper! Player 1 wins!"
    if p1 == 2 and p2 == 1:
        print "Scissors cut paper! Player 2 wins!"
    if p1 == 1 and p2 == 4:
        print "Scissors decapitates lizard! Player 1 wins!"
    if p1 == 4 and p2 == 4:
        print "Scissors decapitates lizard! Player 2 wins!"
    if p1 == 4 and p2 == 2:
        print "Lizard eats paper! Player 1 wins!"
    if p1 == 2 and p2 == 4:
        print "Lizard eats paper! Player 2 wins!"
    if p1 == 3 and p2 == 4:
        print "Rock crushes lizard! Player 1 wins!"
    if p1 == 4 and p2 == 3:
        print "Rock crushes lizard! Player 2 wins!"
    if p1 == 4 and p2 == 5:
        print "Lizard poisons Spock! Player 1 wins!"
    if p1 == 5 and p2 == 4:
        print "Lizard poisons Spock! Player 2 wins!"
    if p1 == 5 and p2 == 3:
        print "Spock vaporizes rock! Player 1 wins!"
    if p1 == 3 and p2 == 5:
        print "Spock vaporizes rock! Player 2 wins!"
    if p1 == 2 and p2 == 5:
        print "Paper disproves Spock! Player 1 wins!"
    if p1 == 5 and p2 == 2:
        print "Paper disproves Spock! Player 2 wins!"
    if p1 == 5 and p2 == 1:
        print "Spock smashes scissors!"
    if p1 == 1 and p2 == 5:
        print "Spock smashes scissors! Player 2 wins!"
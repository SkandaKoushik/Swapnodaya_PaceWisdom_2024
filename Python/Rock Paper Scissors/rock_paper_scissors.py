import random

def play():
    u = input("Users Choose Rock(r), Paper(p), Scissors(s) >> ").lower()
    c = random.choice(['r', 's', 'p'])
    print(f"Computers Choice >> {c}")
    
    if u == c:
        print("\nIts a Tie")
        
    else:
        if (u == 'r' and c == 's') or (u == 's' and c == 'p') \
            or (u == 'p' and c == 'r'):
            print("\nUser Wins")
            
        else:
            print("\nComputer Wins")

            
play()
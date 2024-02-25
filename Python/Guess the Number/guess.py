import random

r = random.randint(1, 100)
g, c = 0, 0

while r != g:
    g = int(input("Guess a number between 1 and 100 : "))
    if g < r:
        print("Try Again. Too Low")
    elif g > r:
        print("Try Again. Too High")
        
print(f"\n\nCongrats. You have guessed the number {r} correctly!!")
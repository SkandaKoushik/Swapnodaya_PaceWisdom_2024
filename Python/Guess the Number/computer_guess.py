import random

low, high = 1, 100
feed = ''

while feed != 'c':
    if low != high:
        g = random.randint(low, high)
    else:
        g = low
        
    feed = input(f"Is Guess {g} Correct(C), Too Low(L) or Too High(H) >> ").lower()
    
    if feed == 'l':
        low = g + 1
    elif feed == 'h':
        high = g - 1
        
print(f"\n\nThe Computer guessed your number, {g}, Correctly")
            
    
    
    


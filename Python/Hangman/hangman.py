
import random
import string
from visuals import lives_visual_dict
from words import words


def choose_word():
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
        
    return word.lower()


word = choose_word()
word_letters = set(word)

letters = set(string.ascii_lowercase)
used_letter = set()

lives = 7

while len(word_letters) > 0 and lives > 0:
    
    print("Used Letters: ", used_letter)
    
    word_list = [l if l in used_letter else '_' for l in word]
    print(lives_visual_dict[lives])
    print('Current Word: ', word_list)
    
    l = input('\nGuess a letter >>  ').lower()
    
    if l in letters - used_letter:
        used_letter.add(l)
        if l in word_letters:
            word_letters.remove(l)
        else:
            lives -= 1
            print(f'{l} not in the word.') 
            
    elif l in used_letter:
        print('You have already used the letter, {l}.')
        
    else:
        print('\nInvalid Letter')
    
                
if lives == 0:
    print(lives_visual_dict[lives])
    print(f'You died. The word is {word}')
else:
    print('You guessed the word', word, '!!')
    

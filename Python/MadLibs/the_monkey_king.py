def madlibs():
    
    verb = input("verb: ")
    noun = input("noun: ")
    adjective = input("adjective: ")
    adverb = input("adverb: ")


    sen = f'''
        The day I saw the Monkey King {verb} was one of the most 
        interesting days of the year.

        After he did that, the king played chess on his brother's 
        {noun} and then combed his {adjective} hair with a 
        comb made out of old fish bones. Later that same day, I saw the 
        Monkey King dance {adverb} in front of an audience of kangaroos and wombats.
        '''
    print(sen)

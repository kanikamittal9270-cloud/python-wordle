def wordle(word,required = "TRIED"):
    word = word.lower()
    required = required.lower()
    if word == required:
        print("EXACT MATCH")
        return True
    for i in range(len(word)):
        letter = word[i]
        if letter in required and required[i] != letter:
            print("letter", letter , "is in the word but at wrong position")
    for i in range(len(word)):
        if (word[i]==required[i]):
            print ("The positions of", word[i] ,"is correct")
    print("REMAINNING LETTERS ARE NOT PRESENT")
    return False
guess = str(input("Enter your guess: "))
wordle(guess)
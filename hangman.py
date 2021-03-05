import random
import json

openWords = json.loads(open('').read()) # opens json file with words
words = openWords["nouns"]
guessedLetters = [] # stores all letters which user has entered
wrongLetters = []
lengthWords = len(words)
randNum = random.randint(0, lengthWords) # generates random number which will be used as index in json file to find word
computerWord = words[randNum - 1].lower()
compWordLength = len(computerWord)
userWord = list("_" * compWordLength)
numLives = int(input("How many lives would you like? "))


gameOver = False
print(userWord)
while gameOver == False: # game loop
    loopCount = 0 # used for calculating the number of lives left
    # checks if user input is valid
    userChoice = input("Enter a letter: ").lower()
    while len(userChoice) != 1:
        userChoice = input("Enter a valid letter: ").lower()
    while ord(userChoice) > 122 or ord(userChoice) < 97:
        print("Letter is not valid")
        userChoice = input("Enter a valid letter: ").lower()
    
    while userChoice in guessedLetters:
        print("Letter has already been guessed.")
        userChoice = input("Enter a valid letter: ").lower()

    # checks if the letter inputted by user is in word
    for i in range(compWordLength):
        if computerWord[i] == userChoice:
            userWord[i] = userChoice
            if loopCount == 0:
                numLives += 1
            loopCount += 1
    numLives -= 1
    guessedLetters.append(userChoice)
    print("Guessed letters are: " + str(guessedLetters))

    print("This is how much of the word you have guessed so far\n" + str(userWord))
    print("Amount of lives left: " + str(numLives) + "\n")
    # option for user to guess the word as long as they have at least 1 life
    if numLives > 0:
        wordBypass = input("Would you like to guess the word? y/n ").lower()
        if wordBypass == 'y':
            finalWord = input("Enter the word: ")
            if finalWord == computerWord:
                print("Congratulations! You guessed the word!")
                gameOver = True
            if finalWord != computerWord:
                print("You guessed wrong and lost an extra life:")
                numLives -= 1
                print("Amount of lives left: " + str(numLives))

    # checks if game is over
    if userWord == list(computerWord):
        print("Congratulations! The word was " + computerWord)
        gameOver = True

    if numLives == 0:
        print("You ran out of lives. Game over")
        print("The word was " + computerWord)
        gameOver = True
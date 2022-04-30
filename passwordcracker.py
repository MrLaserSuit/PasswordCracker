import time #Time module is used to tell us how long it take to crack the password

info = """
  Name            : Simple Password Cracker
  Created By      : Niklas Tageby
  Blog            : bullplay.org
  Documentation   : https://github.com/MrLaserSuit
  License         : Completely Free EDUCATION PURPOSE
  Thanks to       : Thank you GCSE
"""

#This program is powered by Niklas Tageby. I want to show how to think when building programs in python with a straightforward explanation.
#I choose to demonstrate it by creating a password cracker.

#We create a function and pass it a password
def passwordCracker(password):
    # time.time will give us the flag when we start, and another flag when our program is done
    startTime = time.time()
    #This is our dictionary I use only letters
    dictionary = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "V", "v", "U", "u", "W", "w", "X", "x", "Z", "z"]
    #We create a new list called letter
    letter = []
    #We create a new variable called pWord which equal to 'password' exactly passed in line 12
    pWord = password
    #Create a for loop, x going to check each letter in the password in the dictionary and jump to the next
    for x in range(0, len(pWord)):
        #Create another for loop, this y going to check all letters in our dictionary
        for y in range(0, len(dictionary)):
            #if x is equal to y, we got a match, append it to the letter list on line 18
            if pWord[x] == dictionary[y]:
                #append
                letter.append(dictionary[y])
                #Only to see what is happening we print out letter
                print(letter)

            else:
                print(letter)

    print(letter)
    #Now we print out the time it took
    endTime = time.time()
    #Totalt seconds it took, endtime - startTime
    elapsedTime = endTime - startTime
    print("That took", elapsedTime, "seconds to crack!")
#Call a password example it's up to you!
passwordCracker("Sweden")



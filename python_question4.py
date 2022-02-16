
def missing_char(word,n):
    if n in range(0,len(word)):
        new_word=word.replace(word[n],"")
        print("Here is the new word: ",new_word)
    else:
        print("Your number is out of range! Try another one")
word=input("Enter a word: ")
n=int(input("Enter an integer number: "))
missing_char(word,n)
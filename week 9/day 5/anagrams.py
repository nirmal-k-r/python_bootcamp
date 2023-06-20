from anagram_checker import AnagramChecker

an=AnagramChecker()
print("Welcome to the Anagram checker")

choice=None

while choice!='exit':
    choice=input("Enter a word or 'exit' to quit: ")
    choice=choice.strip().lower()
   

    if choice=='exit':
        break
    else:
        # print(choice)
        if choice.isalnum():
            # print('entered 1')
            # print( an.is_valid_word(choice))
            # if an.is_valid_word(choice):
            # print('entered 2')
            print("Your word: ",choice)
            print("this is a valid English word.")
            anagrams=an.get_anagrams(choice)
            # print(anagrams)
            print("Anagrams of ",choice," are: ",",".join(anagrams))

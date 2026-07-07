#Get the text from the user.
text = input("Please, input a text: ")


#create a vowel counting function
def count_vowel(text):
    #create a list of vowels
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    #a counter for storing the number of vowels
    num_vowel = 0
    
    #loop through the text and count every vowel.
    for char in text.lower():
        if char in vowels:
            num_vowel += 1
            
    return num_vowel
    
    
num_vowel = count_vowel(text)
print(f'There is/are {num_vowel} vowel(s) in {text}.')
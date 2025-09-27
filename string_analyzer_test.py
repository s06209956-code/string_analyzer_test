def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0 
    consonant_count = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                 vowel_count += 1
        else:
          consonant_count += 1
    return vowel_count, consonant_count           
def count_words(text):
    words = text.split()
    return len(words)
def longest_word(text):
    words = text.split()
    longest = max(words, key = len)
    return longest
def is_palindrome(text):
    text =text.lower()
    reverse = text[::-1]
    if (text == reverse):
        return True
    else:
        return False
string = input("Enter sentence:")
while True:
    print("STRING ANALYZER TEST:")
    print("1. Count vowels and consonants")
    print("2. Count words")
    print("3. Find longest number")
    print("4. Palindrome checker")
    print("5. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        v, c = count_vowels_consonants(string)
        print("Number of vowels:", v)
        print("Number of consonants:", c)
    elif choice == 2: 
        print("Number of words:", count_words(string))
    elif choice == 3: 
        print("Longest word:", longest_word(string))
    elif choice == 4:  
        print("Plaindrome or not string:", is_palindrome(string))
    elif choice == 5:
        print("Exit") 
        break
    else:
        print("Invalid Choice! Try Again")   


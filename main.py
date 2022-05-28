# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    # Convert both strings to lowercase
    word = word.lower()
    anagram = anagram.lower()
    # Loop through word
    for letter in word:
        # Check if the letter exists in anagram
        if anagram.find(letter) == -1:
            # Return False if it doesn't exist
            return False
    # Return True as the default case
    return True


print(find_anagram('Silent', "Listen"))
print(find_anagram("hello", "check"))
print(find_anagram("below", "elbow"))

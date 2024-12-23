# Python program to find the first non-repeating character in a string
# using a hashmap (dictionary) approach

def nonRepeatingChar(s):
    # Create a dictionary to store the frequency of characters
    char_count = {}

    # Count the occurrences of each character
    for char in s:
        # char_count[char] = char_count.get(char, 0) + 1
        if char in char_count:
          char_count[char] = char_count[char] + 1
        else: char_count[char] = 1
          
    # Find the first character with frequency 1
    for char in s:
        if char_count[char] == 1:
            return char

    # If no non-repeating character is found, return '$'
    return '$'

# Example input
s = "racecar"
print(nonRepeatingChar(s))

"""
This is a program that takes in input, such as a phrase, song lyrics, or other text, and "translates" 
the text into Ubbi Dubbi, the made up language from the PBS show Zoom. 

This language features a syllable "ub" in front of any vowell sound. 

For example, in Ubbi Dubbi, the phrase, " Peace on earth" would be "P-ub-eace ub-on ub-earth."

This program operates by taking in a string of only letters and spaces and adds in the "ub" syllable 
as it iterates over each letter in each word.

The new translated text is return to the console. 
"""

original = input("Enter your text or phrase: ")

syllable = 'ub'

vowel_sound = ['ai', 'ee', 'ea', 'eau', 'eu' 'oa', 'oi', 'oo', 'ou', 'ui']

# check if "y" comes at the begininng or at end
vowels = ["a". "e", "i", "o", "u", "y" ] 

text = original.lower()

text_lst = list(text)



new_list = []

new_list_as_str = str(new_list)

cap_str = new_list_as_str.capitalize()

print(cap_str)

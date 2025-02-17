path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read()

words = len(file_contents.split())

#print(file_contents)
#print(words)

my_string = file_contents
lowered_string = my_string.lower()
#print(lowered_string)

character_analysis = {
    "a" : 0,
    "b" : 0,
    "c" : 0,
    "d" : 0,
    "e" : 0,
    "f" : 0,
    "g" : 0,
    "h" : 0,
    "i" : 0,
    "j" : 0,
    "k" : 0,
    "l" : 0,
    "m" : 0,
    "n" : 0,
    "o" : 0,
    "p" : 0,
    "q" : 0,
    "r" : 0,
    "s" : 0,
    "t" : 0,
    "u" : 0,
    "v" : 0,
    "w" : 0,
    "x" : 0,
    "y" : 0,
    "z" : 0}

for chars in lowered_string:
        #print(chars)
        if chars in character_analysis:
              character_analysis[chars] = character_analysis[chars] + 1
print("--- Begin report of books/frankenstein.txt ---")
for summary in character_analysis:
      print(f"The '{summary}' character was found {character_analysis[summary]} times")

print("--- End report ---")
# m04_assn1_LT.py
# Logan Till
# 2025-04-13
# Count words in a file
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Count Words in a File (by Logan Till)")
print("***************************************\n")

# this will print the welcome message
print("Welcome!")
print("This program will count words in a file.\n")

# Import Libraries

# Input File
FILE_NAME = "bookpassage1.txt"

# Output File

# Constants

# Variables

# Function to strip punctuation from words
   #Functions are used for reusability and to keep organzied.
   #The argument is a single word, a string.
   #It returns a striped version of the word with no punctuation.
   #Scope: local variables only
def strip_word(word):
   
   
   return word.strip(".,;:")

# Function to count the words
   # Functions are used for reusability and to keep organzied.
   # The argument is the file name
   # Returns the word list and unique words
   # Scope: local variables only
   # CodingAssist-Ai: Deepseek helped write this function
def process_file(FILE_NAME):
   # Opens the file in read mode
   with open(FILE_NAME, 'r') as file:
      text = file.read()
   # Gets words from the text file
   words = text.split()
   # Calls strip word function
   cleaned_words = [strip_word(word) for word in words]
   # Gets unique words list
   unique_words = set(cleaned_words)

   return cleaned_words, unique_words

# Process the file and get word lists
all_words, unique_words = process_file(FILE_NAME)

# Sort the unique words
sorted_unique = sorted(unique_words)

# Display summary
print("Book Passage Word Count (by LT)")
print(f"# of words: {len(all_words)}")
print(f"# of unique words: {len(unique_words)}\n")

# Display the sorted unique words
print("Sorted Word List:\n")
for word in sorted_unique:
   print(word)
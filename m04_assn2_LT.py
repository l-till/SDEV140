# m04_assn2_LT.py
# Logan Till
# 2025-04-13
# Count unique words in a file
# Coding assistance was used in this program


# this will print the title of the program
print("\n***************************************")
print("Count Unique Words in a File (by Logan Till)")
print("***************************************\n")

# this will print the welcome message
print("Welcome!")
print("This program will count unique words in a file.\n")

# Import Libraries
# os needed to access path to file
import os

# Input File
DATA_FOLDER = "datafiles"
FILE_NAME = "bookpassage2.txt"
FILE_PATH = os.path.join(DATA_FOLDER, FILE_NAME)

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
def process_file(file_path):
   # Opens the file in read mode
   with open(file_path, 'r') as file:
      text = file.read()

   # Gets words from the text file
   words = text.split()

   # Calls strip word function and gets cleaned words
   cleaned_words = [strip_word(word).lower() for word in words]

   # Tracks the instances of a word
   # CodingAssistance-AI: AI fixed my code for counting instances
   word_instances = {}
   for word in cleaned_words:
      # Verifies length of word before counting
      if len(word) > 3:  
         if word in word_instances:
               word_instances[word] += 1
         else:
               word_instances[word] = 1
   return cleaned_words, word_instances

# Process the file and get word lists
all_words, word_instances = process_file(FILE_PATH)
# CodingAssistance-AI: AI fixed my code for counting instances
unique_words = word_instances.keys()

# Display summary
print(f"# of words: {len(all_words)}")
print(f"# of unique words: {len(unique_words)}\n")

# Display the sorted unique words
print("Sorted Word List:\n")
print(f"{'WORDS'} {'INSTANCES':>20}")
print(f"{'-----'} {'---------':>20}")
# CodingAssistance-AI: AI fixed my code for counting instances
for word, count in word_instances.items():
    print(f"{word:<15} {count:>10}")
from pyspark.sql import SparkSession
import re

# Create a Spark session
spark = SparkSession.builder \
    .appName("Word Types Identifier") \
    .getOrCreate()

# Function to preprocess text by removing punctuation and converting to lowercase
def preprocess_text(text):
    # Remove punctuation using regex and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    return cleaned_text

def is_palindrome(word):
    return word == word[::-1]

def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)

def process_text(text):
    # Preprocess the text to remove punctuation and convert to lowercase
    cleaned_text = preprocess_text(text)
    words = cleaned_text.split()

    total_count = len(words)
    palindrome_count = 0
    anagram_count = 0
    palindromes = []
    anagrams = []

    # Collect unique words for anagram checking
    unique_words = set(words)

    # Check for palindromes and prepare for anagrams
    for word in unique_words:
        if is_palindrome(word):
            palindrome_count += 1
            palindromes.append(word)

    # Check for anagrams
    checked_pairs = set()
    for word in unique_words:
        for other_word in unique_words:
            if word != other_word and (word, other_word) not in checked_pairs and (other_word, word) not in checked_pairs:
                if are_anagrams(word, other_word):
                    anagram_count += 1
                    anagrams.append((word, other_word))
                    checked_pairs.add((word, other_word))

    return total_count, palindrome_count, anagram_count, palindromes, anagrams

# Function to display menu
def display_menu():
    print("\nMenu:")
    print("1. List Palindromes")
    print("2. List Anagrams")
    print("3. Exit")

# Main function to run the application
def main():
    text = input("Please enter your text: ")
    total_count, palindrome_count, anagram_count, palindromes, anagrams = process_text(text)

    print("\nTotal word count:", total_count)
    print("Palindrome count:", palindrome_count)
    print("Anagram pairs count:", anagram_count)

    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            print("\nPalindromes found:")
            for word in palindromes:
                print(word)
        elif choice == "2":
            print("\nAnagrams found:")
            for word_pair in anagrams:
                print(f"{word_pair[0]} <-> {word_pair[1]}")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please choose again.")

# Run the application
if __name__ == "__main__":
    main()

# Stop the Spark session
spark.stop()

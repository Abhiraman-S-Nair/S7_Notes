from pyspark.sql import SparkSession
import re
from collections import defaultdict
from google.colab import files

# Upload the input file in Google Colab
uploaded = files.upload()  # Upload your input.txt file

# Initialize Spark session
spark = SparkSession.builder.appName("WordVowelConsonantCount").getOrCreate()

# Input and output file paths
input_path = "input.txt"  # Ensure this matches the uploaded file name
output_path = "results/output.txt"  # Output will be saved here

# Load the input file into an RDD
lines = spark.sparkContext.textFile(input_path)

# Function to count words, vowels, and consonants
def count_words_vowels_consonants(line):
    vowels = "aeiouAEIOU"
    word_count = len(line.split())
    vowel_count = sum(1 for char in line if char in vowels)
    consonant_count = sum(1 for char in line if char.isalpha() and char not in vowels)
    return ("words", word_count), ("vowels", vowel_count), ("consonants", consonant_count)

# Map each line to counts and reduce by key to get the total counts
counts = lines.flatMap(count_words_vowels_consonants) \
              .reduceByKey(lambda x, y: x + y)

# Save results to the output file
counts.saveAsTextFile(output_path)

# Display the results
output_rdd = spark.sparkContext.textFile(output_path)
print("Counts from results/output.txt:")
for line in output_rdd.collect():
    print(line)

# Stop the Spark session
spark.stop()

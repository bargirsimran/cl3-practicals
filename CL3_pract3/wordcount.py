from collections import defaultdict

def count_words(file_path):
    # Create a defaultdict to store word counts
    word_count = defaultdict(int)
    
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()  # Split the line into words
            for word in words:
                word_count[word.lower()] += 1  # Convert to lowercase to avoid case sensitivity
    
    # Print word counts
    for word, count in sorted(word_count.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    count_words(file_path)

from collections import defaultdict

def count_characters(file_path):
    # Create a defaultdict to store character counts
    char_count = defaultdict(int)
    
    # Open the file and read it line by line
    with open(file_path, 'r') as file:
        for line in file:
            for char in line:
                if char.isalpha():  # Consider only alphabets
                    char_count[char.lower()] += 1
    
    # Print character counts
    for char, count in sorted(char_count.items()):
        print(f"{char}: {count}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    count_characters(file_path)

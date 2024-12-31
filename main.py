def get_character_count(text):
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count only alphabetic characters
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    
    # Convert dictionary to list of tuples
    char_list = [{"char": char, "count": count} for char, count in char_count.items()]
    
    # Sort the list by the "count" field in descending order
    def sort_by_count(item):
        return item["count"]
    
    char_list.sort(key=sort_by_count, reverse=True)
    return char_list

def main():
    path = "/home/csoutherland/workspace/github.com/bootbot/frankenstein.txt"
    
    try:
        with open(path) as f:
            file_contents = f.read()
    except FileNotFoundError:
        print(f"Error: File at {path} not found.")
        return
    
    # Get word count
    words = file_contents.split()
    
    # Print report header
    print(f"--- Begin report of {path} ---")
    print(f"{len(words)} words found in the document\n")
    
    # Get and print character counts
    char_list = get_character_count(file_contents)
    for char_dict in char_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['count']} times")
    
    print("--- End report ---")
    return file_contents

# Run the program
file_contents = main()

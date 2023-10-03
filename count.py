# Name: Gabriella Salviano da Silva 
#Georgian ID: 200552337 
#Program: Computer programming 
#2 Semester

def count_word_frequency(file_path):
    word_count = {}  # Create an empty dictionary to store word frequencies
    with open(file_path, 'r') as file:  # Open the file in read mode
        text = file.read().lower()  # Read the content of the file and convert it to lowercase
        words = text.split()  # Split the text into words based on spaces
        for word in words:  # Iterate through each word in the list of words
            word = word.strip('.,!?()[]{}"\'')  # Remove common punctuation marks from the word
            if word in word_count:  # Check if the word is already in the word_count dictionary
                word_count[word] += 1  # If yes, increment the word count by 1
            else:
                word_count[word] = 1  # If not, add the word to the dictionary with a count of 1
    return word_count  # Return the dictionary containing word frequencies

def save_word_frequency_report(word_count, output_file):
    sorted_word_count = {k: v for k, v in sorted(word_count.items(), key=lambda item: item[1], reverse=True)}
    # Sort the word_count dictionary by values in descending order and create a new sorted dictionary
    with open(output_file, 'w') as file:  # Open the output file in write mode
        for word, count in sorted_word_count.items():  # Iterate through the sorted dictionary
            file.write(f'{word}: {count}\n')  # Write each word and its frequency to the output file

def main():
    input_file = '/Users/gabriellasalviano/Desktop/python/sample.txt'  # Define the path of the input file
    output_file = 'word_frequency_report.txt'  # Define the name of the output file

    # Count word frequency
    word_count = count_word_frequency(input_file)  # Call the function to count word frequencies

    # Save word frequency report
    save_word_frequency_report(word_count, output_file)  # Call the function to save the word frequency report

    print(f'Word frequency report saved to {output_file}')  # Print a message indicating the successful completion

if __name__ == "__main__":
    main()  # Call the main function if the script is executed directly

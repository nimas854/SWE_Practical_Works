import os
import string

def count_unique_words(text):

    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    

    unique_words = set(words)
    
  
    
    return unique_words


if __name__ == "__main__":
    path_to_txt = os.path.abspath("C:/Users/LENOVO/Desktop/SWE_Practical_Works/lab1/Sample.txt")

    text = ""
    with open(path_to_txt, 'r') as stream:
            text = stream.read()

            unique_words = count_unique_words(text)
            print("Unique Word Count: ", len(unique_words))
            print("-" * 80)


def Longest_words(text):

    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    words = text.split()
    

    longest_word = max(words, key=len) if words else ""
    
  
    
    return longest_word
longest = Longest_words(text)
print("Longest Word Count: ", len(longest))
print("-" * 80)

def count_word_occurrences(content, target_word):

    content = content.lower()

    target_word = target_word.lower()

    content = content.translate(str.maketrans('', '', string.punctuation))
    
    words = content.split()
    
    occurrences = words.count(target_word)
    
    return occurrences


target_word = input("Enter the word to count occurrences: ")
occurrences = count_word_occurrences(text, target_word)
print(f"Occurrences of '{target_word}': {occurrences}")
print("-" * 80)

def percentage_longer_than_average(content):
    content = content.lower()
    content = content.translate(str.maketrans('', '', string.punctuation))
    words = content.split()
    
    if not words:
        return 0.0  

    
    average_length = sum(len(word) for word in words) / len(words)

    
    longer_than_average_count = sum(1 for word in words if len(word) > average_length)

    percentage = (longer_than_average_count / len(words)) * 100
    return percentage

percentage = percentage_longer_than_average(text)
print(f"Percentage of words longer than the average word length: {percentage:.2f}%")
        
print("-" * 80)







        

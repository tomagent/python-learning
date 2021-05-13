import ch1text

# Count the sentences in the text
def count_sentences(text):
    count = 0

    terminals = '.;?!' # Use this characters to count the num of sentences
    for char in text:
        if char in terminals:
            count += 1

    return count

# Count the number of syllables
def count_syllables(words):
    count = 0
    
    for word in words: #Iterate through all the words
        word_count = count_syllables_in_word(word) # Get the num of syllables of the current word
        count += word_count # Add the syllables of the current word to the counter

    return count

# Count the syllables in each word
def count_syllables_in_word(word):
    count = 0

    # Remove final punctuation
    endings = ".,;!?:"
    last_char = word[-1]
    # Check if the last character is a punctuation
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word

    # 1. If the length of the word is less than 3, then it's only one syllable 
    if len(processed_word) <= 3: 
        return 1

    if processed_word[-1] in "eE":
        processed_word = processed_word[0:-1]
    
    # 2. Count number of vowels that represents syllables
    vowels = "aeiouAEIOU" # Variable that holds all the vowels
    prev_char_was_vowel = False

    for char in processed_word: # Iterate through each char of the word
        if char in vowels: # If the current character matches any of the characters is a vowel
            if not prev_char_was_vowel: # If the current character is a vowel and the previous wasn't
                count = count + 1 # Count it as a syllable
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False   

    # If it encounters a y as a the last character, it counts it as syllable
    if processed_word[-1] in "yY":
        count = count + 1
    
    return count    

def output_results(score):
    if score >= 90:
        print("Reading level of 5h Grade")
    elif score >= 80:
        print("Reading level of 6th Grade")
    elif score >= 70:
        print("Reading level of 7th Grade")
    elif score >= 60:
        print("Reading level of 8-9th Grade")
    elif score >= 50:
        print("Reading level of 10-12th Grade")
    elif score >= 30:
        print("Reading level of College Student")
    else:
        print("Reading level of College Graduate")

# Make the final computation of the readability
def compute_readability(text): 
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words = text.split() # Get the words in an array
    total_words = len(words) # Get total of words
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)

    score = (206.835 - 1.015 * (total_words / total_sentences)
        - 84.6 * (total_syllables / total_words))

    output_results(score)

compute_readability(ch1text.text)

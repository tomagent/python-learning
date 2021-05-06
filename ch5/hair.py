# hair = input("What color hair[brown]? ")
# if hair == "":
#     hair = "brown"
# print("You chose", hair)
#
# hair_length = input("What hair length [short]? ")
# if hair_length == "":
#     hair_length = "short"
# print("You chose", hair_length)
#
# eyes = input("What eye color [blue]? ")
# if eyes == "":
#     eyes = "blue"
# print("You chose", eyes)
#
# gender = input("What gender [female]? ")
# if gender == "":
#     gender = "female"
# print("You chose", gender)
#
# has_glasses = input("Has glasses [no]? ")
# if has_glasses == "":
#     has_glasses = "no"
# print("You chose", has_glasses)
#
# has_beard = input("Has beard [no]? ")
# if has_beard == "":
#     has_beard = "no"
# print("You chose", has_beard)

# Returns true if the question has two words
def two_words(string):
    if len(string.split("_")) >= 2:
        return True

# Breaks the words that have a underscore in between
def break_two_words(string):
    final_word = ""
    if two_words(string):
        split_word = string.split("_")
        for word in split_word:
            final_word += word + " "
        return final_word.capitalize()
    else:
        return string

# Asks for user preferences and print the statement of his choice
def user_preferences(attribute_question, predefined_answer):
    broke_word = break_two_words(attribute_question)
    if len(broke_word.split(" ")) <= 1:
        user_choice = input("What " + broke_word + " [" + predefined_answer + "]" + "? ")
    elif len(broke_word.split(" ")) >= 2:
        user_choice = input(broke_word + " [" + predefined_answer + "]" + "? ")
    if user_choice == "":
        user_choice = predefined_answer
    print("You choice", user_choice)

user_preferences("hair", "brown")
user_preferences("length", "short")
user_preferences("eyes", "blue")
user_preferences("gender", "female")
user_preferences("has_glasses", "no")
user_preferences("has_beard", "no")

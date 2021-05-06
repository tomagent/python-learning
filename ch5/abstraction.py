# def get_attribute(query, default):
#     question = query + " [" + default + "]? "
#     answer = input(question)
#     if (answer == ""):
#         answer = default
#     print("You chose", answer)
#     # return answer
#
# hair = get_attribute("What hair color", "brown")
# hair_length = get_attribute("What hair length", "short")
# eye = get_attribute("What eye color", "blue")
# gender = get_attribute("What gender", "female")
# glasses = get_attribute("Has glasses", "no")
# beard = get_attribute("Has beard", "no")

bank = 10500
camera_on = True

def steal(balance, amount):
    global camera_on
    camera_on = False
    if (amount < balance):
        balance = balance - amount

    return amount
    camera_on = True

proceeds = steal(bank, 1250)
print("Criminal: you stole", proceeds)

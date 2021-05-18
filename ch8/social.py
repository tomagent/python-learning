users = {}
users["Kim"] = {"email" : "kim@oreilly.com", "gender": "f", "age": 27, "friends": ["John", "Josh"]}
users["John"] = {"email" : "john@abc.com", "gender": "m", "age": 24, "friends": ["Kim", "Josh"]}
users["Josh"] = {"email" : "josh@wickedlysmart.com", "gender": "m", "age": 32, "friends": ["Kim"]}

def average_age(user):
    global users
    age = 0
    for friend in users[user]["friends"]:
        age += users[friend]["age"]
    print(user+"'s friends have an average age of", age/len(users[user]["friends"])) 
        
average_age("Kim")
average_age("John")
average_age("Josh")
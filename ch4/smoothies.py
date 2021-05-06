smoothies = ["coconut", "strawberry", "banana", "tropical", "acai berry"]

has_coconut = [True, False, False, True, False]

smoothies_length = len(smoothies)
for i in range(smoothies_length):
    if has_coconut[i]:
        print(smoothies[i], "contains coconut")

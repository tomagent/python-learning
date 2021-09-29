import csv
import numpy as np
from collections import Counter
import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv("data.csv")
ids = data["Responder_id"]
lang_responses = data["LanguagesWorkedWith"]
    
language_counter = Counter()

for response in lang_responses:
    languages = response.split(";")
    language_counter.update(languages)
        
languages = [language[0] for language in language_counter.most_common(15)]
votes = [language[1] for language in language_counter.most_common(15)]

languages.reverse()
votes.reverse()

plt.barh(languages, votes)

plt.title("Most Popular Languages")
plt.xlabel("Number of People Who Use")

plt.tight_layout()

plt.show()
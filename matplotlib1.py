from matplotlib import pyplot as plt

plt.xkcd()

# Ages
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# Salaries
dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.bar(ages_x, py_dev_y, label="Python")
plt.bar(ages_x, js_dev_y, label="Javascript")
plt.bar(ages_x, dev_y, color="#444444", linestyle="--", label="All Devs")

plt.title("Median Salary (USD) by Age")
plt.ylabel("Median Salary (USD)")
plt.xlabel("Ages")

plt.legend()

plt.tight_layout()

plt.savefig('plot.png')
plt.show()
# Define function to make a bubble sort algorithm
def bubble_sort(scores, numbers):
    swapped = True # Set swapped variable to True to begin the loop

    while swapped: 
        swapped = False 
        for i in range(0, len(scores)-1): # Loop from 0 to the length of scores minus one  
            if scores[i] < scores[i+1]: # We compare if the score at given index is less than the next score
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

number_of_scores = len(scores)
solution_numbers = list(range(number_of_scores))
bubble_sort(scores, solution_numbers)

print("Top Bubble Solutions")
for i in range(5):
    print(str(i+1) + ")",
          "Bubble solution #" + str(solution_numbers[i]), "score:", scores[i])
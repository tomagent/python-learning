# Define function to make a bubble sort algorithm with two parameters (scores and the indexes)
def bubble_sort(scores, numbers):
    swapped = True # Set swapped variable to True to begin the loop

    while swapped: 
        swapped = False 
        for i in range(0, len(scores)-1): # Loop from 0 to the length of scores minus one  
            if scores[i] < scores[i+1]: # We compare if the score at given index is less than the next score, then modify the lists
                temp = scores[i]
                scores[i] = scores[i+1]
                scores[i+1] = temp
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp
                swapped = True

scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

number_of_scores = len(scores) # Get length of scores
solution_numbers = list(range(number_of_scores)) # Make a list from 0 to 35
bubble_sort(scores, solution_numbers) # Pass the scores and the solution list to the function

print("Top Bubble Solutions")
for i in range(5): # Loop 5 times to get the top 5 scores with its index
    print(str(i+1) + ")",
          "Bubble solution #" + str(solution_numbers[i]), "score:", scores[i])
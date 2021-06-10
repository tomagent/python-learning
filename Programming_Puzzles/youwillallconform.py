def pleaseConform(caps):
    # Initialize start, forward and backward to 0
    start = forward = backward = 0
    # List of 3-tuple intervals
    intervals = []
    print("\nWelcome to the show :) \n")
    # Iterate through all caps starting at one
    for i in range(1, len(caps)):
        # Compare if the start (initially 0) is different than i (initially 1):
        if caps[start] != caps[i]:
            # We have another interval since the next cap is different (start, end, type of cap)
            intervals.append((start, i-1, caps[start]))
            # Count forwards and backwards
            if caps[start] == "F":
                forward += 1
            else:
                backward += 1
            # Set the end of the previous interval to the new one
            start = i
    # Add last interval
    intervals.append((start, len(caps)-1, caps[start]))
    # Count forward and backward of the last
    if caps[start] == "F":
        forward += 1
    else:
        backward += 1
    # The minority need to flip their cap
    if forward < backward:
        flip = "F"
    else:
        flip = "B"
    # Message to the minority that needs to flip the cap
    for t in intervals:
        # Access type of style cap
        if t[2] == flip:
            print(f"People in positions {t[0]} through {t[1]} flip your caps!")

if __name__ == "__main__":
    cap1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    pleaseConform(cap1)
    pleaseConform(cap2)

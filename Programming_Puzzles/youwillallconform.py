def pleaseConform(caps):
    # Initialize
    start = forward = backward = 0
    intervals = []
    caps = caps + ["END"]

    #Determine intervals where caps are on in the same direction
    for i in range(1, len(caps)):
        if caps[i-1] == "H":
            start = i

        if caps[start] != caps[i]:
            # each interval is a tuple with 3 elements (start, end, type)
            intervals.append((start, i - 1, caps[start]))
            
            if caps[start] == 'F':
                forward += 1
            else:
                backward += 1
            start = i

    # The minority need to flip their cap
    if forward < backward:
        flip = 'F'
    else:
        flip = 'B'

    # Message to the minority that needs to flip the cap
    for t in intervals:
        if t[2] == flip:
            if t[0] == t[1]:
                print(f"Person in position {t[0]} flip your cap!")
            else:
                print ('People in positions', t[0],
                   'through', t[1], 'flip your caps!')

if __name__ == "__main__":
    cap1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    cap3 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
    pleaseConform(cap3)


def pleaseConformOnepass(caps):
    # Ensure last interval is printed in case last element is different than the first
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        # New interval
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i-1, "flip your caps!")

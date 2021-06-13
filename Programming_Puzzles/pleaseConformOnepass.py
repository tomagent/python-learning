def pleaseConformOnepass(caps):
    # Ensure last interval is printed in case last element is different than the first
    caps = caps + [caps[0]]
    for i in range(1, len(caps)):
        if caps[i] != caps[i-1]:
            if caps[i] != caps[0]:
                start = i
            else:
                if start == i-1:
                    print(f"Person at position {start} please flip your cap!")
                else:
                    print(f"People in positions {start} through {i-1} flip your cap! ")

if __name__ == "__main__":
    cap1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    cap2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    pleaseConformOnepass(cap1)

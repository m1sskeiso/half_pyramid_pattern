# Print a downward half-pyramid pattern of stars
rows = 10

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()


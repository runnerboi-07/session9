fp = open("text.txt", "r") # r (=read) is by default, so not really needed; w = write
print(fp.read()) # prints the entire content of the file
fp.close() # good practice to close the file

# same exact thing w/ context manager
with open("text.txt", "r") as fp:
    print(fp.read())

# let's read from the same file --> line by line
print("Read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp: # we iterate over the file line by line
        print(f"{line_number}: {line}", end = "") # ask print not to add a new line
        # print(line.rstrip())
        line_number += 1
print("Done with the code")
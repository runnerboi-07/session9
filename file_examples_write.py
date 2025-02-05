# let's create a virtual diary
with open("diary.txt", "a") as fp: # a - append; add to this file or create it if it doesn't exist
    while True:
        text = input("How do you feel today? (types q to quit): ")
        if text == "q":
            break
        fp.write(f"{text}\n") # this is the same as the line below
        # fp.write(text + "\n")


# finally: keyword can be as useful as oxygen sometimes

try:
    f = open("text.txt")
    try:
        f.write("Thank you.")
    except:
        print("Couldn't perform write operation")
    else:
        print("Written to the file successfully")
    finally:
        f.close()  # if anything goes wrong, we can still rul finally and close file.
except:
    print("Couldn't open file")


f = open("newFile1", "x")  # - Create - will create a file, returns an error if the file exist
f.close()
f = open("newFile2", "a")  # - Append - will create a file if the specified file does not exist
f.close()
f = open("newFile3", "w")  # - Write - will create a file if the specified file does not exist
f.close()

# to delete a file, a module named os have to be imported
import os

os.remove("newFile1")  # removes specified file
os.rmdir("an empty folder")  # removes specified folder
# note: removes only if the folder is empty, and throws error if folder doesn't exist


# to avoid an error, check the file if it exists before attempting to delete it.
if os.path.exists("newFile2"):
    print("yes the File exists, i am deleting it.")
    os.remove("newFile2")
    print("done! the File was deleted successfully")
else:
    print("the file doesn't exist.")

# similarly
if os.path.exists("newFile3"):
    print("yes the File exists, i am deleting it it.")
    os.remove("newFile3")
    print("done! the File was deleted successfully")
else:
    print("the file doesn't exist.")

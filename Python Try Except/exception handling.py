# print(x)
# this will raise an error and program will crash


# even this will raise an error but won't crash the program because except handle the exception
try:
    print(x)
except NameError:
    print("NameError has occurred")
except:
    print("unknown exception occurred")
    # to handle many errors
else:
    print("no errors encountered")
    # also, we can add else block to ensure everything is fine,
finally:
    print("i don't care about errors. i always get executed")
    # unlike else block,The finally block,
    # if specified, will be executed regardless if the try block raises an error or not.

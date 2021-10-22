# re-naming a module
import MyModule as MyMod

x = MyMod.myDict["name"]
print(x)

# built-in modules
import platform

y = platform.system()
print(y)

# use of dir() function is to list all the function names (or variable names) in a module

z = dir(MyMod)
# Note: The dir() function can be used on all modules, also the ones you create yourself.
print(z)

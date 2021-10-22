import json

emp = {
    "name": "HariOm",
    "age": "23",
    "Software Engineer": True,
    "married": False,
    "parents": ("Ram", "Sita"),
    "girlfriend": None,
    "friends": ("Md", "Arjun", "Shankar"),
    "gadgets": {
        "phone": "Vivo",
        "release_year": "2014"
    },
    "favorites": ["apple", "bike", "cricket"]
}
print(json.dumps(emp))
# this gives some messy output

# indent parameter to define the numbers of indents:
print(json.dumps(emp, indent=4))

# parameter to change the default separator(which is (", ", ": "))
# with the one that is given below((". ", "= ")):
print(json.dumps(emp, indent=4, separators=(".", "=")))

# Order the result with sort keyword
print(json.dumps(emp, indent=4, sort_keys=True))

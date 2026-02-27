#exercise 1: Create a list of parables and sort them.

Parables = [ "The talents", "The lost coins", "The ten virgins", "The lost sheep","The good samaritan" ] 

Parables.sort()

print("Parables:")
for parable in Parables:
    print(parable)


#exercise 2:  Use a dict to map apostles to their roles.

Apostles = { "John": "the beloved", "Peter": "the rock and leader","Matthew": "tax collector and writter", "Andrew": "the first called"}

print("Apostles and their roles:")
for apostle, roles in Apostles.items():
   print(f"{apostle}: {roles}")
disciples = ["Peter", "John", "Mary", "Paul"]

# If/else example
for disciple in disciples:
    if disciple == "Paul":
        print(f"{disciple} is an apostle!")
    else:
        print(f"Hello, {disciple}!")

# While loop example
commandments = ["Honor God", "Love thy neighbor", "Do not steal"]
i = 0
while i < len(commandments):
    print(f"Commandment {i+1}: {commandments[i]}")
    i += 1
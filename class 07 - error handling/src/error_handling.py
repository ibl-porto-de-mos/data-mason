try:
    disciples = ["Peter", "John"]
    print(disciples[2])  # IndexError
except IndexError:
    print("Temptation avoided: Stay within bounds!")
finally:
    print("Always pray for guidance.")
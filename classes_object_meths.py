from classes_imported import Bio

miss_piggy = Bio("Piggy", "Miss", "Peepants", 4)

print(miss_piggy.__doc__)
print(miss_piggy.__dict__)


del miss_piggy.age

print(miss_piggy.__dict__)

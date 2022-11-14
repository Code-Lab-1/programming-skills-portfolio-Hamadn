# Assigning a variable(invite) to the list
invite = ["Faham", "Zoraiz", "Raheem", "Khalid", "Imran", "Hamza"]

# Capitalizing the first letter of every item in the list
# Printing a message using concatenation of index and string for every item
invited = invite[0].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[1].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[2].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[3].title()
print(f"{invited}, you are invited to the dinner.")


invited = invite[5].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[4].title()
print(f"\nSorry, {invited} can't make it to the dinner.")

# Removing the 5 item in the list and inserting a new item called 'Hamad' instead
del(invite[4])
invite.insert(4, 'Hamad')

# Printing the list and messages again
invited = invite[0].title()
print(f"\n{invited}, you are invited to the dinner.")

invited = invite[1].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[2].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[3].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[4].title()
print(f"{invited}, you are invited to the dinner.")

invited = invite[5].title()
print(f"{invited}, you are invited to the dinner.")

invite = ["Faham", "Zoraiz", "Raheem", "Khalid", "Imran", "Hamza"]

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

del(invite[4])
invite.insert(4, 'Hamad')

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

print("\nSorry, only two people can be invited.")

invited = invite.pop()
print(f"Sorry, {invited.title()} there's no space.")
invited = invite.pop()
print(f"Sorry, {invited.title()} there's no space.")
invited = invite.pop()
print(f"Sorry, {invited.title()} there's no space.")
invited = invite.pop()
print(f"Sorry, {invited.title()} there's no space.")

invited = invite[0].title()
print(f"{invited}, you are invited to the dinner.")
invited = invite[1].title()
print(f"{invited}, you are invited to the dinner.")

del(invite[0])
del(invite[0])

print(invite)
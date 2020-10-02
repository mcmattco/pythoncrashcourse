guests = ['Adam', 'Derek', 'Spencer', 'Kyle']
print("Please come to dinner " + guests[0] + ".")
print("Please come to dinner " + guests[1] + ".")
print("Please come to dinner " + guests[2] + ".")
print("Please come to dinner " + guests[3] + ".")
print("\n")

declined = guests.pop(3)
print(declined + " can't make it :(")
guests.append('Matt')
print("Please come to dinner " + guests[3] + ".")

print("\nWe found a bigger table and can invite three more dudes")
guests.insert(0,'Steve')
guests.insert(2,'Tom')
guests.append('Brian')
print("New guest list:")
print(guests)
print("Please come to dinner " + guests[0] + ".")
print("Please come to dinner " + guests[2] + ".")
print("Please come to dinner " + guests[-1] + ".")

print("\nOops jk, only room for two dudes")
uninvited = guests.pop(1)
print("Sorry " + uninvited + ", band guys only")
#etc

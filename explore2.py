words = "Animalia,Plantae,Fungi,Protista,Archaea,Bacteria"
kingdoms = words.split(",")

print("---sorted() *does not* change the list---")
print("\nusing sorted():", sorted(kingdoms))
print("\nsorted() with reverse", sorted(kingdoms, reverse=True))
print("\nsee, no change:", kingdoms)





print("\n\n---.sort() DOES change the list---")
kingdoms.sort()
print("\n\nusing .sort():", kingdoms)

kingdoms.sort(reverse=True)
print("\nusing .sort() with reverse:", kingdoms)
print("\nnote, it DID change the list")








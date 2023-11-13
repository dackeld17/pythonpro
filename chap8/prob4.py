import pickle
import shelve

print("Pickling lists.")
print("\nUnplicking lists.")

variety = ["Sweet", "Spicy", "Dill"]
shape = ["whole", "spear", "chip"]
brand = ["Claussen", "Heinz", "Vlassic"]

pickle_file = open("pickles1.dat", "wb")

pickle.dump(variety, pickle_file)
pickle.dump(shape, pickle_file)
pickle.dump(brand, pickle_file)

pickle_file.close()

pickle_file = open("pickles1.dat", "rb")

variety = pickle.load(pickle_file)
shape = pickle.load(pickle_file)
brand = pickle.load(pickle_file)

print( variety)
print( shape)
print( brand)

pickle_file.close()

print("\nShelving lists.")

pickles = shelve.open("pickles2.dat")
pickles["variety"] = ["sweet", "hot", "dill"]
pickles["shape"] = ["whole", "spear", "chip"]
pickles["brand"] = ["Claussen", "Heinz", "Vlassic"]
pickles.sync()
pickles.close()

pickles = shelve.open("pickles2.dat")

print("\nRetrieving the lists from a shelved file:")
for key in pickles.keys():
    print(key, "-", pickles[key])

pickles.close()

input("\n\nPress the enter key to exit.")


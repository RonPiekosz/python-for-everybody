fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File can't be opened:", fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

# we are going to be doing this pattern a lot
# this is Historgram pattern, which results in a set of frequencies
# after reading in a file
# using the get() method returns the (frequency) value for the key (word)
# and rather than resulting in a Traceback when attempting to get the value
# for a key that is not a member of the collection,
# we can set the default value to zero then increment by 1
# and when we encounted a word that we've seen before, it simply gets the value,
# increments it, then puts the value back in to the key counts[word]
# key: word
# value: defaults to zero, increments by one each time that the word is seen

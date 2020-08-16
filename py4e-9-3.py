fname = input("Enter the file name: ")
try:
    fhand = open(fname, 'r')
except:
    print("File cannot be opened:", fname)
    exit()

emails = dict()
for line in fhand:
    if line.startswith("From "):
        line = line.split()
        email = line[1]
        emails[email] = emails.get(email, 0) + 1

print(emails)

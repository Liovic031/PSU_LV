datoteka = open("C:\\Users\\student\\Documents\\miki\\lv1\\6z\\SMSSpamCollection.txt", 'r')

br_ham = 0
br_spam = 0
suma_ham = 0
suma_spam = 0
usklicnici = 0

for line in datoteka:
    line = line.rsplit()
    if line[0] == "ham":
        br_ham += 1
        suma_ham += len(line)
    elif line[0] == "spam":
        br_spam += 1
        suma_spam += len(line)
        if "!" in line[-1]:
            usklicnici += 1

print('Prosjecan broj rijeci u ham-u: ', suma_ham/br_ham)
print('Prosjecan broj rijeci u spam-u: ', suma_spam/br_spam)
print('SMS poruke s usklicnikom: ', usklicnici)
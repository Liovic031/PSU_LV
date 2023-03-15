datoteka = open("C:\\Users\\student\\Documents\\student1\\lv1\\5z\\song.txt", 'r')

rijecnik = {}

for line in datoteka:
    words = line.rsplit()

    for word in words:
        if word in rijecnik:
            rijecnik[word] += 1
        else:
            rijecnik[word] = 1

unique_words = []

for word in rijecnik:
    if rijecnik[word] == 1:
        unique_words.append(word)

print(rijecnik)

print("Unikatne rijeci: ", len(unique_words))
print(unique_words)

ime_datoteke = input()
directory = "C:\\Users\\student\\Documents\\student1\\lv1\\4z\\" + ime_datoteke
datoteka = open(directory, 'r')
suma = 0
br = 0

for line in datoteka:
    line = line.rsplit()
    if "X-DSPAM-Confidence:" in line:
        br += 1
        suma += float(line[1])

print("Average X-DSPAM-Confidence:", suma/br)

datoteka.close()

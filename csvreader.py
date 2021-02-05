import csv

with open('utilities/loanapp.csv') as csvReader:
    reader = csv.reader(csvReader, delimiter=',')
    names = []
    stats = []

    for row in reader:
        names.append(row[0])
        stats.append(row[1])
print(names)
print(stats)
counter = 0
for name in names:
    if name == 'Vishnu':
        print(stats[counter])
        break
    else:
        counter = counter + 1
with open('utilities/loanapp.csv', 'a') as writer:
    write = csv.writer(writer)
    write.writerow(['Sanjay', 'Rejected'])
    writer.close()

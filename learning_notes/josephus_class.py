
import person
import josephus
import reader

person_list = []

txt_read = reader.TXTReader("josephus_list2.txt")
txt_ring = txt_read.read()
for i in txt_ring:
    person_list.append(i)
#print(person_list)

csv_read = reader.CSVReader("josephus_list1.csv")
csv_ring = csv_read.read()
for i in csv_ring:
    person_list.append(i)
#print(person_list)

zip_read = reader.ZIPReader("josephus.zip")
zip_ring = zip_read.read()
for i in zip_ring:
    person_list.append(i)

people = josephus.create_ring(person_list)

STEP = 2
START = 3
josephus_ring = josephus.Josephus(START, STEP, people)

for PEOPLE in josephus_ring:
    print(PEOPLE)
#print(RING.start)
print(josephus_ring.pop())

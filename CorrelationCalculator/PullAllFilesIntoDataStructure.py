import os,glob
import csv
folder_path = "..\\tickerData"
count = 1
dict = {}
set = set()
fieldnames = []
fieldnames.append("Date")
for filename in glob.glob(os.path.join(folder_path, 'USA*.txt')):
  with open(filename, 'r') as f:
    # print(count)
    text = f.read()
    filename = filename.replace(folder_path + "\\","")
    filename = filename.replace(".txt","")
    #print (len(text))
    lines = text.splitlines()
    for line in lines:
        val = line.split(',')
        date = val[0]
        if(date != "DATE" and int(date) > 20010000):
            # print(date)
            value = val[1]
            if date in dict:
                list = dict.get(date)
                list[count] = value
            else:
                set.add(date)
                list = [None] * 54
                list2 = [date]
                list2.extend(list)
                list2[count] = value
                # print("the length is " ,len(list2))
                dict[date] = list2
    count = count + 1
    fieldnames.append(filename)

# for key in dict.keys():
#     print(key)
#     print(dict[key])

listK = sorted(set)
print(listK)

arrayS = []

for item in listK:
    arrayS.append(dict[item])

print("the csv is being made")

with open('data3.csv', 'w', newline='') as csvfile:
    a = range(55)
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    writer.writerow(fieldnames)

    for item in listK:
        writer.writerow(dict[item])

# with open('data2.csv', 'w') as csvfile:
#     a = range(55)
#     writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     for item in listK:
#         writer.writerow(dict[item])





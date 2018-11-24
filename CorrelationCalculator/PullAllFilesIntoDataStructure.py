import os,glob
folder_path = "C:\\Users\\cfee\\git\\trading\\tickerData"
count = 0
dict = {}
for filename in glob.glob(os.path.join(folder_path, 'USA*.txt')):
  with open(filename, 'r') as f:
    print(count)
    text = f.read()
    print (filename)
    print (len(text))
    lines = text.splitlines()
    for line in lines:
        val = line.split(',')
        date = val[0]
        if(date != "DATE" and int(date) > 20010000):
            print(date)
            value = val[1]
            if date in dict:
                list = dict.get(date)
                list[count] = value
            else:
                list = [None] * 54
                list[count] = value
                dict[date] = list
    count = count + 1

for key in dict.keys():
    print(key)
    print(dict[key])
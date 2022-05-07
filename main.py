import csv
import re

with open('dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    i = 0
    n = 0
    for line in reader:
        line = ''.join(line)
        y = line.split('\t')
        y = y[5:]   # reads a string and gets the sixth row
        for row in y:
            x = row.split(';')
            j = []

            for i in x:
                j.append(i.strip())

            numbers = []
            emails = []
            sites = []
            for i in j:
                i = i.replace(' ', '')
                if re.search("([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})", i) is not None:
                    emails.append(i)
                    continue
                elif '.' in i and 'o' in i:  # it should be as "elif '.' in i and ('o' not in i):" but it doesn't work
                    sites.append(i)
                    continue
                i = i.replace('(', '').replace(')', '').replace('-', '').replace('+', '').replace(',', '')
                length = len(i)
                try:
                    if type(int(i)) == int:
                        if length == 12:
                            numbers.append(i)
                        elif length == 9:
                            numbers.append(int('380' + str(i)))
                        elif length == 10:
                            numbers.append(int('38' + str(i)))
                        elif length == 11:
                            numbers.append(int('3' + str(i)))
                except ValueError:
                    continue

            final_list = list(numbers + emails + sites)
            if len(final_list) == 0:
                continue
            else:
                with open('new_file.csv', 'a', encoding='utf-8', newline='') as file2:
                    writer = csv.writer(file2)   # write down all the data from final_list
                    writer.writerow(final_list)
                    n += 1
                    print(n)


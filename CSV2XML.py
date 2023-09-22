from bs4 import BeautifulSoup
import csv
import time
import os
Loc = os.path.dirname(os.path.abspath(__file__))

start = time.time()
count = 0
edited = 0

filenames = os.listdir(Loc + "/old")
for filename in filenames:
    with open("old/"+filename, encoding='utf-8') as raw_resuls:
        results = BeautifulSoup(raw_resuls, 'xml')

    for txt in results.find_all("entry"):
        fl = False
        # translatedfile = filename.replace(".xml",".csv")
        translatedfile = "all.csv"
        g = open("translate/"+translatedfile, encoding='utf-8')
        csv_reader2 = csv.reader(g)
        for i in csv_reader2:
            if i[0] == txt['name'] and i[2] != "":
                txt.string = i[2]
                print(str(count)+'_'+txt['name']+": แก้ไขแล้ว")
                fl = True
                edited += 1
                count += 1
                break
        if fl != True:
            print(str(count)+'_'+txt['name']+": ข้าม")
            fl = False
            count += 1
    with open("new/"+filename, "w", encoding='utf-8') as outfile:
        outfile.write(str(results).replace('<?xml version="1.0" encoding="utf-8"?>\n',''))

end = time.time()
percentage = "{:.2f}".format(edited*100/count)
print('ทั้งหมด: '+str(edited)+'/'+str(count)+'('+percentage+'%)')
restime = end - start
if restime >= 60:
    restime = restime/60
    unit = ' นาที'
else:
    unit = ' วินาที'
totaltime = "{:.2f}".format(restime)
print('ใช้เวลาไป: ' + str(totaltime) + unit)

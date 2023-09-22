# from bs4 import BeautifulSoup
# import csv
# import time
# import os
# Loc = os.path.dirname(os.path.abspath(__file__))

# start = time.time()
# count = 0

# filenames = os.listdir(Loc + "/old")
# for filename in filenames:
#     allitems = []
#     filename = filename.replace('.xml','')
#     print(filename)
#     with open('old/'+filename+'.xml', encoding='utf-8') as raw_resuls:
#         results = BeautifulSoup(raw_resuls, 'xml')
#     checkItem = []
#     fl = ""
#     for txt in results.find_all("entry"):
#         print(txt['name']+" : "+txt.getText())
#         allitems.append([txt['name'], txt.getText(), ""])


#     with open('translate/'+filename+'.csv', 'w', encoding='utf8', newline='') as f:
#         write = csv.writer(f)
#         write.writerow(["ID", "EN", "TH"])
#         write.writerows(allitems)
from bs4 import BeautifulSoup
import csv
import time
import os
Loc = os.path.dirname(os.path.abspath(__file__))

start = time.time()
count = 0

filenames = os.listdir(Loc + "/old")
allitems = []
for filename in filenames:
    filename = filename.replace('.xml','')
    print(filename)
    with open('old/'+filename+'.xml', encoding='utf-8') as raw_resuls:
        results = BeautifulSoup(raw_resuls, 'xml')
    checkItem = []
    fl = ""
    for txt in results.find_all("entry"):
        print(txt['name']+" : "+txt.getText())
        allitems.append([txt['name'], txt.getText(), ""])


with open('translate/all.csv', 'w', encoding='utf8', newline='') as f:
    write = csv.writer(f)
    write.writerow(["ID", "EN", "TH"])
    write.writerows(allitems)

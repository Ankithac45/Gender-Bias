import csv

inputfile = csv.reader(open('hash.csv','r',encoding='utf-8'))

i=0


for row in inputfile:
    if (i > 0 and i < i+1):	
        place = row[3].replace(' ,',',')
        print(place)
        open('placelist'+str(i)+'.txt','w').write(place+'\n')
    i+=1
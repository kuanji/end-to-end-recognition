lines = open("data/B-59.850.lst", 'r').read().splitlines()
list10 = open("data/B-59.850_10.lst", 'w')
list20 = open("data/B-59.850_20.lst", 'w')
list30 = open("data/B-59.850_30.lst", 'w')
list40 = open("data/B-59.850_40.lst", 'w')
list50 = open("data/B-59.850_50.lst", 'w')
list60 = open("data/B-59.850_60.lst", 'w')
list70 = open("data/B-59.850_70.lst", 'w')
list80 = open("data/B-59.850_80.lst", 'w')
list90 = open("data/B-59.850_90.lst", 'w')
list100 = open("data/B-59.850_100.lst", 'w')

for idx, line in enumerate(lines):
    if(idx < 10):
        list10.write(line + '\n')
        list20.write(line + '\n')
        list30.write(line + '\n')
        list40.write(line + '\n')
        list50.write(line + '\n')
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 20):
        list20.write(line + '\n')
        list30.write(line + '\n')
        list40.write(line + '\n')
        list50.write(line + '\n')
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 30):
        list30.write(line + '\n')
        list40.write(line + '\n')
        list50.write(line + '\n')
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 40):
        list40.write(line + '\n')
        list50.write(line + '\n')
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 50):
        list50.write(line + '\n')
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 60):
        list60.write(line + '\n')
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 70):
        list70.write(line + '\n')
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 80):
        list80.write(line + '\n')
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 90):
        list90.write(line + '\n')
        list100.write(line + '\n')
    elif(idx < 100):
        list100.write(line + '\n')
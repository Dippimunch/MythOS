import re


text = open('features.txt', 'r')
lines = text.readlines()
clean_txt = []

#print(lines[1])
for l in range(len(lines)):
    new_clean = re.sub(',\d+,,', '', lines[l])
    clean_txt.append(new_clean)
    print(clean_txt[l])
    #print(l)
    #print(lines[l])
    
#print(lines)

import re


text = open('features.txt', 'r')
lines = text.readlines()
clean_txt = []
clean_txt_2 = []
clean_txt_3 = []

for l in range(len(lines)):
    new_clean = re.sub(',\d+,,', '', lines[l])
    clean_txt.append(new_clean)

for l in range(len(lines)):
    new_clean = re.sub(',\D,\d+,\d+\\n$', '', clean_txt[l])
    clean_txt_2.append(new_clean)

for l in range(len(lines)):
    new_clean = re.sub(',{},,', ', ', clean_txt_2[l])
    clean_txt_3.append(new_clean)

print(clean_txt_3)

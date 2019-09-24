phrase = input ("What do you want to encrypt ? ")
phrase = phrase.upper()
shift = input ("What shift do you want from 1 to 25? ")
i=0
my_hash = dict({"A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9", "J":"10", "K":"11", "L":"12", "M":"13", "N":"14", "O":"15", "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20", "U":"21", "V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26", " ":"100"})
my_hash1 = dict({"1":"A", "2":"B", "3":"C", "4":"D", "5":"E", "6":"F", "7":"G", "8":"H", "9":"I", "10":"J", "11":"K", "12":"L", "13":"M", "14":"N", "15":"O", "16":"P", "17":"Q", "18":"R", "19":"S", "20":"T", "21":"U", "22":"V", "23":"W", "24":"X", "25":"Y", "26":"Z", "100":" "})
Character_list = list(phrase)
Number_list = []
for i in range(len(Character_list)):
    x = int(my_hash.get(Character_list[i]))
    if x > 99:
        Number_list.append(x)
    else:
        shift=int(shift)
        x=x+shift
        if x > 26:
            x=x-26
        Number_list.append(x)
Shifted_Character_list = []
j=0

for j in range(len(Number_list)):
    y = (my_hash1.get(str(Number_list[j])))
    Shifted_Character_list.append(y)
Final_string = ''.join(Shifted_Character_list)
print ("Your encrypted code is : " + Final_string)




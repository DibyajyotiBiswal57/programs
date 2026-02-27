roman = list(str(input("Enter a Roman number between 1 and 3999 (I-MMMCMXCIX)\n")).upper())
for i in range(3):
    roman.append("")
integer = 0
i=0


i_set=i
if roman[i_set]=="M":
    if roman[i_set+1]=="M":
        if roman[i_set+2]=="M":
            integer+=3000
            i+=3
        else:
            integer+=2000
            i+=2
    else:
        integer+=1000
        i+=1



i_set=i
if roman[i_set]=="C":
    if roman[i_set+1] == "M":
        integer+=900
        i+=2
    elif roman[i_set+1]=="D":
        integer+=400
        i+=2
    elif roman[i_set+1] == "C":
        if roman[i_set+2] == "C":
            integer+=300
            i+=3
        else:
            integer+=200
            i+=2
    else:
        integer+=100
        i+=1
if roman[i_set]=="D":
    if roman[i_set+1]=="C":
        if roman[i_set+2]=="C":
            if roman[i_set+3]=="C":
                integer+=800
                i+=4
            else:
                integer+=700
                i+=3
        else:
            integer+=600
            i+=2
    else:
        integer+=500
        i+=1


i_set=i
if roman[i_set]=="X":
    if roman[i_set+1] == "C":
        integer+=90
        i+=2
    elif roman[i_set+1]=="L":
        integer+=40
        i+=2
    elif roman[i_set+1] == "X":
        if roman[i_set+2] == "X":
            integer+=30
            i+=3
        else:
            integer+=20
            i+=2
    else:
        integer+=10
        i+=1
if roman[i_set]=="L":
    if roman[i_set+1]=="X":
        if roman[i_set+2]=="X":
            if roman[i_set+3]=="X":
                integer+=80
                i+=4
            else:
                integer+=70
                i+=3
        else:
            integer+=60
            i+=2
    else:
        integer+=50
        i+=1

i_set=i
if roman[i_set]=="I":
    if roman[i_set+1] == "X":
        integer+=9
        i+=2
    elif roman[i_set+1]=="V":
        integer+=4
        i+=2
    elif roman[i_set+1] == "I":
        if roman[i_set+2] == "I":
            integer+=3
            i+=3
        else:
            integer+=2
            i+=2
    else:
        integer+=1
        i+=1
if roman[i_set]=="V":
    if roman[i_set+1]=="I":
        if roman[i_set+2]=="I":
            if roman[i_set+3]=="I":
                integer+=8
                i+=4
            else:
                integer+=7
                i+=3
        else:
            integer+=6
            i+=2
    else:
        integer+=5
        i+=1


string =""
for i in range(len(roman)-3):
    string+=roman[i]
print("")
print (f"Roman Numerals: \t{string}")
print (f"Hindu-Arabic Numerals: \t{integer}")
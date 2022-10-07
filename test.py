

f = open("test.txt","r")


total = 0
antall = 0
for count,value in enumerate(f.readline().split("	")):

    if int(value) >0:
        print("hei ", antall)
        total += int(value)*int(count)
        antall +=1


print("gjennomsnitt ", total/antall)
print("gjennomsnitt2 ", total/91)






getOpen = open("txt/metin.txt", 'r')
for dataShow in getOpen:
    print(dataShow)
getOpen.close()
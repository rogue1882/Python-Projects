

fileList = ['information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt',\
                'data.pdf', 'myPhoto.jpg']

i = [1,4]
element = []
for index in i:
    element.append(fileList[index])
    print(element)

    
print(len(fileList))
i = 0
while i < len(fileList):
      print(fileList[i])
      i = i + 1


for i in enumerate(fileList):
    print(i)


newfileList= [a for a in fileList if "txt" in a]
print(newfileList)

    
    
        



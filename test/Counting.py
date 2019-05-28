urls = [
"http://www.google.com/a.txt",
"http://www.google.com.tw/a.txt",
"http://www.google.com/download/c.jpg",
"http://www.google.co.jp/a.txt",
"http://www.google.com/b.txt",
"https://facebook.com/movie/b.txt",
"http://yahoo.com/123/000/c.jpg",
"http://gliacloud.com/haha.png",
]


count = [0,0,0]
filenames = ["a.txt","b.txt","c.jpg"]

for filename in urls:
  for i in range(3):
    if(filename[-5:]==filenames[i]):
      count[i]+=1  
      
print(filenames[0]+" "+str(count[0]))
print(filenames[1]+" "+str(count[1]))
print(filenames[2]+" "+str(count[2]))
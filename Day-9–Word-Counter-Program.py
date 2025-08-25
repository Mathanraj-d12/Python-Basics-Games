sentence=input("Enter a sentence:")

words=sentence.split()

wordCount={}
for word in words:
    word.lower()
    if word in wordCount:
        wordCount[word]+=1
    else:
        wordCount[word]=1

print("\nWord Count:")
for word,count in wordCount.items():
    print(word,":",count)
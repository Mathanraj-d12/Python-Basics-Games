sentence=input("Enter a sentence:")

words=sentence.split()
reversed_words = [word[::-1] for word in words]
output=" ".join(reversed_words)
print(output)




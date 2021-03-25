vowels = ['a','e','i','o','u']
tmp=[]
word=input("enter:")
for letter in word:
    if letter in vowels:
        if letter not in tmp:
            tmp.append(letter)
  
print(tmp)            
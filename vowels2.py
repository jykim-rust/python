vowels = ['a','e','i','o','u']
tmp={}
word=input("enter:")
for letter in word:
    if letter in vowels:
        tmp.setdefault(letter,0)    
        tmp[letter]+=1
       
for a,b in sorted(tmp.items()):
    print(a,':',b)
  
         
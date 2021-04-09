def search4vowels(word:str)->bool:
    '''annotation is selective it doesn't work'''
    vowels=set('aeiou')
#    word=input('input something:')
    found=vowels.intersection(set(word))
#    for vowel in found:
#        print(vowel)
    if len(found)==0:
        return False
    else:
        return True
# or can use bool(vowels.intersection(set(word))) instead if phrase

def search4letters(phrase:str,letters:str='aeiou')->set:
    return set(phrase).intersection(set(letters))
#main function


        
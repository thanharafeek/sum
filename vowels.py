vowels_and_constents=['a','e','i','u','o','r','t','A','U','y','k']
vowels=['A','E','I','O','U']
vowels_list=[]
constents_list=[]
for i in vowels_and_constents:
    i=i.upper()
    if i in vowels:
        vowels_list.append(i)
    else:
        constents_list.append(i)
print(vowels_list)
print(constents_list)
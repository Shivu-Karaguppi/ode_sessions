# str = '',"", ''' '''
# print(''' ojois
#       kijnjinijn
#       kniij ''')

# print("shiva\n is \n teaching \n python")

#immutable

# a = 'Pya[0] = 'S'thon'

# word = "Python"
# print(word[-1])

#slicing 
# txt = "Hello world"
# print(txt[0:12])

# for t in txt[0:15]:
#     print(t)


# print("Ha"*3)

# not / in 
# wo = "python"
# print('x' in wo)
txt = "hello World. Jocker"
# print(txt.find('o'))

# lower(),upper(),title(),capitalize()
# print(txt.capitalize())

## strip ***

# a = " Shivac       "
# print(">" + a.rstrip() + a.lstrip() )

#1 count(),find(), startswith(), endswith()
txt = "hello World . Jocker"
print(txt.endswith('er'))

# 2 replace
# print(txt.replace('o','x'))

# print(txt.split('.'))


### f""" """
def doc(f):
    # return f"My name is {f}"
    return "My name is {}".format(f)

print(doc("Anmol"))

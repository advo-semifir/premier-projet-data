import re

regex1 = re.compile(r'(\d+)-(\d+)-(\d+)')

texte = '2018-12-31'
validation = regex1.match(texte)

if validation:
    print(validation.groups())
else:
    print('Le format de la date n\'est pas valide')
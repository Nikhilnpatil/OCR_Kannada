
#Google translate library to translate kannada characters into english characters
from googletrans import Translator
text1="ಹ"
translator=Translator()
ans=translator.translate(text1,src='kn',dest='en')
print(ans.text)


#Dictionary mapping of character image classes into byte representation of UTF-8 code of Kannada vowels and consonants
#print(text1.encode("utf-8"))

dict1={0:b'\xe0\xb2\x85',1:b'\xe0\xb2\x86',2:b'\xe0\xb2\x87',3:b'\xe0\xb2\x88',4:b'\xe0\xb2\x89',5:b'\xe0\xb2\x8a',
       6:b'\xe0\xb2\x8b',8:b'\xe0\xb2\x8e',9:b'\xe0\xb2\x8f',10:b'\xe0\xb2\x90',11:b'\xe0\xb2\x92',12:b'\xe0\xb2\x93',
       13:b'\xe0\xb2\x94',14:b'\xe0\xb2\x85\xe0\xb2\x82',15:b'\xe0\xb2\x85\xe0\xb2\x83',
       16:b'\xe0\xb2\x95',17:b'\xe0\xb2\x96',18:b'\xe0\xb2\x97',19:b'\xe0\xb2\x98',20:b'\xe0\xb2\x99',
       21:b'\xe0\xb2\x9a',22:b'\xe0\xb2\x9b',23:b'\xe0\xb2\x9c',24:b'\xe0\xb2\x9d',25:b'\xe0\xb2\x9e',
       26:b'\xe0\xb2\x9f',27:b'\xe0\xb2\xa0',28:b'\xe0\xb2\xa1',29:b'\xe0\xb2\xa2',30:b'\xe0\xb2\xa3',
       31:b'\xe0\xb2\xa4',32:b'\xe0\xb2\xa5',33:b'\xe0\xb2\xa6',34:b'\xe0\xb2\xa7',35:b'\xe0\xb2\xa8',
       36:b'\xe0\xb2\xaa',37:b'\xe0\xb2\xab',38:b'\xe0\xb2\xac',39:b'\xe0\xb2\xad',40:b'\xe0\xb2\xae',
       41:b'\xe0\xb2\xaf',42:b'\xe0\xb2\xb0',43:b'\xe0\xb2\xb2',44:b'\xe0\xb2\xb3',45:b'\xe0\xb2\xb5',
       46:b'\xe0\xb2\xb6',47:b'\xe0\xb2\xb7',48:b'\xe0\xb2\xb8',49:b'\xe0\xb2\xb9'}

print(dict1[37].decode('utf-8'))
# for i in range(50):
#     if i!=7:
#         string_ans=dict1[i].decode('utf-8')
#         print(string_ans)
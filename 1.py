'''
map.html
'''

msg = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# 일반적인 코드
# result = ""
# for i in list(msg):
#     if i.isalpha():
#         result += chr((ord(i)+2-97)%26+97)
#     else:
#         result += i
# print(result)

result = ''.join(chr((ord(i)+2-97)%26+97) if i.isalpha() else i for i in 'map')
print(result)

# string.maketrans()와 translate()를 사용한 코드
# dec1 = "abcdefghijklmnopqrstuvwxyz"
# dec2 = "cdefghijklmnopqrstuvwxyzab"
# dec = msg.maketrans(dec1, dec2)
# print(msg.translate(dec))

'''
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
'''


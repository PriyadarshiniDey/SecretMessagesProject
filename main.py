alphabet= 'abcdefghijklmnopqrstuvwxyz'

key = 3

newmsg = ''

msg= input('enter your message')


for character in msg:

    if character in alphabet:

        position = alphabet.find(character)

        newposition = (position+key) % 26

        newcharacter= alphabet[newposition]

        newmsg +=newcharacter
    
else:
        
        newmsg +=character

print('Secret message:', newmsg)
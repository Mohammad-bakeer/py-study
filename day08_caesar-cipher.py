"""
edits to make code better 
1- make a list alphabet=[a,b,c,......,z]
2- shift_number %= 26 
3- combine encode and decode like this, and make it change only the character from the alphabet:
{
end_text = ""
if(dir==decode):
   shift_number*=-1
for char in start_text:
   if char in alphabet:
      position=alphabet.index(char)
      new_position=position+shift_number
      end_text += alphabet[new_position]
   else:
      end_text += char
}

"""
def caesar_cipher(op):
    #print("encode or decode ?")
    if(op=="encode"):
        message=input("type your message: \n")
        shift_var=int(input("type the shift number: \n"))
        en_message=""
        for letter in message:
            en_message+=chr(ord(letter)+shift_var)
        print(en_message)    

    elif(op=="decode"):
        message=input("type your message: \n")
        shift_var=int(input("type the shift number: \n"))
        de_message=""
        for letter in message:
            de_message+=chr(ord(letter)-shift_var)
        print(de_message)    
    else:
        print("you mush choose one of them (decode/encode)")

    re=input("type 'yes' to try again, 'no' to exit\n")
    if(re=="yes"):
        caesar_cipher(input("encode or decode ?"))
    elif(re=="no"):
        return
    else:
        print("follow instruction next time please!")
        return    


caesar_cipher(input("encode or decode ?"))
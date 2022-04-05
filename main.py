alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
def encrypt(userInput, shftAmt):
    # I had to move newMsg out of the for loop
    # because otherwise it would just generate one character
    # instead of adding each character in sequence
    newMsg = ''
    for letter in userInput:
        letPos = alphabet.index(letter)
        newPos = letPos + shftAmt
        newLet = alphabet[newPos]
        newMsg += newLet
    print(f"Your encoded message is {newMsg}")
# It's at this point that I'm going to veer off from
# the guided path.  It's obvious the next phase will be to
# set up Decryption and give the user the choice
# So I'm going to go ahead and attempt that on my own :)

def decrypt(userInput, shftAmt):
    decodedMsg = ''
    for letter in userInput:
        letPos = alphabet.index(letter)
        newPos = letPos - shftAmt
        newLet = alphabet[newPos]
        decodedMsg += newLet
    print(f"Your DEcoded message is {decodedMsg}")
decrypt(text, shift)
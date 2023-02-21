from resource import alphabet, logo

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction not in ['encode', 'decode']:
    print("Invalid direction...")
    break
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number in the range 1 to 25:\n"))
  if shift < 1 or shift > 25:
    print("Invalid shift number...")
    break

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'end' if you want to end the program.\n")
  if restart == "end":
    should_end = True
    print("Goodbye")
    



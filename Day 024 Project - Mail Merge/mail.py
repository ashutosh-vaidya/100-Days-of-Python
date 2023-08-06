PLACEHOLDER_NAME = "[name]"
PLACEHOLDER_DAY = "[day]"
PLACEHOLDER_TIME = "[time]"

DAY = "Sunday"
TIME = "7:30"

with open("Input\Guests\invitee_names.txt") as guests:
    guest_names = guests.readlines()
    #print(guest_names)

with open("Input\Letters\letter_template.txt") as template:
    letter_template = template.read()
    #print(letter_template)
    
    for guest in guest_names:
        name = guest.strip()
        letter = letter_template.replace(PLACEHOLDER_NAME, name).replace(PLACEHOLDER_DAY, DAY).replace(PLACEHOLDER_TIME, TIME)
        with open(f"Output\ReadyToSend\letter_for_{name}.txt", mode="w") as completed_letter:
            completed_letter.write(letter)
        
PLACEHOLDER = "[name]"

with open ("mail_file/input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("mail_file/input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        str_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, str_name)
        with open(f"mail_file/input/Letters/letter_for_{str_name}.txt", mode="w") as new_letters:
            new_letters.write(new_letter)
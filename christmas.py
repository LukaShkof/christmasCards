# read from employees
with open('employees.txt', 'r') as file:
    names = [line.strip() for line in file]
# read from template
with open('template.txt', 'r') as file:
    template = file.read()

# create a card
for name in names:
    # replace 'NAME'
    card_content = template.replace('NAME', name)

    # generate the filename
    filename = f'christmasCards/{name}.txt'

    # write the card to the file
    with open(filename, 'w') as file:
        file.write(card_content)

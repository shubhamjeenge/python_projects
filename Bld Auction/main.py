from art import logo
print(logo)

data = {}
def find_the_winner(data_dict):
    max_value = 0
    name = ""
    for key in data_dict:
        value = data_dict[key]
        if value> max_value:
            max_value = value
            name = key
    print(f"The winner is {name} with a bid ${max_value}")

over = False
while over != True:
    name = str(input("What is your name?:")).lower()
    bid = int(input("What is your bid?: $"))
    data[name] = bid
    options = str(input("Are there any other bidders? Type 'yes or 'no'.")).lower()
    if options == "no":
        over = True
        find_the_winner(data_dict=data)

    if options == "yes":
        print("\n"*20)







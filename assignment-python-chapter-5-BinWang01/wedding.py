# Bin Wang
# Follow the instructions for how to code this application
guest_list = []
while True:
    name = input("Enter a guest's name or type 'end' to stop.\n")
    if name.lower() == "end":
        break
    else:
        guest_list.append(name)
print(*guest_list, sep='\n')
num_of_guests = len(guest_list)
total_cost = num_of_guests * 12
print(
    f"You have invited {num_of_guests} guests at a cost of ${total_cost} for food.")

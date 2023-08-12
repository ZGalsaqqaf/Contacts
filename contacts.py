import json

from enum import Enum

class Choice(Enum):
    ADD = '1'
    VIEW = '2'
    DELETE = '3'
    UPDATE = '4'
    EXIT = '5'

Choice_values = [member.value for member in Choice]

# -------------------------------------------------------------
print('-' * 35, "\n\tYOUR CONTACT LIST")
print('-' * 35, "\n") 

# -------------------------------------------------------------
file_path = 'contacts.json'
user_choice =""
# -------------------------------------------------------------

def check_name_phone(name, phone):
    if not phone.isdigit():
        return f"Phone includes just numbers. ( {phone} ) is not a phone number! \nAgain please: \n"
    
    elif name.isdigit():
        return f"At least one letter included. ( {name} ) is not a name! \nAgain please: \n"
    else:
        return False
# -------------------------------------------------------------

def check_repeate(name, phone):
    with open(file_path, 'r') as getdata:
        data = json.load(getdata)

        for key, value in data.items():
            if name in value.values():
                if phone in value.values():
                    return "\nThis contact is already existed! \nAdd new please: \n"
                
                return f"\nThis name ( {name} ) is repeated! \nAgain please: \n"
            if phone in value.values():
                return f"\nThis phone number ( {phone} ) is repeated! \nAgain please: \n"
            
    return False
   
# ------------------------------------------------------------------------------------------
    
def add_data():
    name = input("Enter Name: ").strip().lower()
    phone = input("Enter Phone Number: ").strip()
    
    with open(file_path, 'r') as getdata:
        data = json.load(getdata)   # convert json to python

        if check_name_phone(name, phone):
            print(check_name_phone(name, phone))
            switch()

        elif check_repeate(name, phone):
            print(check_repeate(name, phone))
            switch()

        else:
            if len(data):
                # get the last id in the dict
                no = int(list(data)[-1]) + 1
                no = str(no)
            else:
                no = '1'

            dict_contact = {
                "id" : no, 
                "name" : name,
                "phone" : phone,
            }

            data[no] = dict_contact

            with open(file_path, 'w') as save:
                json.dump(data, save)   # python to json
                print("Successfully Added.\n")

# ---------------------------------------------------

def view_data():
    with open(file_path, 'r') as view:
        data = json.load(view)
        for key, value in data.items():
            for k, v in value.items():
                print(f"{k.title()}: ", end=" ")
                print(f"{v.title()}")
            print('\n')

# ---------------------------------------------------

def delete_data():
    id = input("Enter Contact id: ")

    with open(file_path, 'r') as getdata:
        data = json.load(getdata)

        if id in data:
            deleted_cont = data.pop(id) 

            with open(file_path, 'w') as delete:
                data_1 = json.dump(data, delete)
                print(f"{deleted_cont['name']} was deleted.\n")
        else:
            print("This Id is not exists!\n")

# ---------------------------------------------------

def update_data():
    view_data()

    id = input("Enter Contact id: ")

    with open(file_path, 'r') as getdata:
        data = json.load(getdata)

        if id in data:
            name = input("Enter Now Name: ").strip().lower()
            phone = input("Enter Now Phone: ").strip()

            if check_name_phone(name, phone):
                print(check_name_phone(name, phone))
                switch()

            elif check_repeate(name, phone):
                print(check_repeate(name, phone))
                switch()
            
            else:
                dic = {
                    "id" : id, 
                    "name" : name,
                    "phone" : phone,
                }
                data[id] = dic
                with open(file_path, 'w') as update:
                    json.dump(data, update)
                    print(f"Successfully Updated.\n")

# -------------------------------------------------------------------

def switch():
    if user_choice == Choice.ADD.value:
        add_data()
    elif user_choice == Choice.VIEW.value:
        view_data()
    elif user_choice == Choice.DELETE.value:
        delete_data()
    elif user_choice == Choice.UPDATE.value:
        update_data()
    else:
        print("Thank You ^^ \n\n")
        exit()

# ------------------------------------------------------------------------------------
# --------------------------**   START THE PROGRAM    **------------------------------
# ------------------------------------------------------------------------------------

while user_choice != Choice.EXIT.value:
    print("1. Add \n2. View \n3. Delete \n4. Update \n5. Exit\n")

    user_choice = input("\nEnter Choice: ").strip()
    print("\n")

    if user_choice in Choice_values:
        switch()

    else:
        print(f"XXX Error: Invalid choice, just digits from {Choice_values[0]} to {Choice_values[-1]} XXX.\n")

# ------------------------------------------------------------------------------------------

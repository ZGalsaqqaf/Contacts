import json

from enum import Enum

import os


class Choice(Enum):
    ADD = '1'
    VIEW = '2'
    DELETE = '3'
    UPDATE = '4'
    EXIT = '5'
# -------------------------------------------------------------

print('-' * 35, "\n\tYOUR CONTACT LIST")
print('-' * 35, "\n") 

# print("1. Add \n2. View \n3. Delete \n4. Update \n5. Exit\n")
# -------------------------------------------------------------

user_choice =""
# -------------------------------------------------------------

while user_choice != Choice.EXIT.value:
    print("1. Add \n2. View \n3. Delete \n4. Update \n5. Exit\n")

    user_choice = input("\nEnter Choice: ").strip()
    print("\n")
    def add_data():
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        # if number.isdigit():
        #     pass
        # else:
        #     print("Error: Phone number contains just numbers.")
        

        with open(file_path, 'r') as getdata:
            data = json.load(getdata)   # convert json to python

            if len(data):
                # the last id in the dict
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
                print("Successfully Added.")

    # -------------------------------------------------------------


    def view_data():
        with open(file_path, 'r') as view:
            data = json.load(view)
            for key, value in data.items():
                for k, v in value.items():
                    print(f"{k.title()}: ", end=" ")
                    print(f"{v.title()}")
                print('\n')


    def delete_data():
        id = input("Enter Contact id: ")

        with open(file_path, 'r') as getdata:
            data = json.load(getdata)

            if id in data:
                deleted_cont = data.pop(id) 

                with open(file_path, 'w') as delete:
                    data_1 = json.dump(data, delete)
                    print(f"{deleted_cont['name']} was deleted.")



    def update_data():
        view_data()

        id = input("Enter Contact id: ")

        with open(file_path, 'r') as getdata:
            data = json.load(getdata)
            if id in data:
                name = input("Enter Now Name: ")
                phone = input("Enter Now Phone: ")

                dic = {
                    "id" : id, 
                    "name" : name,
                    "phone" : phone,
                }
                data[id] = dic
                with open(file_path, 'w') as update:
                    json.dump(data, update)
                    print(f"Successfully Updated.")


        # print("What Do You To Change Change?")
        

    # -------------------------------------------------------------

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

    # -------------------------------------------------------------
    # # -------------------------------------------------------------
    if user_choice.isdigit():

        file_path = 'contacts.json'

        switch()

    else:
        print("Error: Invalid choice, just digits are available.")
    


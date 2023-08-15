import json

from enum import Enum

import os


class Choice(Enum):
    VIEW = "1"
    ADD = "2"
    DELETE = "3"
    UPDATE = "4"
    SEARCH = "5"
    EXIT = "6"


Choice_values = [member.value for member in Choice]

# -------------------------------------------------------------

print("-" * 35, "\n\tYOUR CONTACT LIST")
print("-" * 35, "\n")

# -------------------------------------------------------------

file_path = "contacts.json"
user_choice = ""
# -------------------------------------------------------------


def check_name_phone(name, phone):
    if not phone.isdigit():
        return f"Phone includes just numbers. ( {phone} ) is not a phone number! \nAgain please: \n"

    elif name.isdigit():
        return f"At least one letter included. ( {name} ) is not a name! \nAgain please: \n"
    else:
        return False


# -------------------------------------------------------------


def check_repeate(name, phone, updated_id="0"):
    with open(file_path, "r") as getdata:
        data = json.load(getdata)

        for key, value in data.items():
            if name in value.values() and updated_id != key:
                if phone in value.values():
                    return "\nThis contact is already existed! \nAdd new please: \n"

                return f"\nThis name ( {name} ) is repeated! \nAgain please: \n"
            if phone in value.values() and updated_id != key:
                return (
                    f"\nThis phone number ( {phone} ) is repeated! \nAgain please: \n"
                )

    return False


# ------------------------------------------------------------------------------------------


def get_id_by_name_phone(input1):
    with open(file_path, "r") as getdata:
        data = json.load(getdata)

        for key, value in data.items():
            if input1 in value.values():
                id = key
                return id, value["name"], value["phone"]  # returns tuple

    return False


# ------------------------------------------------------------------------------------------


def if_try_again():
    user_input = input("Do you want to try again? y  n \n").strip().lower()
    print("\n")
    to_main_minue = True if user_input == "y" or user_input == "yes" else False
    return to_main_minue


# ------------------------------------------------------------------------------------------


def style_text(the_string=""):
    char_style_number = len(the_string) + 20
    character = "^"
    print("\n")
    print(character * char_style_number)
    print(the_string.center(char_style_number, character))
    print(character * char_style_number)
    print("\n")


# ------------------------------------------------------------------------------------------


def add_data():
    name = input("Enter Name: ").strip().lower()
    phone = input("Enter Phone Number: ").strip()

    with open(file_path, "r") as getdata:
        data = json.load(getdata)  # convert json to python

        if check_name_phone(name, phone):
            print(check_name_phone(name, phone))
            switch(Choice.ADD.value, if_try_again())

        elif check_repeate(name, phone):
            print(check_repeate(name, phone))
            switch(Choice.ADD.value, if_try_again())

        else:
            if len(data):
                # get the last id in the dict
                no = int(list(data)[-1]) + 1
                no = str(no)
            else:
                no = "1"

            dict_contact = {
                "id": no,
                "name": name,
                "phone": phone,
            }

            data[no] = dict_contact

            with open(file_path, "w") as save:
                json.dump(data, save)  # python to json
                os.system("cls")
                style_text(f" ( {name}  [{phone}] ) Added Successfully . ")


# ---------------------------------------------------


def view_data():
    with open(file_path, "r") as view:
        data = json.load(view)
        if data:
            print(
                "",
                "-" * 45,
                "\n",
                "|",
                "Id".center(6, " "),
                "|",
                "Name".center(15, " "),
                "|",
                "Phone".center(14, " "),
                "|",
                "\n",
                "-" * 45,
            )
            for key, value in data.items():
                for k, v in value.items():
                    c = 6 if k == "id" else 15
                    print(" |", v.title().center(c, " "), end="")
                print("|")
            print("", "-" * (c * 3))
        else:
            print("\nNo Contacts to show!\n")


# ---------------------------------------------------


def delete_data():
    user_input = input("Enter an id, name, or phone number: ").strip().lower()
    contact_info = get_id_by_name_phone(user_input)

    if contact_info:
        with open(file_path, "r") as getdata:
            data = json.load(getdata)
            id = contact_info[0]
            deleted_cont = data.pop(id)

            with open(file_path, "w") as delete:
                data_1 = json.dump(data, delete)

                os.system("cls")
                style_text(f" ( {deleted_cont['name']} ) was deleted. ")
    else:
        print(f"This contact ( {user_input} ) is not exists!\n")
        switch(Choice.DELETE.value, if_try_again())


# ---------------------------------------------------


def update_data():
    view_data()

    user_input = input("Enter an id, name, or phone number: ").strip().lower()
    contact_info = get_id_by_name_phone(user_input)

    if contact_info:
        with open(file_path, "r") as getdata:
            data = json.load(getdata)

            name = input("Enter Now Name: ").strip().lower()
            phone = input("Enter Now Phone: ").strip()

            if name == contact_info[1] and phone == contact_info[2]:
                style_text(f" No change happened. ")
                switch(Choice.VIEW.value, True)

            elif check_repeate(name, phone, contact_info[0]):
                print(check_repeate(name, phone))
                switch(Choice.UPDATE.value, if_try_again())

            elif check_name_phone(name, phone):
                print(check_name_phone(name, phone))
                switch(Choice.UPDATE.value, if_try_again())

            else:
                dic = {
                    "id": contact_info[0],
                    "name": name,
                    "phone": phone,
                }
                data[contact_info[0]] = dic
                with open(file_path, "w") as update:
                    data1 = json.dump(data, update)
                    # os.system("cls")
                    style_text(f" Successfully Updated. ")
    else:
        print(f"This contact ( {user_input} ) is not exists!\n")
        switch(Choice.UPDATE.value, if_try_again())


# -------------------------------------------------------------------


def search_data():
    user_input = (
        input("Enter an id, name, or phone number to search for: ").strip().lower()
    )
    contact_info = get_id_by_name_phone(user_input)
    if contact_info:
        print(f"Name: {contact_info[1]} \nPhone: {contact_info[2]}")

    else:
        print(f"This contact ( {user_input} ) is not exists!\n")
        switch(Choice.SEARCH.value, if_try_again())


# -------------------------------------------------------------------
def switch(user_choice="2", try_again=True):
    if not try_again:
        os.system("cls")
        s = """
------------------------------------------------------------------------
---------------------**   Main Menue    **------------------------------
------------------------------------------------------------------------
"""
        print(s)
        print("1. View \n2. Add \n3. Delete \n4. Update \n5. Search \n6. Exit")

        user_choice = input("\nEnter Choice: ").strip()
        print("\n")

    if user_choice in Choice_values:
        if user_choice == Choice.VIEW.value:
            view_data()
        elif user_choice == Choice.ADD.value:
            add_data()
        elif user_choice == Choice.DELETE.value:
            delete_data()
        elif user_choice == Choice.UPDATE.value:
            update_data()
        elif user_choice == Choice.SEARCH.value:
            search_data()
        else:
            print("Thank You ^^ \n\n")
            exit()


# ------------------------------------------------------------------------------------
# --------------------------**   START THE PROGRAM    **------------------------------
# ------------------------------------------------------------------------------------

while user_choice != Choice.EXIT.value:
    s = """
------------------------------------------------------------------------
---------------------**   Main Menue    **------------------------------
------------------------------------------------------------------------
"""
    print(s)
    print("1. View \n2. Add \n3. Delete \n4. Update \n5. Search \n6. Exit")

    user_choice = input("\nEnter Choice: ").strip()
    print("\n")

    if user_choice in Choice_values:
        switch(user_choice)

    else:
        print(
            f"XXX Error: Invalid choice, just digits from {Choice_values[0]} to {Choice_values[-1]} XXX.\n"
        )

# ------------------------------------------------------------------------------------------

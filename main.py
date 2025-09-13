import json
import random
import tkinter
import pyperclip
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def display_password():
    password_entry.delete(0, "end")

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password_1 = password_entry.get()
    new_data = {
        website: {
            "email":email_username,
            "password": password_1
        }
    }

    if len(website) == 0 or len(email_username) == 0 or len(password_1) == 0:
        messagebox.showerror(title="Error", message="Please fill all the fields")
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nWebsite: {website}"
                                                      f"\nEmail/Username: {email_username}\nPassword: {password_1}"
                                                      f"\nAre those details valid and can be saved?")
        if is_okay:
            try:
                with open("data.json", mode="r") as data:
                    piece_of_data = json.load(data)
                    piece_of_data.update(new_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as data:
                    json.dump(new_data, data, indent=4)
            else:
                with open("data.json", mode="w") as data:
                    json.dump(piece_of_data, data, indent=4)
            finally:
                website_entry.delete(0, "end")
                password_entry.delete(0, "end")

# ---------------------------- DISPLAY DATA LOCATED IN JSON FILE ------------------------------- #
def find_password():
    user_entry = website_entry.get()
    try:
        with open("data.json", mode="r") as data:
            all_data = json.load(data)
            try:
                messagebox.showinfo(title=user_entry, message=f"Email: {all_data[user_entry]['email']}\nPassword: {all_data[user_entry]['password']}")
            except KeyError:
                messagebox.showerror(title="Error", message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.minsize(400, 350)
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
lockImage = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lockImage)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text="Website:", fg="black", font=("Arial" , 10))
website_label.grid(column=0, row=1)

email_username_label = tkinter.Label(text="Email/Username:", fg="black", font=("Arial", 10))
email_username_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", fg="black", font=("Arial", 10))
password_label.grid(column=0, row=3)

website_entry = tkinter.Entry(width=27)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")

search_button = tkinter.Button(text="Search", width=13, font=("Arial", 10), highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1, sticky="w")

email_username_entry = tkinter.Entry(width=42)
email_username_entry.insert(0, "example@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="w")

password_entry = tkinter.Entry(width=27)
password_entry.grid(column=1, row=3, sticky="w")

generate_pass_button = tkinter.Button(text="Get Password", width=13, font=("Arial", 10), highlightthickness=0, command=display_password)
generate_pass_button.grid(column=2, row=3, sticky="w")

add_button = tkinter.Button(text="Add", width=39, height=1, command=save_data)
add_button.grid(column=1, row=5, columnspan=2, sticky="w")

window.mainloop()
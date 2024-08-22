from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import sync



# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    p_word.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = site.get().title()
    email = user_n.get()
    password = p_word.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data_desktop.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data_desktop.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data
            data.update(new_data)
            with open("data_desktop.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            site.delete(0, END)
            p_word.delete(0, END)
            site.focus()

# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password(site):
    try:
        with open("data_desktop.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if site in data:
            user_email = data[site]["email"]
            user_pword = data[site]["password"]
            messagebox.showinfo(title=site, message=f"Email: {user_email} \nPassword: {user_pword}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {site} exist")

# ---------------------------- Sync Data ------------------------------- #

sync.sync_data()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
web = Label(text="Website:", bg="white", fg="black")
web.grid(row=1, column=0)

email = Label(text="Email/Username:", bg="white", fg="black")
email.grid(row=2, column=0)

password = Label(text="Password:", bg="white", fg="black")
password.grid(row=3, column=0)

# Entries
site = Entry(width=20, bg="white", fg="black", highlightthickness=0)
site.grid(row=1, column=1)
site.focus()

user_n = Entry(width=35, bg="white", fg="black", highlightthickness=0)
user_n.grid(row=2, column=1, columnspan=2)
user_n.insert(0, "djcamp14@gmail.com")

p_word = Entry(width=20, bg="white", fg="black", highlightthickness=0)
p_word.grid(row=3, column=1)

# Buttons
search = Button(text="Search", width=11, highlightbackground="white", command=lambda: find_password(site.get().title()))
search. grid(row=1, column=2)

generate_pword = Button(text="Generate Password", width=11, highlightbackground="white", command=generate_password)
generate_pword.grid(row=3, column=2)

add_button = Button(text="Add", width=33, highlightbackground="white", command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

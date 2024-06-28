import tkinter as tk
from tkinter import simpledialog, messagebox

def add_pass():
    name = simpledialog.askstring("Input", "Enter Name:")
    password = simpledialog.askstring("Input", "Enter Password:")

    if name and password:
        with open("Passwords.txt", "a") as f:
            f.write(name + "|" + password + "\n")
        messagebox.showinfo("Success", "Password Added Successfully!")
    else:
        messagebox.showwarning("Input Error", "Name or Password cannot be empty!")

def view_pass():
    try:
        with open("Passwords.txt", "r") as f:
            passwords = f.readlines()

        if passwords:
            result = ""
            for line in passwords:
                data = line.rstrip()
                username, passw = data.split("|")
                result += f"Username: {username}\nPassword: {passw}\n\n"
            messagebox.showinfo("Stored Passwords", result)
        else:
            messagebox.showinfo("No Passwords", "No passwords stored yet.")
    except FileNotFoundError:
        messagebox.showinfo("No Passwords", "No passwords stored yet.")

def check_master_password():
    master_password = simpledialog.askstring("Master Password", "Enter Master Password:", show='*')
    if master_password == "OP":
        main_menu()
    else:
        messagebox.showerror("Error", "Wrong Master Password!")
        root.destroy()

def main_menu():
    root.title("Passwords Manager by OP")
    root.geometry("6    00x300")
    root.configure(bg='black')

    title = tk.Label(root, text="Passwords Manager by OP", font=("Helvetica", 30, "bold"), bg='black', fg='#00FF00')
    title.pack(pady=20)

    add_button = tk.Button(root, text="Add Password", command=add_pass, font=("Helvetica", 14), bg='black', fg='#00FF00')
    add_button.pack(pady=10)

    view_button = tk.Button(root, text="View Password", command=view_pass, font=("Helvetica", 14), bg='black', fg='#00FF00')
    view_button.pack(pady=10)

    exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Helvetica", 14), bg='black', fg='#00FF00')
    exit_button.pack(pady=10)

root = tk.Tk()
check_master_password()
root.mainloop()

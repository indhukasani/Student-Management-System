import tkinter as tk
from tkinter import messagebox

def validate_age(new_value):
    if new_value == "" or new_value.isdigit():
        return True
    return False

def add_student():
    name = entry_name.get()
    age = entry_age.get()
    course = course_var.get()
    gender = gender_var.get()
    if name == "" or age == "" or course == "Select Course" or gender=="gender":
        messagebox.showwarning("Input Error", "Please fill all details!")
        return

    student_data = f"Name: {name} | Age: {age} | Course: {course} | Gender: {gender}"
    listbox.insert(tk.END, student_data)

    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    course_var.set("Select Course")

def delete_student():
    selected_item = listbox.curselection()

    if not selected_item:
        messagebox.showwarning("Selection Error", "Please select a student to delete!")
        return

    listbox.delete(selected_item)
    
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x500")

tk.Label(root, text="Student Management System",font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)

tk.Label(root, text="Age:").pack()

validate_cmd = root.register(validate_age)
entry_age = tk.Entry(root, width=30, validate="key",validatecommand=(validate_cmd, "%P"))
entry_age.pack(pady=5)

tk.Label(root, text="Course:").pack()
course_var = tk.StringVar()
course_var.set("Select Course")

course_menu = tk.OptionMenu(root, course_var,"CSE", "IT", "EEE", "ECE", "IOT")
course_menu.pack(pady=5)

tk.Label(root, text="Gender").pack()
gender_var = tk.StringVar()

tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack()

tk.Button(root, text="Add Student", command=add_student).pack(pady=10)

listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Delete Selected", command=delete_student).pack(pady=5)

root.mainloop()

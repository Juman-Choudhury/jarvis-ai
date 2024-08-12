import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os

filepath = "F:\\Programming videos\\Python\\data.xlsx"

# Create workbook and sheet if it doesn't exist
if not os.path.exists(filepath):
    work_book = openpyxl.Workbook()
    sheet = work_book.active
    heading = ["Title", "FirstName", "LastName", "Age", "Nationality",
               "Completed Course", "Completed Semester", "Registration Status"]
    sheet.append(heading)
    work_book.save(filepath)

# Create the main window
window = tk.Tk()
window.title("My Application")
window.geometry("700x500")

def getData():
    # User info
    title = title_Dmenu.get()
    firstName = first_name_entry.get()
    lastName = last_name_entry.get()
    Age = user_inpt_age.get()
    Nationality = user_nationality_input.get()
    if title and firstName and lastName and Nationality:
        if int(Age) <= 0:
            messagebox.showwarning("Warning", "Age should be greater than zero!")
            return

        # Registration Status info
        compCourse = numCourse_spin.get()
        CompSemester = numSems_spin.get()
        regStatus = reg_status_var.get()

        # Printing details
        print(f"Title: {title}| First name: {firstName}| Last name: {lastName}\n"
              "-------------------------------------------\n"
              f"Completed Course: {compCourse}| Completed Semester: {CompSemester}\n"
              "-------------------------------------------\n"
              f"Registration Status: {regStatus}")

        # Append data to the Excel sheet
        work_book = openpyxl.load_workbook(filepath)
        sheet = work_book.active
        sheet.append([title, firstName, lastName, Age, Nationality, compCourse, CompSemester, regStatus])
        work_book.save(filepath)
    else:
        messagebox.showerror("Error", "Enter user details properly!")

frame = tk.Frame(window)
frame.pack()
frame.rowconfigure((0, 1, 2), weight=1)
frame.columnconfigure(0, weight=1)

user_info = tk.LabelFrame(frame, text="User Info", font=('Arial', 12))

title_label = tk.Label(user_info, text="Select title", font=('Arial', 12))
title_Dmenu = ttk.Combobox(user_info, values=["Mr.", "Mrs.", "Miss", "Ms.", "Dr.", "Prof.", "Rev.", "Sir", "Lady", "Lord", "Mx."], state='readonly', font=('Arial', 12))
title_label.grid(row=0, column=0)
title_Dmenu.grid(row=1, column=0)

first_name_label = tk.Label(user_info, text="First name", font=('Arial', 12))
first_name_label.grid(row=0, column=1)
last_name_label = tk.Label(user_info, text="Last name", font=('Arial', 12))
last_name_label.grid(row=0, column=2)

first_name_entry = tk.Entry(user_info, font=('Arial', 12))
last_name_entry = tk.Entry(user_info, font=('Arial', 12))
first_name_entry.grid(row=1, column=1, padx=20)
last_name_entry.grid(row=1, column=2, padx=20)

user_age_label = tk.Label(user_info, text="Enter your age", font=('Arial', 12))
user_inpt_age = tk.Spinbox(user_info, from_=0, to=200, increment=1, font=('Arial', 12))
user_age_label.grid(row=2, column=0)
user_inpt_age.grid(row=3, column=0, sticky='w', padx=20)

user_nationality_label = tk.Label(user_info, text="Nationality", font=('Arial', 12))
user_nationality_input = ttk.Combobox(user_info, values=[
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda",
    "Argentina", "Armenia", "Australia", "Austria", "Azerbaijan", "Bahamas",
    "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", "Belize", "Benin",
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon",
    "Canada", "Central African Republic", "Chad", "Chile", "China", "Colombia",
    "Comoros", "Congo, Democratic Republic of the", "Congo, Republic of the",
    "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Denmark", "Djibouti",
    "Dominica", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea",
    "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala",
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland",
    "India", "Indonesia", "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica",
    "Japan", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Korea, North", "Korea, South",
    "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho",
    "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar",
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania",
    "Mauritius", "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia", "Montenegro",
    "Morocco", "Mozambique", "Myanmar", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Macedonia", "Norway",
    "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda",
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia",
    "Seychelles", "Sierra Leone", "Singapore", "Slovakia", "Slovenia", "Solomon Islands",
    "Somalia", "South Africa", "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand",
    "Timor-Leste", "Turkey", "Turkmenistan", "Tuvalu", "Uganda", "Ukraine", "United Arab Emirates",
    "United Kingdom", "United States", "Uruguay", "Uzbekistan", "Vanuatu", "Vatican City",
    "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
], state='readonly', font=('Arial', 12))

user_nationality_label.grid(row=2, column=1)
user_nationality_input.grid(row=3, column=1)

user_info.grid(row=0, column=0)

course_frame = tk.LabelFrame(frame, text="Registration Status", font=('Arial', 12))
reg_status_var = tk.StringVar(value="Not registered!")
registration_check = tk.Checkbutton(course_frame, text="Currently registered", onvalue="Registered!", offvalue="Not registered!", variable=reg_status_var, font=('Arial', 12))
registration_check.grid(row=1, column=0)

numCourse_label = tk.Label(course_frame, text="Completed Course", font=('Arial', 12))
numCourse_spin = tk.Spinbox(course_frame, from_=0, to='infinity', font=('Arial', 12))
numCourse_label.grid(row=0, column=1)
numCourse_spin.grid(row=1, column=1, padx=20)

numSems_label = tk.Label(course_frame, text="Completed Semester", font=('Arial', 12))
numSems_spin = tk.Spinbox(course_frame, from_=0, to='infinity', font=('Arial', 12))
numSems_label.grid(row=0, column=2)
numSems_spin.grid(row=1, column=2)
course_frame.grid(row=1, column=0, sticky='news', pady=(10, 0))

terms_frame = tk.LabelFrame(frame, text="Accept terms & conditions", font=('Arial', 12))
terms_check = tk.Checkbutton(terms_frame, text="I accept terms & conditions", font=('Arial', 12))
terms_check.grid(sticky='w')
terms_frame.grid(row=2, column=0, sticky='news', ipady=10)

Enter_button = tk.Button(frame, text="Enter data", font=('Arial', 12), bd=5, relief='raised', command=getData)
Enter_button.grid(row=3, column=0, pady=20, sticky='nwes')

window.mainloop()

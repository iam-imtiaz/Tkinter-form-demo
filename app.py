import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from countries import all_countries
from tkcalendar import Calendar
from utility import get_hours, get_minutes, get_meridiem


# Submit button command
def submit_btn():
    window.geometry('620x500')
    text_area.grid()
    text_area.configure(state='normal')
    text_area.delete("1.0", "end")
    text_area.insert(tk.INSERT, "Hello")
    text_area.configure(state='disable')


# Browse file button command
def browse_file():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.*"),
                                                     ("all files",
                                                      "*.txt*")))
    file_browse_text.set(filename)
    return


# Browse directory button command
def browse_directory():
    dirname = filedialog.askdirectory(initialdir="/",
                                          title="Select a directory")

    dir_browse_text.set(dirname)
    return


def show_selected_date(date,top):
    print(date)
    date_text.set(date)
    top.destroy()
    return


def date_picker():
    top = tk.Toplevel(window)
    x = window.winfo_x()
    y = window.winfo_y()
    top.geometry("+%d+%d" % (x + 250, y + 50))
    top.wm_transient(window)
    cal = Calendar(top, selectmode='day', date_pattern="dd-mm-y")
    cal.bind("<<CalendarSelected>>",lambda event: show_selected_date(cal.get_date(),top))
    cal.pack(fill="both", expand=True)


def gender_selection():
    print("gender", gender_var.get())
    print("hello")

# Creating tkinter window and set dimensions
window = tk.Tk()
window.title('Form Submission')
window.geometry('620x400')
window.resizable(0, 0)
my_countries = all_countries.all_country_names

frame_1 = tk.Frame(window)
frame_1.grid(row=0, column=1)
frame_2 = tk.Frame(window)
frame_2.grid(row=0, column=2)

# Frame 1
ttk.Label(frame_1, text="First Name", foreground="black").grid(row=0, column=1, padx=10, pady=15)
ttk.Label(frame_1, text="Last Name", foreground="black").grid(row=1, column=1, padx=10, pady=15)
ttk.Label(frame_1, text="Nationality", foreground="black").grid(row=2, column=1, padx=15)

# Separator
ttk.Separator(frame_1, orient='vertical').grid(column=3, row=0, padx=30, pady=5, rowspan=3, sticky='ns')
# Frame 2
ttk.Label(frame_2, text="Date of Birth", width=15,  foreground="black").grid(row=0, column=1, pady=15)
ttk.Label(frame_2, text="Time",width=15, foreground="black").grid(row=1, column=1, pady=15)
ttk.Label(frame_2, text="Gender",width=15, foreground="black").grid(row=2, column=1, pady=15)


# Input Frame 1
first_name_entry = tk.Entry(frame_1, width=25, foreground="black").grid(row=0, column=2, padx=5, pady=15)
last_name_entry = tk.Entry(frame_1,width=25, foreground="black").grid(row=1, column=2, padx=5, pady=15)

# Adding countries drop down list
country_var = tk.StringVar()
country_var.set(my_countries[102])
country_combo = ttk.Combobox(frame_1, width=22, textvariable=country_var)
country_combo['values'] = my_countries
country_combo.grid(column=2, row=2, pady=15)
country_combo.current()

# Frame 2 input
calendar_time = tk.Frame(frame_2)
calendar_time.grid(row=0, column=2)

# Date
calendar_image = tk.PhotoImage(file =r"calendar.png")
date_text = tk.StringVar()
date_entry = ttk.Label(calendar_time, background="white", width=21, foreground="black", textvariable=date_text).grid(row=0, column=1, pady=15)
button = tk.Button(calendar_time, width=15,image=calendar_image ,foreground="black", command=date_picker).grid(row=0, column=2,padx=5, pady=15)

# Gender
gender_var = tk.StringVar()
gender_var.set("male")
frame_gender = tk.Frame(frame_2)
frame_gender.grid(row=2, column=2)
female = tk.Radiobutton(frame_gender, text='Female', value='female', variable=gender_var, command=gender_selection).grid(row=0, column=0, padx=0, pady=15)
male = tk.Radiobutton(frame_gender, text='Male',  value='male', variable=gender_var,  command=gender_selection).grid(row=0, column=1,padx=25, pady=15)

# Time
frame_time = tk.Frame(frame_2)
frame_time.grid(row=1, column=2)
# Hour Combo
hour_var = tk.StringVar()
hour_var.set(get_hours()[0])
hour_combo = ttk.Combobox(frame_time, width=4, textvariable=hour_var)
hour_combo['values'] = get_hours()
hour_combo.grid(column=1, row=1, pady=15)
hour_combo.current()
# Minute Combo
minute_var = tk.StringVar()
minute_var.set(get_minutes()[0])
minute_combo = ttk.Combobox(frame_time, width=4, textvariable=minute_var)
minute_combo['values'] = get_minutes()
minute_combo.grid(column=2, row=1, padx=10, pady=15)
minute_combo.current()
# Minute Combo
meridiem_var = tk.StringVar()
meridiem_var.set(get_meridiem()[0])
meridiem_combo = ttk.Combobox(frame_time, width=4, textvariable=meridiem_var)
meridiem_combo['values'] = get_meridiem()
meridiem_combo.grid(column=3, row=1 ,pady=15)
meridiem_combo.current()

# horizontal separator
ttk.Separator(window, orient='horizontal').grid(row=1, padx=10, pady=20, columnspan=3, sticky='we')

#file explorer
file_dir_explore_frame = tk.Frame(window)
file_dir_explore_frame.grid(row=3,columnspan=3)
file_browse_text = tk.StringVar()
label_file_explorer = ttk.Label(file_dir_explore_frame, text="Resume").grid(row=0, padx=10, column=1, pady=15)
# file_browse = ttk.Entry(file_dir_explore_frame ,width=70,foreground="black", textvariable=file_browse_text ).grid(row=0, column=2, padx=5, pady=15, sticky='ns')
file_browse = ttk.Label(file_dir_explore_frame ,background="white", width=70,foreground="black",wraplength=400, textvariable=file_browse_text ).grid(row=0, column=2, padx=5, pady=15)
file_browse_btn = tk.Button(file_dir_explore_frame, text="Browse",width=10 ,foreground="black",command = browse_file).grid(row=0, column=3,padx=5, pady=15)

# Create a directory Explorer label
dir_browse_text = tk.StringVar()
dir_file_explorer = ttk.Label(file_dir_explore_frame, text="Directory").grid(row=1, padx=10, column=1, pady=15)
dir_browse = ttk.Label(file_dir_explore_frame, background="white",wraplength=400, width=70,foreground="black", textvariable=dir_browse_text).grid(row=1, column=2, padx=5, pady=15)
dir_browse_btn = tk.Button(file_dir_explore_frame, text="Browse",width=10 ,foreground="black", command = browse_directory).grid(row=1, column=3,padx=5, pady=15)
submit_btn = tk.Button(file_dir_explore_frame, text="Submit", width=10 ,foreground="black", command = submit_btn).grid(row=2, column=2,padx=5, pady=15)

# Hidden textarea
text_area = scrolledtext.ScrolledText(file_dir_explore_frame, wrap=tk.WORD,
                                      width=53, height=4, state='disable')
text_area.grid(columnspan=4, column=1, row=3, pady=10, padx=5)
text_area.grid_remove()

window.mainloop()



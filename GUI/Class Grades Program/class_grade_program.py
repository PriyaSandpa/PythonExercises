from tkinter import*

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

def show_grade(event):
    current_cursor = students_listbox.curselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[0].get_grade())
    
csc_2=[]

csc_2.append(Student("Boaz", "Excellence"))
csc_2.append(Student("Rehaan", "Merit"))
csc_2.append(Student("Aaran", "Merit"))
csc_2.append(Student("Christian", "Achieved"))
csc_2.append(Student("Siddhu", "Achieved"))
csc_2.append(Student("Hamish", "Excellence"))
csc_2.append(Student("Aarzoo", "Achieved"))
csc_2.append(Student("Shauryya", "Merit"))
csc_2.append(Student("Zakaria", "Excellence"))
csc_2.append(Student("Amon", "Achieved"))
csc_2.append(Student("Yaneth", "Excellence"))
csc_2.append(Student("Kajah", "Achieved"))
csc_2.append(Student("Bilal", "Excellence"))
csc_2.append(Student("Ken", "Merit"))
csc_2.append(Student("Mohammed", "Achieved"))
csc_2.append(Student("Spike", "Merit"))
csc_2.append(Student("Tharin", "Excellence"))
csc_2.append(Student("Thushann", "Achieved"))
csc_2.append(Student("Fathihe", "Achieved"))
csc_2.append(Student("Abubakr", "Excellence"))
csc_2.append(Student("Anna", "Excellence"))
csc_2.append(Student("Krish", "Merit"))
csc_2.append(Student("Melissa", "Merit"))
csc_2.append(Student("Kamlesh", "Achieved"))
csc_2.append(Student("Gabriel", "Merit"))
csc_2.append(Student("Jacob", "Excellence"))
csc_2.append(Student("Zhiliang", "Merit"))

window = Tk()
window.geometry("300x300")
window.title("Class Grades")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0,[])


grade_label = Label()
grade_label.pack()
show_grade_btn = Button(text="Show Grade", command=show_grade)
show_grade_btn.pack()

window.mainloop()

from tkinter import*

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def get_grade(self):
        return self.grade

def show_grade(self):
    current_cursor = students_listbox.curselection()
    current_student = current_cursor[0]
    grade_label.config(text=csc_2[0].get_grade())
    
csc_2=[]

csc_2.append(Student("Boaz", "Excellence"))
csc_2.append(Student("Rehaan", "Merit"))
csc_2.append(Student("Aaran", "Merit"))

window = Tk()
window.geometry("300x300")
window.title("Class Grades")

students_listbox = Listbox(window)
students_listbox.pack()

students_listbox.insert(0,"Boaz")
students_listbox.insert(0,"Rehaan")
students_listbox.insert(0,"Aaran")



grade_label = Label()
grade_label.pack()
show_grade_btn = Button(text="Show Grade", command=show_grade())
show_grade_btn.pack()

window.mainloop()

from tkinter import*
from tkinter import ttk #module to provide access to TK themed widget set
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2

class assignment:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")#size-x.axis-y.axis
        self.root.title("Face regonition system")
        
         ### variables declaration ###
        self.var_class = StringVar()
        self.var_section = StringVar()
        self.var_subject = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_assignment = StringVar()
        self.var_status = StringVar()
        
        #student registration 
        title_lbl=Label(text="ASSIGNMENT SECTION",font=("times new roman",35,"bold"),bg="black",fg="white")#bgimg
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
    #Adding background image if you want 
        #img1 = Image.open(r"C:\Users\.....path......jpg")
        #img1 = img1.resize((1530,710),Image.LANCZOS )
        #self.photoimg1 = ImageTk.PhotoImage(img1)
        # bg_img = Label(self.root,image = self.photoimg1)
        #bg_img.place(x=0,y=45,width=1530,height=710)

    #making frame 
        main_frame=Frame(bd=2) #bgimage add hane paxi change to (bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1530,height=790)
    
    #left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=700)  


     #left side label frame--current course
        current_course = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course.place(x=10,y=10,width=720,height=150)
     #class combobox
        class_label = Label(current_course,text="Class",font=("times new roman",12,"bold"),bg="white")
        class_label.grid(row=0,column=0,padx=10)

        #combo box
        class_combo = ttk.Combobox(current_course,textvariable=self.var_class,font=("times new roman",12,"bold"),width=17,state="read only")
        class_combo["values"]=("Select Class","i","ii","iii","iv","v","vi","vii","viii","ix","x",)
        class_combo.current(0)
        class_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
    
     #Section Part
        section_label = Label(current_course,text="Section",font=("times new roman",12,"bold"),bg="white")
        section_label.grid(row=1,column=0,padx=15,pady=5,sticky=W)
        
        section_combo = ttk.Combobox(current_course,textvariable=self.var_section,font=("times new roman",12,"bold"),width=17,state="read only")
        section_combo["values"]=("Select Section","A","B")
        section_combo.current(0)
        section_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)
        #for manually entering section 
        # section_entry=ttk.Entry(current_course,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        # section_entry.grid(row=1,column=1,padx=2,pady=5,sticky=W)

       #Subject Part
        subject_label = Label(current_course,text="Subject",font=("times new roman",12,"bold"),bg="white")
        subject_label.grid(row=0,column=4,padx=10,pady=5,sticky=W)

        assignment_entry=ttk.Entry(current_course,textvariable=self.var_subject,width=20,font=("times new roman",12,"bold"))
        assignment_entry.grid(row=0,column=5,padx=2,pady=5,sticky=W)
 
        #list button
        listbtn=Button(current_course,text="List All",command=self.fetch_data,font=("times now roman",13,"bold"),bd=3,relief=RIDGE,fg="white",bg="grey",activeforeground="black",activebackground="silver")
        listbtn.grid(row=1,column=5,padx=5,pady=2,sticky=W)
        




#.............................................................................................................................................
        
        #Student Imformation
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Assign Marks",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=160,width=720,height=500)  

        #Student name
        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=10,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=10,sticky=W)

         #Roll Number
        roll_number_label = Label(class_student_frame,text="Roll Number:",font=("times new roman",12,"bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        roll_number_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_number_entry.grid(row=1,column=3,padx=10,pady=10,sticky=W)
        
        #Subject Part
        subject_label = Label(class_student_frame,text="Subject:",font=("times new roman",12,"bold"),bg="white")
        subject_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)

        assignment_entry=ttk.Entry(class_student_frame,textvariable=self.var_subject,width=20,font=("times new roman",13,"bold"))
        assignment_entry.grid(row=2,column=3,padx=10,pady=10,sticky=W)

        #Assignment
        assignment_label = Label(class_student_frame,text="Assignment:",font=("times new roman",12,"bold"),bg="white")
        assignment_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        
        assignment_entry=ttk.Entry(class_student_frame,textvariable=self.var_assignment,width=20,font=("times new roman",13,"bold"))
        assignment_entry.grid(row=3,column=3,padx=10,pady=10,sticky=W)

       #Status Part check buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_status,text="Assignment Submitted",value="Submitted")
        radiobtn1.grid(row=4,column=2,padx=10,pady=10)
        
         
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_status,text="Assignment Not Submitted",value="Not Submitted")
        radiobtn2.grid(row=4,column=3,padx=10,pady=10)

#...................................................................................................................................................
       
       #Button Frame
        btn_frame = Frame(class_student_frame,bd=0,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=270,width=710,height=178)

        #ADD Button
        add_btn = Button(btn_frame,text="Add",width=70,command=self.add_data,font=("times new roman",13,"bold"),bg="grey",fg="white",activeforeground="black",activebackground="silver")
        add_btn.grid(row=0,column=0,padx=5,pady=5)

        #Update Button
        update_btn = Button(btn_frame,text="Update",width=70,command=self.update_data,font=("times new roman",13,"bold"),bg="grey",fg="white",activeforeground="black",activebackground="silver")
        update_btn.grid(row=1,column=0,padx=5,pady=5)

        #Delete Button
        delete_btn = Button(btn_frame,text="Delete",width=70,command=self.delete_function,font=("times new roman",13,"bold"),bg="maroon",fg="white",activeforeground="black",activebackground="red")
        delete_btn.grid(row=2,column=0,padx=5,pady=5)

        #Reset Button
        reset_btn = Button(btn_frame,text="Reset",width=70,command=self.reset_data,font=("times new roman",13,"bold"),bg="grey",fg="white",activeforeground="black",activebackground="silver")
        reset_btn.grid(row=3,column=0,padx=5,pady=5)

#............................................................................................................................................................................................................
        #right side label frame
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=780,y=10,width=710,height=700)

####### Searching system #########
        Search_frame = LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",15,"bold"))
        Search_frame.place(x=10,y=10,width=680,height=70)  

        Search_label = Label(Search_frame,text="Search By:",font=("times new roman",12,"bold"),bg="grey",fg="white")
        Search_label.grid(row=0,column=0,padx=2,pady=5,sticky=W)

     
          
        #search combo box
        self.var_combo_search = StringVar()
        search_combo = ttk.Combobox(Search_frame,textvariable=self.var_combo_search,font=("times new roman",12,"bold"),width=17,state="read only")
        search_combo["values"]=("Select ","Roll","Name","Status","Assignment","Subject")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        self.var_search = StringVar()
        search_entry=ttk.Entry(Search_frame,textvariable=self.var_search,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        search_btn = Button(Search_frame,text="Search",width=12,command=self.search_data,font=("times new roman",13,"bold"),bg="Grey",fg="white")
        search_btn.grid(row=0,column=3,padx=5,pady=5)

       
 ###########  Table Frame ##########

        Table_frame = Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        Table_frame.place(x=10,y=100,width=680,height=550) 
 
  #Scroll Bar
        scroll_x = ttk.Scrollbar(Table_frame,orient=HORIZONTAL) 
        scroll_y = ttk.Scrollbar(Table_frame,orient=VERTICAL) 

        self.student_table = ttk.Treeview(Table_frame,columns=("Class","Section","Name","Roll_no","Subject","Assignment","Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
      
        self.student_table.heading("Class",text="Class")
        self.student_table.heading("Section",text="Section")
        #self.student_table.heading("ID",text="StudentID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll_no",text="Roll Number")
        self.student_table.heading("Subject",text="Subject")
        self.student_table.heading("Assignment",text="Assignment")
        self.student_table.heading("Status",text="Submission Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Class",width=100)
        self.student_table.column("Section",width=100)
        #self.student_table.column("ID",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll_no",width=100)
        self.student_table.column("Subject",width=100)
        self.student_table.column("Assignment",width=100)
        self.student_table.column("Status",width=100)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
         #self.fetch_data()

# ####################################################### FETCH DATA FROM DATABASE #################################################################

  
    def fetch_data(self):
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="qwerty123", database="admin_minorproject")
                my_cursor = conn.cursor()

                class_value = self.var_class.get()
                section_value = self.var_section.get()

                table_name = "assignment"
                column_name = "Assignment"
                query1 = f"SELECT COUNT(*) FROM {table_name} WHERE {column_name} IS NOT NULL"
                my_cursor.execute(query1)
                non_empty_count = my_cursor.fetchone()[0]
          
                if non_empty_count > 0:
                    query = """SELECT s1.Class, s1.Section, s1.Name, s1.Roll, a1.Subject, a1.Assignment, a1.Status
                              FROM student s1
                              LEFT JOIN assignment a1 ON s1.Student_id = a1.STUDENT_id 
                              WHERE s1.Class = %s AND s1.Section = %s"""
                    my_cursor.execute(query, (class_value, section_value))
                else:
                    query = "SELECT Class, Section, Name, Roll FROM student WHERE Class = %s AND Section = %s"
                    my_cursor.execute(query, (class_value, section_value))
                
                data = my_cursor.fetchall()

                if data:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in data:
                        self.student_table.insert("", "end", values=row)
                else:
                    messagebox.showerror("Error", "No data found", parent=self.root)
            except mysql.connector.Error as err:
                print(f"Error fetching data: {err}")
            finally:
                if conn.is_connected():
                    my_cursor.close()
                    conn.close()

####################################for adding data##########################################################
    def add_data(self):
        if self.var_class.get() == "Select Class" or self.var_roll.get() == "" or self.var_std_name.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="qwerty123", database="admin_minorproject")
                my_cursor = conn.cursor()

                query = "SELECT Student_id FROM student WHERE Class = %s AND Roll = %s AND Name = %s"
                my_cursor.execute(query, (self.var_class.get(), self.var_roll.get(), self.var_std_name.get()))
                student_id = my_cursor.fetchone()[0]

                # Check if marks already exist for the student and subject
                check_query = "SELECT * FROM assignment WHERE Student_id = %s AND Subject = %s"
                my_cursor.execute(check_query, (student_id, self.var_subject.get()))
                existing_marks = my_cursor.fetchone()

                if existing_marks:
                    messagebox.showerror("Error", "Status for this assignment already exist ", parent=self.root)
                else:
                    my_cursor.execute("INSERT INTO assignment (Student_id, Subject, Assignment, Status) VALUES (%s, %s, %s, %s)",
                                      (student_id, self.var_subject.get(), self.var_assignment.get(), self.var_status.get()))

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)

            except mysql.connector.Error as err:
                print(f"Error adding data: {err}")
                messagebox.showerror("Error", f"Due to :{str(err)}", parent=self.root)

    # ------------------------->get cursor <---------------

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)  #item takes the content.
        data = content["values"]

        self.var_class.set(data[0]),
        self.var_section.set(data[1]),
        self.var_std_name.set(data[2]),
        self.var_roll.set(data[3]),
        self.var_subject.set(data[4]),
        self.var_assignment.set(data[5]),
        self.var_status.set(data[6])
        

############################################  UPDATE FUNCTION ###############################################################    
  
    def update_data(self):
      if self.var_class.get() == "Select Class" or self.var_roll.get() == "" or self.var_std_name.get() == "":
          messagebox.showerror("Error", "All Fields are required", parent=self.root)
      else:
          try:
              update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
              if update:
                  # Connect to the database
                  conn = mysql.connector.connect(host="localhost", username="root", password="qwerty123", database="admin_minorproject")
                  my_cursor = conn.cursor()

                  # Execute the SQL query to fetch the student ID
                  query = "SELECT Student_id FROM student WHERE Class = %s AND Roll = %s AND Name = %s"
                  my_cursor.execute(query, (self.var_class.get(), self.var_roll.get(), self.var_std_name.get()))
                  row = my_cursor.fetchone()

                  if row:  # Check if student exists
                      student_id = row[0]  # Retrieve student ID from the result

                      # Update 
                      my_cursor.execute("UPDATE assignment SET Subject=%s, Assignment=%s, Status=%s WHERE STUDENT_id=%s", (
                          self.var_subject.get(),
                          self.var_assignment.get(),
                          self.var_status.get(),
                          student_id
                      ))

                      conn.commit()
                      self.fetch_data()
                      conn.close()
                      messagebox.showinfo("Success", "Student details successfully updated.", parent=self.root)
                  else:
                      messagebox.showerror("Error", "Student not found.", parent=self.root)
              else:
                  return
          except Exception as es:
              messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


######################################################### DELETE FUNCTION ###########################################################################      
        
    def delete_function(self):
          if self.var_class.get() == "Select Class" or self.var_roll.get() == "" or self.var_std_name.get() == "":
              messagebox.showerror("Error", "All Fields are required", parent=self.root)
          else:
              try:
                  delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
                  if delete:
                      conn = mysql.connector.connect(host="localhost", username="root", password="qwerty123", database="admin_minorproject")
                      my_cursor = conn.cursor()

                      # Execute the SQL query to fetch the student ID
                      query = "SELECT Student_id FROM student WHERE Class = %s AND Roll = %s AND Name = %s"
                      my_cursor.execute(query, (self.var_class.get(), self.var_roll.get(), self.var_std_name.get()))
                      row = my_cursor.fetchone()

                      if row:  # Check if student exists
                          student_id = row[0]  # Retrieve student ID from the result

                          # Delete student's data from the marks table
                          sql = "DELETE FROM assignment WHERE STUDENT_id = %s"
                          val = (student_id,)
                          my_cursor.execute(sql, val)
                          conn.commit()

                          # Fetch updated data and show success message
                          self.fetch_data()
                          messagebox.showinfo("Delete", "Successfully deleted student", parent=self.root)
                      else:
                          messagebox.showerror("Error", "Student not found.", parent=self.root)
                  else:
                      # User chose not to delete, do nothing
                      return
              except Exception as es:
                  messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
              finally:
                  # Close the database connection
                  if conn.is_connected():
                      my_cursor.close()
                      conn.close()

  
    ############ RESET Funtion ###############

    def reset_data(self):
        
        
        self.var_class.set("Select Class")
        self.var_section.set("Select Section")
        self.var_subject.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_assignment.set("")
        self.var_status.set("")
    
   ############################################### SEARCHING FUNCTION ######################################################
    
    def search_data(self):
        if self.var_combo_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select an option")
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="qwerty123",
                    database="admin_minorproject"
                )
                my_cursor = conn.cursor()

                # Get the class value and section value from the variables
                class_value = self.var_class.get()
                section_value = self.var_section.get()

                # Construct the SQL query with filter conditions for class and section
                query = """
                        SELECT student.Class,student.Section,student.Name,student.Roll, assignment.Subject, assignment.Assignment, assignment.Status
                        FROM student 
                        LEFT JOIN assignment ON student.Student_id = assignment.STUDENT_id 
                        WHERE {} = %s AND student.Class = %s AND student.Section = %s
                        """.format(self.var_combo_search.get())

                # Pass the search value, class value, and section value as parameters to the execute method
                search_value = self.var_search.get()
                my_cursor.execute(query, (search_value, class_value, section_value))

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                    conn.commit()
                else:
                    messagebox.showinfo("No Data", "No matching records found")

            except mysql.connector.Error as e:
                messagebox.showerror("Error", f"Database error: {e}")

            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {es}")

            finally:
                if 'conn' in locals() and conn.is_connected():
                    my_cursor.close()
                    conn.close()

      


      
if __name__=="__main__":
    root=Tk()
    obj=assignment(root)
    root.mainloop()
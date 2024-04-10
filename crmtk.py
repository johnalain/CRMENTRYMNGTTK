#https://youtu.be/G9seoA3Mv4Y?list=PLlvFEn0NKwXKydxD7jmZGiGNMloiI7nI1
from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('CRM Project')
root.iconbitmap('/Users/michelkadi/Desktop/icons/butter_toast_2sc_icon.ico')
root.geometry('1000x500')
# do some database stuff
#create database or connect to database exists
conn = sqlite3.connect('tree_crm.db')
#create a cursor instance
c = conn.cursor()
#create table
c.execute("""CREATE TABLE IF not exists customers(
first_name text,
last_name text,
id integer,
address text,
city text,
state text,
zipcode text)
""")
#add dummy data
data=[['john','alain',1,'123 saida St.','saida','south',12345],
      ['michel','alain',2,'123 beirut St.','beirut','mont-liban',14545],
      ['rita','kadi',3,'123 saida St.','beirut','beirut',1234],
      ['josephine','kadi',4,'123 saida St.','saida','south',12345],
      ['georges','kadi',5,'123 douma St.','douma','akkar',2345],
      ['karim','safadi',6,'224 tripoli St.','tripoli','north',345],
      ['john','alain',1,'123 saida St.','saida','south',12345],
      ['michel','alain',2,'123 beirut St.','beirut','mont-liban',14545],
      ['rita','kadi',3,'123 saida St.','beirut','beirut',1234],
      ['josephine','kadi',4,'123 saida St.','saida','south',12345],
      ['georges','kadi',5,'123 douma St.','douma','akkar',2345],
      ['karim','safadi',6,'224 tripoli St.','tripoli','north',345]]

for record in data:
    c.execute('INSERT INTO customers VALUES (:first_name,:last_name,:id,:address,:state,:city,:zipcode)',
              {'first_name':record[0],
               'last_name':record[1],
               'id':record[2],
               'address':record[3],
               'state':record[4],
               'city':record[5],
               'zipcode':record[6]}
)
    conn.commit()
    # conn.close()
def query_database():
  conn = sqlite3.connect('tree_crm.db')
  c=conn.cursor()
  c.execute('SELECT * FROM customers ')
  records = c.fetchall()
  print(records)
    

    

#commit changes
conn.commit()
#close
# conn.close()




#add some style
style=ttk.Style()
#add a theme
style.theme_use('default')
#configure the treeview colors
style.configure('treeview',
                background='#d3d3d3',
                foreground='black',
                rowheight=25,
                fieldbackground='#d3d3d3')
#change selected colorr
#https://youtu.be/G9seoA3Mv4Y?list=PLlvFEn0NKwXKydxD7jmZGiGNMloiI7nI1&t=134
style.map('treeview',
          background=[('selected','#347083')])
#-----create treeview frame----
tree_frame = Frame(root)
tree_frame.pack(pady=10)
#create a treeview Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)
#----create the treeview ----
my_tree = ttk.Treeview(tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode='extended')
my_tree.pack()
#----configure the scrollbar ----
tree_scroll.config(command=my_tree.yview)
#----define our columns ---
my_tree['columns']=("First name", "Last name",'ID', 'Address','City','State','Zipcode')
#----format our columns ---
my_tree.column("#0",width=0,stretch=NO)
my_tree.column("First name",anchor=W,width=140)
my_tree.column("Last name",anchor=W,width=140)
my_tree.column("ID",anchor=CENTER,width=100)
my_tree.column("Address",anchor=CENTER,width=140)
my_tree.column("City",anchor=CENTER,width=140)
my_tree.column("State",anchor=CENTER,width=140)
my_tree.column("Zipcode",anchor=CENTER,width=140)

#-------create headings---
#https://youtu.be/G9seoA3Mv4Y?list=PLlvFEn0NKwXKydxD7jmZGiGNMloiI7nI1&t=695
my_tree.heading("#0",text="",anchor=W)
my_tree.heading("First name",text="First name",anchor=W)
my_tree.heading("Last name",text="Last name",anchor=W)
my_tree.heading("ID",text="ID",anchor=CENTER)
my_tree.heading("Address",text="Address",anchor=CENTER)
my_tree.heading("City",text="City",anchor=CENTER)
my_tree.heading("State",text="State",anchor=CENTER)
my_tree.heading("Zipcode",text="Zipcode",anchor=CENTER)

#--------add fake data----------

#------create stripped row tags---------
my_tree.tag_configure('oddrow',background='white')
my_tree.tag_configure('evenrow',background='lightblue')
#------add our data to the screen----
global count
count = 0
for record in data:
    if count % 2 == 0:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('evenrow',))
        
    else:
        my_tree.insert(parent='',index='end',iid=count,text='',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]),tags=('oddrow',))
#-------increment counter---------
    count+=1 
#-------add record entry boxes--------- 
data_frame = LabelFrame(root,text='Record')
data_frame.pack(fill='x',expand='yes',padx=20)

fn_label = Label(data_frame,text='First name')
fn_label.grid(row=0,column=0,padx=10,pady=10)
fn_entry = Entry(data_frame)
fn_entry.grid(row=0,column=1,padx=10,pady=10)

ln_label = Label(data_frame,text='Last name')
ln_label.grid(row=0,column=2,padx=10,pady=10)
ln_entry = Entry(data_frame)
ln_entry.grid(row=0,column=3,padx=10,pady=10)

id_label = Label(data_frame,text='ID')
id_label.grid(row=0,column=4,padx=10,pady=10)
id_entry = Entry(data_frame)
id_entry.grid(row=0,column=5,padx=10,pady=10)

address_label = Label(data_frame,text='Address')
address_label.grid(row=1,column=0,padx=10,pady=10)
address_entry = Entry(data_frame)
address_entry.grid(row=1,column=1,padx=10,pady=10)

city_label = Label(data_frame,text='City')
city_label.grid(row=1,column=2,padx=10,pady=10)
city_entry = Entry(data_frame)
city_entry.grid(row=1,column=3,padx=10,pady=10)

state_label = Label(data_frame,text='State')
state_label.grid(row=1,column=4,padx=10,pady=10)
state_entry = Entry(data_frame)
state_entry.grid(row=1,column=5,padx=10,pady=10)

zipcode_label = Label(data_frame,text='Zipcode')
zipcode_label.grid(row=1,column=6,padx=10,pady=10)
zipcode_entry = Entry(data_frame)
zipcode_entry.grid(row=1,column=7,padx=10,pady=10)
#-----move row up---
def up():
     rows=my_tree.selection()
     for row in rows:
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)-1)
#-----move row down -----
def down():
    rows=my_tree.selection()
    for row in reversed(rows):
        my_tree.move(row,my_tree.parent(row),my_tree.index(row)+1)
#----remove one record-----
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
#----remove manu record-----
def remove_many():
    x = my_tree.selection()
    for record in x:
        my_tree.delete(record)
#----remove all records----
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
    

    

    
        
#------select record-----
#------clear entry boxes-----
def clear_entries():
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zipcode_entry.delete(0,END)
    
def select_record(e):
    #clear entry boxes
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zipcode_entry.delete(0,END)
    #grab record number
    selected = my_tree.focus()
    #grab record value
    values =my_tree.item(selected,'values')
    #output to entry boxes
    fn_entry.insert(0,values[0])
    ln_entry.insert(0,values[1])
    id_entry.insert(0,values[2])
    address_entry.insert(0,values[3])
    city_entry.insert(0,values[4])
    state_entry.insert(0,values[5])
    zipcode_entry.insert(0,values[6])
 #---update records
def update_record():
    #grab record number
    selected= my_tree.focus()
    #update record
    my_tree.item(selected,text='',values=(fn_entry.get(),ln_entry.get(),
            id_entry.get(),address_entry.get(),city_entry.get(),
            state_entry.get(),zipcode_entry.get,))
    fn_entry.delete(0,END)
    ln_entry.delete(0,END)
    id_entry.delete(0,END)
    address_entry.delete(0,END)
    city_entry.delete(0,END)
    state_entry.delete(0,END)
    zipcode_entry.delete(0,END)
    
       

#-----add buttons-------
button_frame = LabelFrame(root,text='commands')
button_frame.pack(fill='x',expand='yes',padx=20)

update_button = Button(button_frame,text='Update record',command=update_record)
update_button.grid(row=0,column=0,padx=10,pady=10)

add_button = Button(button_frame,text='Add record')
add_button.grid(row=0,column=1,padx=10,pady=10)

remove_all_button = Button(button_frame,text='Remove all record',command=remove_all)
remove_all_button.grid(row=0,column=2,padx=10,pady=10)

remove_one_button = Button(button_frame,text='Remove one selected',command=remove_one)
remove_one_button.grid(row=0,column=3,padx=10,pady=10)

remove_many_button = Button(button_frame,text='Remove many selected',command=remove_many)
remove_many_button.grid(row=0,column=4,padx=10,pady=10)

move_up_button = Button(button_frame,text='Move Up',command=up)
move_up_button.grid(row=0,column=5,padx=10,pady=10)

move_down_button = Button(button_frame,text='Move Down',command=down)
move_down_button.grid(row=0,column=6,padx=10,pady=10)

select_record_button = Button(button_frame,text='clear entry boxes',command=clear_entries)
select_record_button.grid(row=0,column=7,padx=10,pady=10)
#bind the treeview
#https://youtu.be/I9gQurGuqSI?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV&t=432

my_tree.bind('<ButtonRelease -1>',select_record)
query_database()


root.mainloop()
#https://youtu.be/I9gQurGuqSI?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV video173 continue
#https://youtu.be/pSXlKihUTlU?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV continue video 174 add database
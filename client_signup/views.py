from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def clientsignupaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Manikanta@1909",database='website')
        Cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value    
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value            
        c=f"insert into clientsignup values('{fn}','{ln}','{s}','{em}','{pwd}')"
        Cursor.execute(c)
        m.commit()
    return render(request,'client_signup.html')
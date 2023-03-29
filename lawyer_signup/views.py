from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''

# Create your views here.
def lawyersignupaction(request):
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
        c=f"insert into lawyersignup values('{fn}','{ln}','{s}','{em}','{pwd}')"
        d=f"insert into lawyerprofile values('{em}','{fn}','{ln}','{s}','',0,'','','00:00:00','00:00:00','','')"
        Cursor.execute(d)
        Cursor.execute(c)
        m.commit()
    return render(request,'lawyer_signup.html')
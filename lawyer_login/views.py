from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''

# Create your views here.
def lawyerloginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Manikanta@1909",database='website')
        Cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value            
        c=f"select * from lawyersignup where Email_Id='{em}' and Password='{pwd}'"
        Cursor.execute(c)
        t=tuple(Cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            data=t[0]
            return render(request,"lawyer_profile.html",context={"firstname":data[0],"lastname":data[1],"email":data[3]})
    return render(request,"lawyer_login.html")
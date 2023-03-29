from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
loc=''
data=''

# Create your views here.
def clientloginaction(request):
    global em,pwd,loc
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Manikanta@1909",database='website')
        Cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="location":
                loc=value            
        c=f"select * from lawyerprofile where Location Like '%{loc}%'"
        Cursor.execute(c)
        t=tuple(Cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            data=t
            print(data)
            return render(request,"client_home.html",context={"data":data})

    return render(request,'client_login.html')
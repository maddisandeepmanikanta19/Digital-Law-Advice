from sqlite3 import Cursor
from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
pn=''
exp=''
expc=''
loc=''
offoptime=''
offcltime=''
minfee=''
addr=''

# Create your views here.
def lawyerprofileaction(request):
    global fn,ln,s,pn,exp,expc,loc,offoptime,offcltime,minfee,addr
    print(request.GET)
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Manikanta@1909",database='website')
        Cursor=m.cursor()
        print("inside POST")
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
        print(d)
        c=f"select * from lawyerprofile where Email_Id='{em}'"
        Cursor.execute(c)
        t=tuple(Cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            data=t[0]
            print(data)
            return render(request,"lawyer_profile.html",context={"email":data[0],"first_name":data[1],"last_name":data[2],"sex":data[3],"phonenumber":data[4],"experience":data[5],"expert_in_cases":data[6],"location":data[7],"office_opening_time":data[8],"office_closing_time":data[9],"minimumfee":data[10],"address":data[11]})
    return render(request,"lawyer_profile.html")
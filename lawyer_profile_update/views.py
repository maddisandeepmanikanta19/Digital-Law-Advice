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
def lawyerprofileupdate(request):
    global fn,ln,s,pn,exp,expc,loc,offoptime,offcltime,minfee,addr
    print(request.POST)
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="Manikanta@1909",database='website')
        Cursor=m.cursor()
        d=request.POST
        print(d)
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value    
            if key=="email":
                em=value    
            if key=="sex":
                s=value
            if key=="phonenumber":
                pn=value
            if key=="Experience":
                exp=value
            if key=="Expert in Cases":
                expc=value            
            if key=="LOCATION":
                loc=value            
            if key=="OfficeopenTiming":
                offoptime=value  
            if key=="OfficecloseTiming":
                offcltime=value              
            if key=="MinimumFee":
                minfee=value 
            if key=="address":
                addr=value          
        print(d)                                          
        c=f"update lawyerprofile set Fisrt_Name='{fn}', Last_Name='{ln}', sex='{s}',phonenumber='{pn}',Expert_in_cases='{expc}',Location='{loc}',Office_open_Timings='{offoptime}',Office_close_Timings='{offcltime}',MinimumFee='{minfee}',Address='{addr}',Experience={exp} where Email_Id='{em}'"
        print(c)
        Cursor.execute(c)
        m.commit()
        return render(request,'lawyer_profile_update.html',context={"email":em,"first_name":fn,"last_name":ln,"sex":s,"phonenumber":pn,"experience":exp,"expert_in_cases":expc,"location":loc,"office_opening_time":offoptime,"office_closing_time":offcltime,"minimumfee":minfee,"address":addr})
    return render(request,'lawyer_profile.html')
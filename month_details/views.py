from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from . models import MonthDetails

def month(request):
    # if(request.method=='POST'):
    # months=[]
    monthnames=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
    # for i in range(len(monthnames)):
    #     monname='month'+str(i)
    #     monname=MonthsDummy()
    #     monname.monthname=monthnames[i]
    #     months.append(monname)
    return render(request,"home.html",{'monthnames':monthnames})

def monthname(request,monthname):
    return render(request,"blockmonths.html",{"monthname":monthname})
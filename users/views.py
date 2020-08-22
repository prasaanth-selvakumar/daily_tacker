from django.shortcuts import render,redirect
from django.http import HttpResponse
from users.forms import EmpIdForm
# Create your views here.
def logout_view(request):
    logout(request)
    return render(request,"registration/logout.html")
def index(request):
    if(request.user.is_authenticated):
        if(request.user.emp_id==""):
            return redirect('add_emp')
            #return HttpResponse("The guys doesn't have an emp_id")
    return render(request,'auth_user/index.html')
def add_emp(request):
    if(request.method=="POST"):
        form = EmpIdForm(request.POST);
        if form.is_valid():
            form.save(commit=False)
            emp_id = form.cleaned_data["emp_id"]
            #emp_id=request.user.objects.add_emp(emp_id)
            request.user.emp_id=emp_id
            request.user.save()
            return redirect('index')
        else:
            return HttpResponse("Hello World")
    else:
        context ={}
        context['form']= EmpIdForm()
        return render(request, "registration/emp_id.html", context)

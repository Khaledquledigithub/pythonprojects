from django.shortcuts import render,redirect
from iapp.models import User,Email,Address,Propic
from iapp.forms import UserForm,AddressForm,EmailForm,PasswordForm,Confirm_PasswordForm,Profil_PicForm,logform
# Create your views here.

def home_view(request):
	u=User.objects.all()
	e=Email.objects.all()
	a=Address.objects.all()
	return render(request,"iapp/home.html",{"u":u,"e":e,"a":a})

def form_view(request):
	form1=UserForm()
	if request.method=="POST":
		form1=UserForm(request.POST)
		form1.save()
	return render(request,"iapp/form.html",{"form1":form1})
def eform_view(request):
	form2=EmailForm()
	if request.method=="POST":
		form2=EmailForm(request.POST)
		if form2.is_valid():
			form2.save()
	return render(request,"iapp/eform.html",{"form2":form2})
def pform_view(request):
	form3=PasswordForm()
	if request.method=="POST":
		form3=PasswordForm(request.POST)
		form3.save()
	return render(request,"iapp/pform.html",{"form3":form3})
def cform_view(request):
	form4=Confirm_PasswordForm()
	if request.method=="POST":
		form4=Confirm_PasswordForm(request.POST)
		form4.save()
	return render(request,"iapp/conform.html",{"form4":form4})
def aform_view(request):
	form5=AddressForm()
	if request.method=="POST":
		form5=AddressForm(request.POST)
		form5.save()
	return render(request,"iapp/aform.html",{"form5":form5})
def piform_view(request):
	form6=Profil_PicForm()
	if request.method=="POST":
		form6=Profil_PicForm(request.POST)
		if form6.is_valid():
			form6.save()
	return render(request,"iapp/pic.html",{"form6":form6})


def up_view(request,id):
	u=User.objects.get(id=id)
	if request.method=="POST":
		form1=UserForm(request.POST, instance=u)
		if form1.is_valid():
			form1.save()
		return redirect("/profile")
	return render(request,"iapp/u_user.html",{"u":u})


def upe_view(request,id):
	e=Email.objects.get(id=id)
	if request.method=="POST":
		form2=EmailForm(request.POST, instance=e)
		if form2.is_valid():
			form2.save()
		return redirect("/profile")
	return render(request,"iapp/u_email.html",{"e":e})

def upa_view(request,id):
	a=Address.objects.get(id=id)
	if request.method=="POST":
		form3=AddressForm(request.POST, instance=a)
		if form3.is_valid():
			form3.save()
		return redirect("/profile")
	return render(request,"iapp/u_address.html",{"a":a})



def del_user(request,id):
	u=User.objects.get(id=id)
	u.delete()
	return redirect("/profile")
def del_email(request,id):
	e=Email.objects.get(id=id)
	e.delete()
	return redirect("/profile")
def del_add(request,id):
	a=Address.objects.get(id=id)
	a.delete()
	return redirect("/profile")
def logview(request):
	form=logform()
	return render(request,"iapp/log.html",{"form":form})

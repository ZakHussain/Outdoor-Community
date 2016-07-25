from django.shortcuts import render, redirect
from models import User


# Create your views here.
def index(request):
	print "INDEX WorKing!!"
	return render(request,'login_and_register/index.html')

def login(request):
	print "LOGIN Working!!"
	email=request.POST['emailLogin']
	password=request.POST['passwordLogin']

	# ucheck=User.userManager.filter(email = email)
	# print u[0].email
	u=User.userManager.login(email,password)
	if u[0]==False:
		context = {
			"message": u[1]
		}
		return render(request,'login_and_register/index.html',context)
	elif u[0]==True:
		context = {
			"message":u[1],
			"firstName":u[2],
			"lastName":u[3],
			"email":u[4],
			"created_at":u[5],
			"Users": User.objects.all() 
		}
		return render(request,'login_and_register/result.html',context)
	else:
		return render(request,'login_and_register/index.html')

def result(request):
	firstName=request.POST['firstName']
	lastName=request.POST['lastName']
	email=request.POST['email']
	password=request.POST['password']
	confirmPassword=request.POST['confirmPassword']
	u=User.userManager.registration(firstName,lastName,email,password,confirmPassword)
	if u[0]==False:
		context = {
			"message": u[1]
		}
		return render(request,'login_and_register/index.html',context)
	else:
		context = {
			"message":u[1],
			"firstName":u[2],
			"lastName":u[3],
			"email":u[4],
			"created_at":u[5],
			"Users": User.objects.all() 
		}
	return render(request,'login_and_register/result.html',context)

def deleteFinal(request, id):
	User.objects.get(id=id).delete()
	context = {
			"Users": User.objects.all() 
		}
	return render(request, 'login_and_register/result.html',context)


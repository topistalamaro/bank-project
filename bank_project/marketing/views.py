from django.shortcuts import  render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from .forms import NewUserForm
from django.contrib.auth import logout
from django.contrib import messages

from django.contrib.auth import authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
# import the login_required decorator and the LoginRequiredMixin mixin below
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Customer

# Import the logout function from django.contrib.auth below



from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from . forms import NewUserForm

import pickle


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return render(request, 'marketing/login.html')
    else:
        form = NewUserForm()

    return render(request, 'registration/signup.html', {'form': form})
def logout_request(request):
  logout(request)
  return redirect("index")


def index(request):
    context = {'prediction':None}
    if request.method == 'POST':
        
        age = int(request.POST['age'])
        default = int(request.POST['default'])
        balance = int(request.POST['balance'])
        duration = int(request.POST['duration'])
        campaign = int(request.POST['campaign'])
        pdays = int(request.POST['pdays'])
        previous = int(request.POST['previous'])
        user_input = [2, age, default, balance, duration, campaign, pdays, previous]
        print(user_input)
        prediction = getPredictions(user_input)

        context = {'prediction':prediction}
        return render(request, 'marketing/prediction.html', context)
    return render(request, 'marketing/index.html', context)

# custom method for generating predictions
def getPredictions(user_input):
    model = pickle.load(open("marketing/bank_marketing_ml_model.sav", "rb"))
    scaled = pickle.load(open("marketing/scaler.sav", "rb"))
    prediction = model.predict(scaled.transform([user_input]))
    
    if prediction == 0:
        return "No"
    elif prediction == 1:
        return "Yes"
    else:
        return "error"
        
# Create your class-based Signup view below:


# def login_request(request):

#     form=AuthenticationForm()
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect("home")
#         else:
#             messages.error(request,"Invalid username or password.")
#         return render(request=request, template_name="registration/login.html", context={"login_form":form})

        
		#form = AuthenticationForm(request, data=request.POST)
		#if form.is_valid():

		
		
			
				# messages.info(request, f"You are now logged in as {username}.")
			
			# else:
			# 	messages.error(request,"Invalid username or password.")
		
			
	
	

# Create your logout function, logout_request, below:


  
# our result page view
def result(request):
    
    cum =Customer.objects.all()
    

    return render(request, 'marketing/results.html', {'cum':cum})

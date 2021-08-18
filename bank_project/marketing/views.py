from django.shortcuts import  render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth import logout

from django.contrib.auth import authenticate #add this
from django.contrib.auth.forms import AuthenticationForm #add this
# import the login_required decorator and the LoginRequiredMixin mixin below
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
import pickle


# Create your class-based Signup view below:
class SignUp(CreateView):
  form_class = UserCreationForm
  success_url = reverse_lazy("login")
  template_name = "registration/signup.html"


def index(request):
    context = {'prediction':""}
    if request.method == 'POST':
        
        age = int(request.POST.get('age'))
        default = int(request.POST.get('default'))
        balance = int(request.POST.get('balance'))
        duration = int(request.POST.get('duration'))
        campaign = int(request.POST.get('campaign'))
        pdays = int(request.POST.get('pdays'))
        previous = int(request.POST.get('previous'))

        user_input = [2, age, default, balance, duration, campaign, pdays, previous]

        model = pickle.load(open("marketing/bank_marketing_ml_model.sav", "rb"))
        scaled = pickle.load(open("marketing/scaler.sav", "rb"))
        prediction = model.predict(scaled.transform([user_input]))

        new_input = Customer(
            age = age, 
            default = default, 
            balance = balance, 
            duration = duration, 
            campaign = campaign, 
            pdays = pdays, 
            previous = previous,
            y = prediction,
        )
        new_input.save()
        if prediction == 0:
            context = "No"
        elif prediction == 1:
            context = "Yes"
        else:
            context = "error"

        return render(request, 'marketing/prediction.html', {'prediction':context})
    return render(request, 'marketing/index.html', context)

# our result page view
@login_required
def result(request):
    cum =Customer.objects.all()
    return render(request, 'marketing/results.html', {'cum':cum})

# Create your logout function, logout_request, below:
def logout_request(request):
  logout(request)
  return redirect("index")

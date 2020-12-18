from django.shortcuts import render, redirect
from django.views import View
from .models import Customer
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
class Index(View):
    def get(self, request):
        return render(request, 'index.html')

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        
        isExists = customer.isExists()
        if isExists:
            error_message = 'This Email Already Register'
            return render(request, 'signup.html', {'error' : error_message})
        else:
            customer.password = make_password(customer.password)
            customer.register()
            return render(request, 'login.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = 'Email or Password Invalid !!'
        else:
            error_message = 'Email or Password Invalid !!'
        
        print(email, password)
        return render(request, 'login.html', {'error': error_message})

class Logout(View):
    def get(self, request):
        request.session.clear()
        return redirect('login')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_reset/change_password.html', {
        'form': form
    })


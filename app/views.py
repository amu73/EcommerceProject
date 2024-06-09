from django.shortcuts import render,redirect
from django.views import View
from . models import Product, Customer
from django.db.models import Count
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm, CustomerProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return render(request,"app/home.html")

def about(request):
    return render(request,"app/about.html")

def contact(request):
    return render(request,"app/contact.html")

# using class for render heree
class CategoryView(View):
    # get method for displaying the products
    def get(self, request, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title').annotate(total=Count('title'))
        return render(request,'app/category.html',locals())
 
class CategoryTitle(View):
    def get(self,request, val):
        product = Product.objects.filter(title=val)
        title = Product.objects.filter(category=product[0].category).values('title')
        return render(request,"app/category.html",locals())

class ProductDetail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)

        return render(request,"app/productdetail.html",locals())


class CustomerRegistrationView(View):
    def get(self,request):
        form = RegisterForm()
        return render(request, 'app/register.html', locals())
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # message middlewares
            messages.success(request, "User registered successfully")
            # login(request, user)
            # return redirect('home')
        else:
            messages.warning(request,"Invalid input data")
        return render(request, 'app/register.html', locals())

# class LoginForm(AuthenticationForm):

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',locals())
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name'] 
            locality = form.cleaned_data['locality'] 
            city = form.cleaned_data['city'] 
            mobile = form.cleaned_data['mobile'] 
            state = form.cleaned_data['state'] 
            zipcode = form.cleaned_data['zipcode'] 
            reg = Customer(user=user,name=name,locality=locality,mobile=mobile,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request, "Profile save successfully")
          
        else:
            messages.warning(request,"Invalid input data")
        return render(request,'app/profile.html',locals())

def address(request):
    add = Customer.objects.filter(user = request.user)
    return render(request,'app/address.html',locals())

class UpdateAddress(View):
    def get(self,request,pk):
        form = CustomerProfileForm()
        return render(request,'app/updateAddress.html',locals())
    def post(self,request,pk):
        form=CustomerProfileForm(request.POST)
        return render(request,'app/updateAddress.html',locals())
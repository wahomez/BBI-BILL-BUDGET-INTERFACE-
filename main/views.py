from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm, ProfileForm, BudgetForm, BillForm
from .models import Profile, Budget, Bill

# Create your views here.
def Home(request):
    return render(request, "home.html")

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST, data=request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")

    form = AuthenticationForm
    context = {
        "form" : form
    }
    return render(request, "login.html", context)

def register_user(request):
    form = RegisterForm

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, email=user.email, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect("/")
            
    context = {
        "form" : form
    }
    return render(request, "register.html", context)

def logout_user(request):
    logout(request)
    return redirect("/login")

def profile_page(request, pk):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("/")


    form = ProfileForm

    context = {
        "form" : form
    }
    return render(request, "profile.html", context)

def profile_form(request, pk):
    profile = Profile.objects.get(user=pk)
    if request.method == 'POST' or request.method == "FILES":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("/")


    form = ProfileForm(instance=profile)

    context = {
        "form" : form, 
    }

    return render(request, "profile_form.html", context)

def budget_page(request, pk):
    budget = Budget.objects.filter(user=pk)

    context = {
        "budget" : budget
    }

    return render(request, "budget.html", context)

def budget_update(request, pk):
    budget = Budget.objects.get(id=pk)

    form = BudgetForm(instance=budget)

    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid:
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('/')

    context = {
        "form" : form
    }

    return render(request, "budget_update.html", context)

def budget_form(request):
    
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid:
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('/')

    form = BudgetForm
    context = {
        "form" : form
    }
    return render(request, "budget_form.html", context)

def delete_budget(request, pk):
    budget = Budget.objects.get(id=pk)
    budget.delete()
    return redirect("/")

def bill_page(request, pk):
    bill = Bill.objects.filter(user=pk)
    
    context = {
        "bills" : bill
    }
    return render(request, "bill.html", context)

def bill_form(request):
    if request.method == "POST":
        form = BillForm(request.POST)
        if form.is_valid:
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            return redirect("/")

    form = BillForm


    context = {
        "form" : form
    }
    return render(request, "bill_form.html", context)

def bill_update(request, pk):
    bill = Bill.objects.get(id=pk)

    form = BillForm(instance=bill)

    if request.method == "POST":
        form = BillForm(request.POST, instance=bill)
        if form.is_valid:
            bill = form.save(commit=False)
            bill.user = request.user
            bill.save()
            return redirect('/')

    context = {
        "form" : form
    }

    return render(request, "bill_update.html", context)

def bill_delete(request, pk):
    bill = Bill.objects.get(id=pk)
    bill.delete()
    return redirect("/")
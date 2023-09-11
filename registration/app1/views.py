from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import RIVUE
from django.http import HttpResponseForbidden
from .forms import RIVUEForm
# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    if request.method == "POST":
        form = RIVUEForm(request.POST, request.FILES)
        ProModel = request.POST['ProModel']
        ProName = request.POST['ProName']
        ProRev = request.POST['ProRev']
        ProEmail = request.POST['ProEmail']
        ProCom = request.POST['ProCom']
        data = RIVUE(ProModel=ProModel, ProName=ProName, ProRev=ProRev, ProEmail=ProEmail, ProCom= ProCom,user=request.user)
        data.save()
        if form.is_valid():
            form.instance.user = request.user  # Set the user from the request
            form.save()
            return redirect('show')
        return redirect('show')
    else:
        form=RIVUEForm()
    return render(request,'home.html')
    
def show_emp(request):
    Product = RIVUE.objects.all()
    return render(request,'show.html',{'Product':Product} )

def edit_emp(request, pk):
    product = RIVUE.objects.get(id=pk)
    if request.user != product.user:  # Adjust this based on your model structure
        return HttpResponseForbidden("You don't have permission to edit this entry.")

    if request.method == 'POST':
        product.ProModel = request.POST['ProModel']
        product.ProName = request.POST['ProName']
        product.ProRev = request.POST['ProRev']
        product.ProEmail = request.POST['ProEmail']
        product.ProCom = request.POST['ProCom']
        product.save()
        return redirect('show')

    context = {
        'Product': product,
    }

    return render(request, 'edit.html', context)

def LandingPage(request):
    return render(request,'index.html')

def remove_emp(request,pk):
    product = RIVUE.objects.get(id=pk)

    if request.user != product.user:
        return HttpResponseForbidden("You don't have permission to delete this entry.")

    if request.method == 'POST':
        product.delete()
        return redirect('show')

    context = {
        'product': product,
    }

    return render(request, 'delete.html', context)
    


def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        user = User.objects.create_user(uname, email, pass1)
        if pass1==pass2:
            return redirect('login')
        else:
            return HttpResponse("Your passwords do not match")
    return render(request,'signup.html')


def LoginPage(request):
    
    if request.method=='POST':
        username=request.POST.get('username')
        pass3=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass3)
        if user is not None:
            print("yes")
            login(request,user)
            print("yes")
            return redirect('home')
            
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('index')

from django.http import JsonResponse

def search_product(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        results = RIVUE.objects.filter(ProName__icontains=query)
        
        # Convert results to JSON and return
        data = [{'ProModel': result.ProModel, 'ProName': result.ProName} for result in results]
        return JsonResponse({'results': data})


def imageupload(request):
    if request.method == 'POST':
        form = RIVUEForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
            # Handle successful form submission
    else:
        form = RIVUEForm()
    return render(request, 'home.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')
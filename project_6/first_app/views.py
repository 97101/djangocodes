# first_app/views.py

from django.shortcuts import render
from . forms import contactForm
def home(request):
    return render(request, 'home.html')

def about(request):
    # Example of accessing query parameters
    id = request.GET.get('id')
    return render(request, 'index.html', {'id': id})

def submit_form(request):
    if request.method == 'POST':
        # Access form data
        name = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        print(email, password,)  # Output for debugging purposes
        # Process form data as needed
        return render(request, 'form.html', {'email': email,'name':name})
    else:
        return render(request, 'form.html')
    

def Djangoform(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            balance = form.cleaned_data['balance']
            file = request.FILES['file']  # Access the uploaded file
            with open('./first_app/upload/' + file.name,'wb+') as destinations:
                for chunck in file.chunks():
                    destinations.write(chunck)
            print(name, email, age, weight, balance, file.name)  # Output for debugging purposes

            # Process form data as needed (e.g., save to database)
            # Example: instance = MyModel(name=name, email=email, ...)
            # instance.save()

            return render(request, 'Django.html', {'form': form, 'name': name})
    else:
        form = contactForm()

    return render(request, 'Django.html', {'form': form})


   



from django.shortcuts import render,redirect
from .import forms
def add_profile(request):
    if request.method=='POST':
        profile_form=forms.profile_form(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("add_profile")
        
    else:
        profile_form=forms.profile_form()
    return render(request,'add_profile.html',{'form':
    profile_form})

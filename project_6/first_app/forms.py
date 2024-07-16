from django import forms

# widges==field to html input
class contactForm(forms.Form):
    name=forms.CharField(label="Full name: ",initial="Arif",help_text="Total lenght mustbe with in 70 characters",widget=forms.Textarea(attrs={'id':'text_area'}))
    file=forms.FileField()
    email=forms.EmailField()
    age=forms.IntegerField()
    weight=forms.FloatField()
    balance=forms.DecimalField()
    MEAL=[('p','peporoni'),('M','Mashroom'),('B','BEEF')]
    pizza=forms.MultipleChoiceField(choices=MEAL)


from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm, SnipetForm


def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            # email=form.cleaned_data['email']
            # print(name)
            # print(email)
    form = ContactForm();
    return render(request, "core/forms.html", {'form':form})

def snipet_detail(request):
    if request.method=='POST':
        form = SnipetForm(request.POST)
        if form.is_valid():
            form.save()
    form = SnipetForm();
    return render(request, "core/forms.html", {'form':form})
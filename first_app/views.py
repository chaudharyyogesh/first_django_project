from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    # webpages_list=AccessRecord.objects.order_by('date')
    # date_dict = {'access_records':webpages_list}
    # # my_dict = {'insert_me': "Hello i am from views.py!"}
    # return render(request,'first_app/index.html',context=date_dict)
    return render(request,'first_app/index.html')

def form_name_view(request):
    form=forms.FormName()

    if request.method == 'POST':
        form=forms.FormName(request.POST)

        if form.is_valid():
            #do something
            print("validation success")
            print("name:"+form.cleaned_data['name'])
            print("email:"+form.cleaned_data['email'])
            print("text:"+form.cleaned_data['text'])

    return render(request,'first_app/form_page.html',{'form':form})
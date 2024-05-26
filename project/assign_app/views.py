from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .analyzer import analyze_image
from django.http import HttpResponse
from .models import *


# Create your views here.

context = {}
country_list = CountryModel.objects.all()
# document_list = DocumentSetModel.objects.all()
index_html = 'index.html'
login_html = 'auth/login.html'
document_html = 'document_form.html'



def index(request):
    # return HttpResponse("<h1> Hello Python </h1>")
    return render(request,login_html,{})


def main_page(request):
    user = UserModel.objects.get(Email = request.session["email"])
      
    document_set = DocumentSetModel.objects.all().filter(Country=  request.POST.get('country_select'))
    back_document_filter = DocumentSetModel.objects.all().filter(Name_of_document=  request.POST.get('document_flter'),Country=  request.POST.get('country_select'))

    context['session_id'] = user 
    context['country_list'] = country_list
    context['document_filter'] = document_set
    context['back_show'] = back_document_filter

    print(request.POST.get('country_select'))  
     
    return render(request, index_html,context)

def login(request):
    try:
        user = UserModel.objects.get(Email = request.POST.get('email'))
        if user.Password == request.POST['password']:
            request.session["email"] = user.Email
            return redirect(main_page)
        else:
            return HttpResponse('incorrect password')
                
    except UserModel.DoesNotExist as err:
        print(err)

    return redirect(index)



def logout(request):
    if 'email' in request.session:
        del request.session["email"]
    return redirect(index)


# functions
def upload_and_analyze_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # Analyze the image using the Vision API
        labels = analyze_image(fs.path(filename))

        return redirect(request, 'document_form.html', {
            'uploaded_file_url': uploaded_file_url,
            'labels': labels
        })
    return render(request, 'upload.html')


   
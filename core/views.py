from django.shortcuts import render ,redirect
from .models import Portfolio, Project,Resume, SocialLink
from django.contrib import messages
from . forms import SocialForm

# Create your views here.

def home(request):
    homes = Portfolio.objects.all()
    projects = Project.objects.all()
    return render(request, 'index.html', {'homes': homes , 'projects': projects})

def about(request):
    pros = Portfolio.objects.all()
    resumes = Resume.objects.all()
    return render (request, 'about.html', {'resumes': resumes , 'pros': pros})
def project(request):
    projs = Project.objects.all()
    return render(request, 'project.html', {'projs': projs})
def contact(request):
    links = SocialLink.objects.all()
    
    if request.method == 'POST':
        form = SocialForm(request.POST, request.FILES)
        if form.is_valid():
           form.save()
           form =  messages.success(request, "Your message has been sent successfully!")
           return redirect('contact')
        
          
    else:
            form = SocialForm()
    
            return render(request, 'contact.html', {'links': links, 'form': form})











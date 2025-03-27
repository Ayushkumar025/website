from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import os


def index(request):
    return HttpResponse("Welcome Himanshu !")

def home(request):    
    return render(request, 'home.html')


def aipage(request):   
    print("ai called") 
    return render(request, 'aipage.html')

def fullstack(request):    
    return render(request, 'fullstack.html')

def trading(request):
    return render(request,'trading.html')

def free(request):
    return render(request,'free.html')

def erp(request):
    return render(request,'erp.html')

# storing form data 

def store(request):
    if request.method == 'POST':
        print('Form submitted!')  # Debug statement
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        form_data = f"Name: {name}\nEmail: {email}\nMessage: {message}\n\n"
        print(form_data)  # Debug statement
        
        file_name='record.txt'
        
        with open(file_name, 'a') as fh:
            fh.write(form_data)
        
        return render(request,'home.html')  # Redirect to home after form submission
    
    return HttpResponse("Invalid request", status=400)

def search(request):
    query = request.GET.get('query', '').lower()
    sections = {
        "contact": "footer",
        "project": "projects",
        "gallery": "navbar",
        "app": "projects",
        "website":"projects",
        "address":"footer",
        "number":"footer",
    }
    # Match the query to a section's ID
    target_id = sections.get(query, None)
    print(f"Query: {query}, Target ID: {target_id}")  # Debugging: Log to console

    return render(request, 'home.html', {'target_id': target_id})

def aisearch(request):
    query = request.GET.get('query', '').strip().lower()
    sections = {
        "machine": "ml",
        "machine learning": "ml",
        "language": "nlp",
        "computer vision": "cv",
        "computer": "cv",
        "technologies": "tech",
        "address":"footer",
        "number":"footer",
    }
    # Match the query to a section's ID
    target_id = sections.get(query, None)
    print(f"Query: {query}, Target ID: {target_id}")  # Debugging: Log to console

    if target_id:
        return render(request, 'aipage.html', {'target_id': target_id})
    else:
        return render(request, 'aipage.html', {'error': "No matching results."})
    
    
def fullsearch(request):
    query = request.GET.get('query', '').strip().lower()
    sections = {
        "frontend": "front",
        "backend":"back",
        "database" : "data",
        "address" : "footer",
        "number":"footer",
       
    }
    # Match the query to a section's ID
    target_id = sections.get(query, None)
    print(f"Query: {query}, Target ID: {target_id}")  # Debugging: Log to console

    if target_id:
        return render(request, 'fullstack.html', {'target_id': target_id})
    else:
        return render(request, 'fullstack.html', {'error': "No matching results."})
    
    
def tradesearch(request):
    query = request.GET.get('query', '').lower()
    sections = {
        "contact": "footer",
        "gallery": "navbar",
        "address":"footer",
        "number":"footer",
    }
    target_id = sections.get(query, None)
    print(f"Query: {query}, Target ID: {target_id}")  # Debugging: Log to console

    if target_id:
        return render(request, 'trading.html', {'target_id': target_id})
    else:
        return render(request, 'trading.html', {'error': "No matching results."})
    
    

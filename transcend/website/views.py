from turtle import setundobuffer
from django.core.mail import send_mail
from django.shortcuts import  render, redirect
from matplotlib.style import context
from .forms import NewUserForm, GenomeForm
from .models import Genome

from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from helpers.my_genome_analyze import *



#from .my_genome_analyze.py import' import *
#get data from the class
#try to run the function
#if you run then pass it to the page
#Display it on the tables

# Create your views here.
def home(request):
    return render(request, 'Home.html', {})

def about(request):
    return render(request, 'About.html', {})

def preferences(request):
    #Get the pref of the past based on match or offspring

    return render(request, 'Preferences.html', {})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            print("success")
            return render(request, 'Home.html', {})

            # messages.success(request, "Regisration successful.")
            # print("hello")
            return render(request, "Home.html")
        else:
            print(form.errors)
            return render(request, 'Register.html', {'form': form, 'errorsman':form.errors})

    form = NewUserForm()
    return render(request, 'Register.html', context={"form":form})

def login(request):
    #If posted then log into session
    return render(request, 'Login.html', {})


def myDNA(request):
    myDNA = Genome.objects.all()
    blake_young = myDNA[len(myDNA)-1].genome
    df = trim_genome(blake_young)
    result = analyze_my_DNA(df)
    #print("result is", result)
    return render(request, 'My-DNA.html', {
        'myDNA': myDNA,
        'analysis': result
    })
    #If nothing then go to log in



    #Get the data of the user from the database
    #If no data then go to upload

    #Else
        #Pass the genome to the html

    #If the user presses preferences then go there



def offspringDNA(request):
    #Given the genome
    #Instantiate profile
    #For trait in traits:
        #Get the first trait allele:
        #Return punnet sqaure as latex
        #Add latex file to profil trait
        #Display profile in a table
 
    return render(request, 'Offspring-DNA.html', {})

def upload(request):
    context = {}
    if request.method == 'POST':
        form = GenomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'my-DNA.html')
        else:
            form = GenomeForm()

        #  uploaded_file = request.FILES['document']
        #  fs = FileSystemStorage()
        #  name = fs.save(uploaded_file.name, uploaded_file)
        #  context['url'] = fs.url(name)
        # #Get the data submitted
        # #Analyze it
        # #Save analysis to a genome
        # #Upload the table

    form = GenomeForm()
    return render(request, 'Upload.html', {
        'form': form
    })

def mateDNA(request):
    # if request.method == 'POST':
    #     genomes = Genome.objects.get(pk=pk)
    #Get preferences

    #If save
    #Pass the preferences into the program


    #If run
    #Gather all panda genomes from the database
    #Pass them to matchDNA.py

    #Inside the py file
    #For genome in genomes:
        #For traits in genome:
            #   search for relevant trait RSID
            #   search for allele at that RSID
            #   Give that genome one more point based on preferences of trait ex genome.points= genome.points + 1(trait.value)
            #reuturn genomes to html file as genomes

    #For genome in genomes:
    #If the genome.points >1:
        #Build the HTML

    #If they post that they want the offspring
    #return offspring-DNA(genome:genome)

    return render(request, 'Mate-DNA.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']
        # send an email

        send_mail(
           message_name , #Subject
           message, #Message
           message_email, #from email
           ['blake_young@college.harvard.edu'], # To email
        )


        return render(request, 'Contact.html', {'message_name = message-name'})

    else:
        return render(request, 'Contact.html', {})
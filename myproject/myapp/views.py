from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Feature

# Create your views here.


def index(request):
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'Our service is very quick'

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true = True
    # feature2.details = 'Our service is very reliable'

    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to Use'
    # feature3.is_true = False
    # feature3.details = 'Our service is very easy to use'

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true = True
    # feature4.details = 'Our service is very affordable'

    # features = [feature1, feature2, feature3, feature4]
    # context = {
    #     'name': 'John',
    #     'age': 20,
    #     'nationality': 'Nigerian'
    # }

    features = Feature.objects.all()

    return render(request, 'index.html', {'features': features})


def counter(request):
    # text = request.POST['text']
    # total_count_words = len(text.split(' '))
    posts = [1, 2, 3, 4, 5, 'tim', 'tom', 'john', 'jane', 'james', 'jessica']
    return render(request, 'counter.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        uname = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['confirmation']

        if password == password2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=uname, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

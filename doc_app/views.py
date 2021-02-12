from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from doc_app.models import Document, Attributes
from doc_app.forms import LoginForm, AddUserForm, AddDocumentForm, AddAttributeForm


# Create your views here.


class WelcomeView(View):
    def get(self, request):
        return render(request, 'views/welcome.html')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'forms/login_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return HttpResponse('Logging error')


class LogutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = AddUserForm()
        return render(request, 'forms/add_user_form.html', {'form': form})

    def post(self, request):
        form = AddUserForm(request.POST)
        if form.is_valid():
            login_user = form.cleaned_data['login']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            User.objects.create_user(username=login_user,
                                     email=email,
                                     password=password,
                                     first_name=first_name,
                                     last_name=last_name)
            return redirect('/')
        else:
            return render(request, 'forms/add_user_form.html', {'form': form})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        user = User.objects.get(id=request.user.id)
        documents = Document.objects.filter(user=user.id)
        return render(request, 'views/dashboard.html', {'documents': documents})


class DocumentCreateView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddDocumentForm()
        return render(request, 'forms/add_document_form.html', {'form': form})

    def post(self, request):
        form = AddDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = Document(
                name=request.POST['name'],
                path=request.FILES['path'],
                user=request.user)
            document.save()

            return redirect('dashboard')
        else:
            return render(request, 'forms/add_document_form.html', {'form': form})


class DocumentView(View):

    def get(self, request, document_id):
        document = Document.objects.get(id=document_id)
        return render(request, 'views/document-view.html', {'document': document})


class AttributesCreateView(View):

    def get(self, request):
        form = AddAttributeForm()
        return render(request, 'forms/add_attributes_form.html')

    def post(self, request):
        form = AddAttributeForm(request.POST)
        if form.is_valid():
            pass

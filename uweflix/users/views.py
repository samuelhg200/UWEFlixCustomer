from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, get_user_model
from django.forms import ModelForm
from users.models import Showing

def index(request):
    return HttpResponse("Hello, world. You're at the users index.")

class UserCreationForm(ModelForm):
 
    class Meta:
        model = User
        fields = ('username',)

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'users/register.html', {'userForm': form, 'nbar': 'registration'})

def getUsers(request):
    User = get_user_model()
    users = User.objects.values()
    return render(
        request,
        'users/retrieveUsers.html',
        {'users': users, 'nbar': 'retrieve'}
    )

def deleteUsers(request, username = ""):
    if username != "":
        User = get_user_model()
        userToDelete = User.objects.get(username = username)
        userToDelete.delete()
    

    return redirect('retrieve users')

class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ('username',)


def editUsers(request, username):
    form = UserChangeForm()

    User = get_user_model()
    users = User.objects.values()
    userToEdit = User.objects.get(username = username)

    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance = userToEdit)
        if form.is_valid():
            form.save()
            return redirect('retrieve users')
        else:
            users = User.objects.get(username = username)
            form = UserChangeForm(instance=userToEdit)

    return render(
        request,
        'users/editUser.html',
        {'users': users, 'nbar': 'retrieve', 'userForm': form}
    )

def viewShowing(request):
    showing = Showing(title="Avatar: The Way of Water", age_rating=16, duration="192 minutes", description="The awaited sequel to the second avatar film. One of the most awaited films of the year. Directed and produced by James Cameron. Tells the story of a alien-like civilization that battles with the human species to find its place in the earth. Highly recommended by critics worldwide.")
    showing.save()
    
    return render(
        request,
        'users/showing.html',
        {'showing': showing, 'nbar': 'showing'}
    )


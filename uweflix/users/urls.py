from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registerUser, name="registration"),
    path('retrieveUserList/', views.getUsers, name="retrieve users"),
    path(r'^users/(?P<username>)/$', views.deleteUsers, name="delete_users"),
    path(r'retrieveUserList/edit/(?P<username>)/$', views.editUsers, name="edit_users"),
    path('showingDetails/', views.viewShowing, name="showing"),

]
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    #register
    path('register/',views.register,name='register'),

    #login view 
    path('login/', auth_views.LoginView.as_view(template_name ='app/login.html',
                                                redirect_authenticated_user=True), name='login'),
    #logout
    path('logout/', auth_views.LoginView.as_view(template_name='app/login.html'), name='logout'),

    #for activate account through mail using link
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),


    #for reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html'), name='password_reset'),

    #for password reset done
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),

    #for password reset confirm
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"), name="password_reset_confirm"),

    #for password reset complete
    path('password_reset_complete,/', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
]
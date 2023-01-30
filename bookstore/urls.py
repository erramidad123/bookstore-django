from django.urls import path 
from django.contrib.auth import views as authViews 

from . import views


urlpatterns = [
    path('', views.home,name='home'), 
    path('books/',views.books,name='books'),
    path('customer/<int:c_id>',views.customer,name='customer'), 
    path('orders/',views.orders,name='orders'),
    path('create/',views.create,name = 'create'),
    path('update/<int:order_id>',views.update,name = 'update'),
    path('delete/<int:order_id>',views.delete,name = 'delete'),
    path('login/',views.userLogin,name='login'),
    path('logout/',views.userLogout,name='logout'),
    path('register/',views.register,name = 'register'),
    path('user/',views.userProfile,name = 'user_profile'),
    path('profile/',views.profile_detail,name = 'profile_details'),
    path('reset_password',authViews.PasswordResetView.as_view(), name = "password_reset"),
    path('reset_password_sent/',authViews.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/',authViews.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path('reset_password_complete/',authViews.PasswordResetCompleteView.as_view(),  name = "password_reset_complete")

]



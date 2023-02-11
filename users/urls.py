from django.urls import path
from . import views
from . views import cloudinary_delete_image

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),
    path('details/', views.getUserProfile, name="users-details"),
    path('usernameImage/', views.getImage, name="user-image"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('updatepassword/', views.updateuserPassword,
         name="user-password-update"),
    path('getuserbyId/<str:pk>/', views.getUserbyId, name="user-by-id"),
    path('deleteimage/', cloudinary_delete_image, name="delete-image"),
]
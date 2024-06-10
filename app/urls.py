from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm
urlpatterns = [
    path('',views.home, name="home"),
      
    
    path('about/',views.about, name="about"),
    path('contact/',views.contact, name="contact"),
    path('category/<slug:val>',views.CategoryView.as_view(), name="category"), #slug because it is  text field
    path('category-title/<val>',views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>',views.ProductDetail.as_view(), name="product-detail"),
    path('profile/',views.ProfileView.as_view(), name="profile"),

    path('address/',views.address, name="address"),
    path('updateAddress/<int:pk>',views.UpdateAddress.as_view(), name="updateAddress"),

    # login authetication
    path('register/', views.CustomerRegistrationView.as_view() , name = "register") ,     
    # built in login view
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name = "logout") ,

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
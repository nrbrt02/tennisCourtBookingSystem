from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('courts', views.courts, name="courts"),
    path('support', views.support, name="support"),
    path('sessions', views.sessions, name="sessions"),
    path('checkout/<int:pk>/', views.checkout, name = "checkout"),
    path('payment-success/<int:pk>/', views.paymentSuccessful, name = "payment-successful"),
    path('payment-failed/<int:pk>/', views.paymentFailed, name = "payment-failed"),
    
    
    path('dashboard', views.dashboard, name="dashboard"),
    path('dashboard/courts', views.adminCourts, name="admin-courts"), 
    path('dashboard/courts/delete/<int:pk>', views.adminDeleteCourt, name="delete-court"), 
    path('dashboard/courts/edit/<int:pk>', views.adminEditCourt, name="edit-court"), 
    path('dashboard/bookings', views.bookings, name="admin-bookings"),  
    path('dashboard/sessions', views.dashboardSessions, name="admin-sessions"), 
    path('dashboard/sessions/add', views.dashboardAddSessions, name="admin-add-session"), 
    path('dashboard/sessions/edit/<int:pk>', views.dashboardEditSessions, name="admin-edit-session"), 
    path('dashboard/images', views.images, name="admin-images"), 
    path('dashboard/refresh', views.refresh, name="admin-refresh"), 
    path('dashboard/images/<int:pk>/', views.deleteImage, name="delete-image"), 
    path('dashboard/courts/add', views.addCourt, name="admin-add-court"), 
    path('dashboard/courts/<str:pk>/', views.changeAvailability, name="admin-courts-status"), 
    # path('accounts/logout', views.logout, name="logout"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('court/<str:pk>/', views.court, name="court"),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
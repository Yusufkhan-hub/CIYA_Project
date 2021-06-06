from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('add/', views.AddDetailsView.as_view(), name='add_details'),
    path('update/<int:pk>', views.UpdateDetailsView.as_view(), name='update_details'),
    path('delete/<int:pk>', views.DeleteDetailsView.as_view(), name='delete_details'),
    path('vehicle/', views.vehicle, name='vehicle'),

]

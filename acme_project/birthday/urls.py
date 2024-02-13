from django.urls import path

from . import views_new

app_name = 'birthday'

urlpatterns = [
    #path('', views.birthday, name='create'),
    path('', views_new.BirthdayCreateView.as_view(), name='create'),
     # Новый маршрут.
    #path('list/', views.birthday_list, name='list'),
    path('list/', views_new.BirthdayListView.as_view(), name='list'),
    #path('<int:pk>/edit/', views.birthday, name='edit'),
    path('<int:pk>/', views_new.BirthdayDetailView.as_view(), name='detail'),
    path('<int:pk>/edit/', views_new.BirthdayUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', views_new.BirthdayDeleteView.as_view(), name='delete') 
    #path('<int:pk>/delete/', views.delete_birthday, name='delete')
]

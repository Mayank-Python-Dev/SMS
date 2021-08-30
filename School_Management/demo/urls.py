from django.urls import path

from . import views

urlpatterns = [

	path('',views.home,name='home'),
	path('update/<str:pk>/',views.editStudent,name='edit'),
	path('delete/<str:pk>/',views.deleteStudent,name='delete'),
	path('ajax/load-teachers/', views.load_teacher, name='ajax_load_teachers'),
	
]
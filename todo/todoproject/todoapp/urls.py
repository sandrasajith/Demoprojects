from django.urls import path
from. import views
urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbindex/', views.Tasklistview.as_view(), name='cbindex'),
    path('cbdetail/<int:pk>/', views.TaskDetailView.as_view(), name='cbdetail'),
    path('cbupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbupdate'),
    path('cbdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbdelete')
]

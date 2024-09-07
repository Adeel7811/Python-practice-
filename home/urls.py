from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.student_list, name='student_list'),
    path('create/', views.create_student, name='create_student'),
    path('<int:stu_id>/update/', views.update_student, name='update_student'),
    path('<int:stu_id>/delete/', views.delete_student, name='delete_student'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
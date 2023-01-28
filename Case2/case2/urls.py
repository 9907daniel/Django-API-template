from django.contrib import admin
from django.urls import path
from case2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tests),
    path('<str:name>', views.test),
    path('work_order/', views.work_orders),
    path('work_order/<int:name>', views.work_order)
]

from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:contactid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('ItemList/',views.ItemList.as_view(),name='ItemList'),

]
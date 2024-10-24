from django.urls import path
from gestion import views


urlpatterns = [


    # CATEGORY
    path('category/', views.catlist, name='catlist' ),
    path('category/add/', views.addcat, name='addcat' ),
    path('category=<cat>/edit/', views.editcat, name='editcat' ),
    path('category=<cat>/delete/', views.delcat, name='delcat' ),
]
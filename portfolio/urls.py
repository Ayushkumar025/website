import os
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), 
    path('home/', views.home, name='home'),
    path('store/', views.store,name='store'),
    
    path('store/aipage.html', views.aipage,name='aipage'),
    path('store/fullstack.html', views.fullstack,name='fullstack'),
    path('store/trading.html', views.trading,name='trading'),
    path('store/free.html', views.free,name='free'),
    path('store/erp.html', views.erp,name='erp'),
    
    
    path('home/aipage.html/',views.aipage,name='aipage'),
    path('home/fullstack.html/',views.fullstack,name='fullstack'),
    path('home/trading.html/', views.trading,name='trading'),
    path('home/free.html/', views.free,name='free'),
    path('home/erp.html/', views.erp,name='erp'),
    
    
    path('home/search/',views.search,name='search'),
    path('home/search/aipage.html/',views.aipage,name='aipage'),
    path('home/search/fullstack.html/',views.fullstack,name='fullstack'),
    path('home/search/trading.html/',views.trading,name='trading'),
    path('home/search/free.html/', views.free,name='free'),
    path('home/search/erp.html/', views.erp,name='erp'),
    
    path('home/aipage.html/aisearch/',views.aisearch,name='aisearch'),
    path('home/fullstack.html/fullsearch',views.fullsearch,name='fullsearch'),    
    path('home/trading.html/tradesearch',views.tradesearch,name='tradesearch'),    
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



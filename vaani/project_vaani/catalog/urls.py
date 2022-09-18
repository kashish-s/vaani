from django.urls import path
from . import views

urlpatterns = [

    path('', views.intro_view, name='intro'),
    
    path('test/', views.TestPageView.as_view(), name = 'test'),
    

    path('record/', views.RecordPageView.as_view(), name = 'record'),
    
    path('upload/', views.UploadPageView.as_view(), name = 'upload'),
   

    path('results/', views.ResultsPageView.as_view(), name = 'results')

]
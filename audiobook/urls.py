from django.urls import path
from . import views
from .views import helloAPI, voice_search

app_name = 'audiobook'  # audiobook:search


urlpatterns = [
     # 첫 화면
     path('', views.index, name='index'),
     
     path('test/', views.test, name='test'),

    # 메인화면
    path('main/', views.MainView.as_view(), name='main'),
    path('main/search/', views.MainSearchView.as_view(), name='main_search'),
    path('main/genre/', views.MainGenreView.as_view(), name='main_genre'),

     # 청취
     path('content/<int:book_id>', views.Content.as_view(), name='content'),
     path('content/play/<int:book_id>', views.ContentPlay.as_view(), name='content_play'),

     # 성우
     path('voice/custom/<int:book_id>', views.voice_custom.as_view(), name='voice_custom'),
     path('voice/celebrity/', views.voice_celebrity, name='voice_celebrity'),
     path('voice/custom/upload/', views.voice_custom_upload.as_view(),name='voice_custom_upload'),
     path('voice/custom/complete/', views.voice_custom_complete.as_view(),name='voice_custom_complete'),
     path('voice/custom/complete/upload', views.voice_custom_upload_post, name='voice_custom_upload_post'),
     path('voice/custom/search/',views.Voice_Custom_Search.as_view(),name='voice_custom_search'),

     # 개인정보처리
     path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
  
     #rvc train
     path('rvc_train/', views.Rvc_Train.as_view(), name='rvc_train'),
     path('rvc_save/', views.Rvc_Save, name='rvc_save'),
     path('rvc_cancel/', views.Rvc_Cancel, name='rvc_cancel'),
     path('tts/', views.TTS, name="TTS")
  
]


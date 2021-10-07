from django.urls import path
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import GetLangugeData

urlpatterns = [
    #path('albums/' , GetAlbumsList.as_view(), name="myapi"),
    #path('albums/<album_id>', GetAlbumDetails.as_view() , name="myapi"),
    path('langage/',GetLangugeData.as_view(),name="myapi"),
]

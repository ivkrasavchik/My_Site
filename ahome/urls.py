from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('verse/<verse_id>/', views.verse, name="verse"),
    path('list_book', views.list_book, name="list_book"),
    path('chapter/<book_id>/', views.chapter, name="chapter"),
    path('text/<text_id><num><do>/', views.text, name="text"),
    path('log_in', views.log_in, name="log_in"),
    path('ok_log', views.ok_log, name="ok_log"),
    path('log_out', views.log_out, name="log_out"),
    path('log_on', views.log_on, name="log_on"),
    path('diary', views.diary, name="diary"),
    path('note_content', views.note_content, name="note_content"),
    path('forum', views.forum, name="forum"),
]

from django.urls import path
from . import views

#P31のアプリケーションごとにurls.pyを配置するを参照
app_name    = "scheduler"
urlpatterns = [
    path('', views.index, name="index"),
    path('delete/', views.delete, name="delete"), #←ここに削除用の処理のパスを追加する
]



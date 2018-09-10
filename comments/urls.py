from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:comment_id>/', views.detail, name="detail"),
  path('new/', views.new, name="new"),
  path('create/', views.create, name="create"),
  path('<int:comment_id>/edit/', views.edit, name="edit")
]


# path('comments/', include('polls.urls')),
#   path('admins/', admin.site.urls),
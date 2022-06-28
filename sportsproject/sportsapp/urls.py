
from django.urls import path
from .import views
app_name='sportsapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('event/<int:event_id>/',views.detail,name='detail'),
    path('add/',views.add_event,name='add_event'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]

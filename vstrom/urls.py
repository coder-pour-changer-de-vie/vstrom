from django.urls import path
from .views import IndexView, LoadParticipantsView

app_name = 'vstrom'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('load_participants/', LoadParticipantsView.as_view(), name='load_participants'),
]

from django.urls import path
from measurement.views import ListCreateView, SensUpdateView, MeasurementCreateView, SensView

urlpatterns = [
    path('listsens/', ListCreateView.as_view()),
    path('sensup/<int:pk>/', SensUpdateView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
    path('sensors/<int:pk>/', SensView.as_view()),

]

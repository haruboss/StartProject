from django.urls import path
from .views import *

app_name = 'testApp'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('advisor-list/', Advisor.as_view(), name='advisor'),
    path('advisor-create/', AdvisorCreate.as_view(), name='advisor-create'),
    path('user/register/', UserCreate.as_view(), name='create-user'),
    path('advisor-booking/', AdvisorBooking.as_view(), name='advisor-booking'),
    path('advisor-booking-list/', advisorBookingList.as_view({'get': 'list'}),
         name='advisor-boooking-list')
]

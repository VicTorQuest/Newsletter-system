from django.urls import path
from .views import home, subscription_confirmed, send_news_letter, edit_preference, start_unsubscribe, unsubscribe, unsubscribe_successful, send_preference_link, adminaaccess



urlpatterns = [
    path('', home, name="home"),
    path('how-to-access-admin/', adminaaccess, name='adminaaccess'),
    path('subscription_confirmed', subscription_confirmed, name="subscription_confirmed"),
    path('subscription-confirmed/', subscription_confirmed, name='subscription_confirmed'),
    path('edit-preference/', send_preference_link, name='send_preference_link'),
    path('edit-preference/<slug:slug>/', edit_preference, name='edit_preference'),
    path('unsubscribe/<slug:slug>/', unsubscribe, name='unsubscribe'),
    path('unsubscription-successful/', unsubscribe_successful, name='unsubscribe_successful'),
    path('send-news-letter/', send_news_letter, name='send_news_letter'),
    path('unsubscribe/', start_unsubscribe, name='start_unsubscribe'),
]

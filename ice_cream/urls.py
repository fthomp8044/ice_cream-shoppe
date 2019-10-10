from django.urls import path
from . import views
from .views import DailyFlavor, SeasonalFlavor, WeeklyFlavor, FeaturedFlavor, increment_votes

app_name = 'icecream'
#the path order the urls will follow

urlpatterns = [

    path('featured_flavors/', views.FeaturedFlavor.as_view(), name="ice-cream-featured-flavors"),
    path('daily_flavors/', views.DailyFlavor.as_view(), name="ice-cream-daily-flavors"),
    path('weekly_flavors/', views.WeeklyFlavor.as_view(), name="ice-cream-weekly-flavors"),
    path('seasonal_flavors/', views.SeasonalFlavor.as_view(), name="ice-cream-seasonal-flavors"),
    path('<int:pk>/', views.increment_votes, name='votes'),
    # <int:pk> is a placeholder. ex. icecream/3/delete.
    path('<int:pk>/delete/', views.delete_view, name='delete'),
    path('new/', views.CreateView.as_view(), name='ice_cream_new')
    # path('', views.IndexView, name='')





]

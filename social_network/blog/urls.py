from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.urlpatterns import format_suffix_patterns
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('user_activity/<int:pk>', views.ActivityUserView.as_view(), name='user_activity'),
    path('register/', views.RegisterApi.as_view()),
    path('post/analitics/date_from=<date_from>&date_to=<date_to>/', views.PostAnaliticsLikesView.as_view(), name='post_likes'),
]

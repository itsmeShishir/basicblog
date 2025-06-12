from django.urls import path
from .views import login_view, register_view, logouts, update_profile, update_password, dashboard
urlpatterns = [
    path("login", login_view, name="logins"),
    path("register", register_view, name="registers"),
    path("logouts", logouts, name="logouts"),
    path("update_profile", update_profile, name="update_profile"),
    path("update_password", update_password, name="update_password"),
    path("dashboard", dashboard, name="dashboard"),
]

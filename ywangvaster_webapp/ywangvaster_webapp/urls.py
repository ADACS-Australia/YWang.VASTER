"""ywangvaster_webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from candidate_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("site_admin/", views.site_admin, name="site_admin"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("change_password/", views.AppChangePassword.as_view(), name="change_password"),
    # Candidate pages
    path("ratings_summary/", views.ratings_summary, name="ratings_summary"),
    path("candidates/", views.candidate_table, name="candidates"),
    path("candidate_random/", views.candidate_random, name="candidate_random"),
    path("clear_candidates_filter/", views.clear_candidates_filter, name="clear_candidates_filter"),
    path("clear_ratings_filter/", views.clear_ratings_filter, name="clear_ratings_filter"),
    path("candidate_rating/<str:cand_hash_id>/", views.candidate_rating, name="candidate_rating"),
    path("create_tag/", views.create_tag, name="create_tag"),
    path("download_lightcurve/<str:cand_hash_id>", views.download_lightcurve_csv, name="download_lightcurve_csv"),
    path("project_select/", views.project_select, name="project_select"),
    # Get nearby objects (all databases in one)
    path("get_nearby_objects/", views.nearby_objects_table, name="get_nearby_objects"),
    # To get or create a token for a user by a post request
    path("get_token/", views.get_token, name="get_token"),
    # Add records to the DB using a POST request
    path("upload_observation/", views.upload_observation, name="upload_observation"),
    path("upload_beam/", views.upload_beam, name="upload_beam"),
    path("upload_candidate/", views.upload_candidate, name="upload_candidate"),
    # Delete records from the DB
    path("delete/", views.delete, name="delete"),
]

# This allows media and css files to be linked and viewed directly
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

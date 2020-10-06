from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page, name="home-page"),
    # LOGIN
    path('login/', views.login_page, name="login"),
    path('login-user/', views.user_login, name="login-user"),
    # LOGOUT
    path('user-logout/', views.logout, name="user-logout"),
    # SIGN IN
    path('signup/', views.signup_page, name="signup"),
    path('add-user/', views.insert_user, name="add-user"),
    path('check-username/', views.check_username, name="check-username"),
    # INSERT INSPECTION
    path('insert_the_inspection/', views.insert_inspection, name="insert_the_inspection"),
    # GET INSPECTION
    path('get-inspection/', views.get_inspection, name="get-inspection"),
    # UPDATE INSPECTION
    path('update-inspection/', views.update_inspection, name="update-inspection"),
    # DELETE INSPECTION
    path('del-insp/', views.delete_inspection, name="del-insp"),
    # DRAFT FORM INSERT
    path('inspection-draft/', views.drafts_show, name="inspection-draft"),
    path('insert-draft/', views.insert_draft, name="insert-draft"),
    path('insert-draft-form/', views.insert_draft_form, name="insert-draft-form"),
    # DRAFT FORM UPDATE
    path('update-draft/', views.update_draft, name="update-draft"),
    # APPROVE INSPECTION
    path('inspection-approve/', views.insp_approve, name="inspection-approve"),
    # SEARCH INSPECTIONS
    path('inspection-search/', views.insp_search, name="inspection-search"),
    # FILTER INSPECTIONS
    path('inspection-filter/', views.insp_filter, name="inspection-filter"),
]
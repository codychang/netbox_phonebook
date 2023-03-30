from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (

    path('function/', views.FunctionListView.as_view(), name='function_list'),
    path('function/add/', views.FunctionEditView.as_view(), name='function_add'),
    path('function/<int:pk>/', views.FunctionView.as_view(), name='function'),
    path('function/<int:pk>/edit/', views.FunctionEditView.as_view(), name='function_edit'),
    path('function/<int:pk>/delete/', views.FunctionDeleteView.as_view(), name='function_delete'),
    path('function/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='function_changelog', kwargs={
        'model': models.Function
    }),

    path('status/', views.StatusListView.as_view(), name='status_list'),
    path('status/add/', views.StatusEditView.as_view(), name='status_add'),
    path('status/<int:pk>/', views.StatusView.as_view(), name='status'),
    path('status/<int:pk>/edit/', views.StatusEditView.as_view(), name='status_edit'),
    path('status/<int:pk>/delete/', views.StatusDeleteView.as_view(), name='status_delete'),
    path('status/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='status_changelog', kwargs={
        'model': models.Status
    }),

    path('number/', views.NumberListView.as_view(), name='number_list'),
    path('number/add/', views.NumberEditView.as_view(), name='number_add'),
    path('number/<int:pk>/', views.NumberView.as_view(), name='number'),
    path('number/<int:pk>/edit/', views.NumberEditView.as_view(), name='number_edit'),
    path('number/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='number_changelog', kwargs={
        'model': models.Number
    }),

)


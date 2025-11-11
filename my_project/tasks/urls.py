"""
URLs de la aplicación Tasks.

Este archivo define todas las rutas relacionadas con la gestión de tareas.
Se incluye en el URLconf principal del proyecto.
"""

from django.urls import path
from . import views

urlpatterns = [
    # Lista de tareas (página principal)
    path('', views.TaskListView.as_view(), name='task-list'),

    # Ver detalles de una tarea
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task-detail'),

    # Crear nueva tarea
    path('task/create/', views.TaskCreateView.as_view(), name='task-create'),

    # Editar tarea existente
    path('task/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task-update'),

    # Eliminar tarea
    path('task/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task-delete'),

    # Toggle estado de completitud
    path('task/<int:pk>/toggle/', views.toggle_task_status, name='task-toggle'),
]

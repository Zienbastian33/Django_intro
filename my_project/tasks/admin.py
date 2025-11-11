from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    """
    Configuración del admin para el modelo Task.
    Esta clase personaliza cómo se visualizan las tareas en el panel admin.
    """

    # Campos que se muestran en la lista
    list_display = [
        'title',
        'priority',
        'completed',
        'created_at',
        'updated_at'
    ]

    # Campos por los que se puede filtrar
    list_filter = [
        'completed',
        'priority',
        'created_at'
    ]

    # Campo de búsqueda
    search_fields = [
        'title',
        'description'
    ]

    # Campos editables directamente desde la lista
    list_editable = [
        'completed',
        'priority'
    ]

    # Campos de solo lectura
    readonly_fields = [
        'created_at',
        'updated_at'
    ]

    # Organización de campos en el formulario de edición
    fieldsets = (
        ('Información Básica', {
            'fields': ('title', 'description')
        }),
        ('Estado y Prioridad', {
            'fields': ('completed', 'priority')
        }),
        ('Metadatos', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Sección colapsable
        }),
    )

    # Valores por defecto al crear nueva tarea
    def get_changeform_initial_data(self, request):
        return {
            'priority': 'medium',
            'completed': False,
        }

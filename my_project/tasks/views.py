from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib import messages
from .models import Task


class TaskListView(ListView):
    """
    Vista para listar todas las tareas.
    ListView es una vista genérica de Django que maneja automáticamente:
    - Consulta a la base de datos
    - Paginación
    - Contexto para el template
    """
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10  # Paginación: 10 tareas por página

    def get_queryset(self):
        """
        Personaliza la consulta de tareas.
        Permite filtrar por estado si se pasa parámetro en URL.
        """
        queryset = super().get_queryset()
        status = self.request.GET.get('status')

        if status == 'completed':
            queryset = queryset.filter(completed=True)
        elif status == 'pending':
            queryset = queryset.filter(completed=False)

        return queryset

    def get_context_data(self, **kwargs):
        """Agrega datos adicionales al contexto del template"""
        context = super().get_context_data(**kwargs)
        context['total_tasks'] = Task.objects.count()
        context['completed_tasks'] = Task.objects.filter(completed=True).count()
        context['pending_tasks'] = Task.objects.filter(completed=False).count()
        return context


class TaskDetailView(DetailView):
    """
    Vista para ver los detalles de una tarea específica.
    """
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    """
    Vista para crear nuevas tareas.
    CreateView maneja automáticamente:
    - Renderizar formulario
    - Validación
    - Guardado en base de datos
    """
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'priority']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        """Se ejecuta cuando el formulario es válido"""
        messages.success(self.request, '¡Tarea creada exitosamente!')
        return super().form_valid(form)


class TaskUpdateView(UpdateView):
    """
    Vista para editar tareas existentes.
    Similar a CreateView pero para actualización.
    """
    model = Task
    template_name = 'tasks/task_form.html'
    fields = ['title', 'description', 'priority', 'completed']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        """Se ejecuta cuando el formulario es válido"""
        messages.success(self.request, '¡Tarea actualizada exitosamente!')
        return super().form_valid(form)


class TaskDeleteView(DeleteView):
    """
    Vista para eliminar tareas.
    Requiere confirmación antes de eliminar.
    """
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def delete(self, request, *args, **kwargs):
        """Se ejecuta al confirmar eliminación"""
        messages.success(self.request, 'Tarea eliminada exitosamente.')
        return super().delete(request, *args, **kwargs)


def toggle_task_status(request, pk):
    """
    Vista funcional simple para cambiar estado de completitud.
    Ejemplo de FBV para operaciones pequeñas.
    """
    try:
        task = Task.objects.get(pk=pk)
        task.completed = not task.completed
        task.save()
        status = "completada" if task.completed else "marcada como pendiente"
        messages.success(request, f'Tarea "{task.title}" {status}.')
    except Task.DoesNotExist:
        messages.error(request, 'Tarea no encontrada.')

    return redirect('task-list')

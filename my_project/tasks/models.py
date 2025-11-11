from django.db import models
from django.utils import timezone


class Task(models.Model):
    """
    Modelo para representar una tarea en el Task Manager.

    Attributes:
        title: Título de la tarea (requerido)
        description: Descripción detallada (opcional)
        completed: Estado de completitud
        priority: Nivel de prioridad (Alta, Media, Baja)
        created_at: Timestamp de creación
        updated_at: Timestamp de última actualización
    """

    # Choices para el campo priority
    PRIORITY_CHOICES = [
        ('high', 'Alta'),
        ('medium', 'Media'),
        ('low', 'Baja'),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name='Título',
        help_text='Título descriptivo de la tarea'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descripción',
        help_text='Descripción detallada de la tarea (opcional)'
    )

    completed = models.BooleanField(
        default=False,
        verbose_name='Completada'
    )

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Prioridad'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Fecha de creación'
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Última actualización'
    )

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-created_at']  # Más recientes primero

    def __str__(self):
        """Representación en string del objeto"""
        status = "✓" if self.completed else "○"
        return f"{status} {self.title}"

    def get_priority_badge(self):
        """Retorna un emoji según la prioridad"""
        badges = {
            'high': '🔴',
            'medium': '🟡',
            'low': '🟢',
        }
        return badges.get(self.priority, '⚪')

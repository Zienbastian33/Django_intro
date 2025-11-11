# Task Manager - Django Project

Sistema de gestión de tareas desarrollado con Django 5.1, diseñado como proyecto de portfolio para demostrar habilidades en desarrollo web con Python.

## Características

- **CRUD Completo**: Crear, leer, actualizar y eliminar tareas
- **Sistema de Prioridades**: Clasificación de tareas (Alta, Media, Baja)
- **Estado de Tareas**: Marcar como completadas o pendientes
- **Filtros Avanzados**: Filtrar por estado de completitud
- **Interfaz Moderna**: UI responsive con Bootstrap 5
- **Panel de Administración**: Django Admin personalizado
- **Estadísticas**: Dashboard con métricas de tareas
- **Paginación**: Navegación eficiente para muchas tareas

## Stack Tecnológico

- **Backend**: Django 5.1.3
- **Base de Datos**: SQLite3
- **Frontend**: Bootstrap 5, Bootstrap Icons
- **Python**: 3.11+

## Instalación

### Requisitos Previos

- Python 3.11 o superior
- pip (gestor de paquetes de Python)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/Zienbastian33/Django_intro.git
cd Django_intro
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Aplicar migraciones**
```bash
cd my_project
python manage.py migrate
```

5. **Crear superusuario** (para acceder al admin)
```bash
python manage.py createsuperuser
```

6. **Iniciar servidor de desarrollo**
```bash
python manage.py runserver
```

7. **Acceder a la aplicación**
- Aplicación principal: http://localhost:8000/
- Panel de administración: http://localhost:8000/admin/

## Uso

### Credenciales de Prueba

Si estás usando este proyecto de ejemplo, puedes usar:
- **Usuario**: admin
- **Contraseña**: admin123

### Funcionalidades Principales

#### Crear Tarea
1. Click en "Nueva Tarea" en el navbar
2. Completa el formulario con título, descripción y prioridad
3. Click en "Crear Tarea"

#### Ver Tareas
- La página principal muestra todas las tareas
- Usa los filtros para ver solo completadas o pendientes
- Click en el ícono de ojo para ver detalles completos

#### Editar Tarea
1. Click en el ícono de lápiz en una tarea
2. Modifica los campos necesarios
3. Click en "Guardar Cambios"

#### Cambiar Estado
- Click en el ícono de check para alternar entre completada/pendiente

#### Eliminar Tarea
1. Click en el ícono de basura
2. Confirma la eliminación

## Estructura del Proyecto

```
Django_intro/
├── my_project/
│   ├── manage.py              # CLI de Django
│   ├── my_project/            # Configuración del proyecto
│   │   ├── settings.py        # Configuración global
│   │   ├── urls.py            # URLs principales
│   │   └── wsgi.py            # WSGI config
│   └── tasks/                 # Aplicación de tareas
│       ├── models.py          # Modelo Task
│       ├── views.py           # Vistas (CBVs)
│       ├── urls.py            # URLs de la app
│       ├── admin.py           # Configuración del admin
│       ├── templates/         # Templates HTML
│       └── migrations/        # Migraciones de DB
├── requirements.txt           # Dependencias
└── README.md                  # Este archivo
```

## Arquitectura

### Modelo de Datos

**Task Model** (`tasks/models.py:5`)
- `title`: CharField - Título de la tarea
- `description`: TextField - Descripción detallada (opcional)
- `completed`: BooleanField - Estado de completitud
- `priority`: CharField - Prioridad (high, medium, low)
- `created_at`: DateTimeField - Fecha de creación
- `updated_at`: DateTimeField - Última actualización

### Vistas Principales

| Vista | Tipo | URL | Descripción |
|-------|------|-----|-------------|
| TaskListView | ListView | `/` | Lista todas las tareas |
| TaskDetailView | DetailView | `/task/<id>/` | Muestra detalles de tarea |
| TaskCreateView | CreateView | `/task/create/` | Crea nueva tarea |
| TaskUpdateView | UpdateView | `/task/<id>/edit/` | Edita tarea existente |
| TaskDeleteView | DeleteView | `/task/<id>/delete/` | Elimina tarea |
| toggle_task_status | FBV | `/task/<id>/toggle/` | Alterna estado |

## Conceptos de Django Demostrados

- **MTV Pattern**: Models, Templates, Views
- **Class-Based Views (CBVs)**: Uso de vistas genéricas
- **Django ORM**: Consultas y relaciones de base de datos
- **Template Inheritance**: Reutilización de templates
- **URL Routing**: Sistema de URLs modular
- **Admin Customization**: Personalización del panel admin
- **Messages Framework**: Sistema de notificaciones
- **Form Handling**: Validación y procesamiento de formularios

## Mejoras Futuras

- [ ] Sistema de autenticación de usuarios
- [ ] Asignar tareas a diferentes usuarios
- [ ] Etiquetas y categorías
- [ ] Fechas límite (deadlines)
- [ ] Notificaciones por email
- [ ] API REST con Django REST Framework
- [ ] Tests automatizados
- [ ] Deploy en producción (Heroku/Railway)

## Desarrollo

### Comandos Útiles

```bash
# Crear nueva migración
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Abrir shell de Django
python manage.py shell

# Ejecutar tests
python manage.py test

# Crear superusuario
python manage.py createsuperuser
```

## Licencia

MIT License - Ver archivo [LICENSE](LICENSE) para más detalles.

## Autor

**Zienbastian**
- GitHub: [@Zienbastian33](https://github.com/Zienbastian33)

## Contacto

Para preguntas o sugerencias sobre este proyecto, por favor abre un issue en GitHub.

---

*Proyecto desarrollado como parte de un portfolio de desarrollo web con Django.*

https://github.com/sandraEstlo/odoo-module/blob/main/imagenes/banner_1.png

## Descripción del Proyecto
Este proyecto consiste en el desarrollo de un módulo de **Gestión de Tareas** para Odoo, diseñado para organizar y supervisar las tareas dentro de un proyecto. Mejora la eficiencia y productividad al simplificar la gestión de las tareas diarias.

## Funcionalidades
- **Operaciones sobre Tareas:** Crear, borrar, modificar y asignar tareas.
- **Monitoreo de Tareas:** Realizar seguimiento del estado de cada tarea y monitorear el progreso global del proyecto.
- **Fases del Proyecto:** Organizar las tareas en fases del proyecto para gestionar mejor los hitos.

## Características
### Vistas
**Árbol (Tree):** Visualiza las tareas y fases del proyecto en una estructura jerárquica.
**Formulario (Form):** Formularios detallados para gestionar tareas, fases y empleados.
**Kanban:** Interfaz visual intuitiva para gestionar las tareas mediante arrastrar y soltar.
**Calendario:** Muestra las tareas según el proyecto y la fase en formato calendario.

### Seguimiento de Estado 
Indicadores visuales como barras de progreso y colores para priorizar tareas y fases.

### Seguridad
Roles de usuario diferenciados (administrador y usuario).
Control de acceso y permisos para modificar o acceder a datos.

### Informes
Genera informes detallados del proyecto, incluyendo las tareas y fases relacionadas, así como los empleados asignados a cada tarea.

### Datos Demo
Datos de ejemplo precargados para facilitar las pruebas y la comprensión del módulo.

## Requisitos No Funcionales
### Base de Datos
Implementación de campos calculados (por ejemplo, porcentaje de tareas completadas).
Restricciones SQL para asegurar la integridad de los datos (por ejemplo, nombres únicos de proyectos, fechas válidas para las tareas).

### Restricciones en Python
Lógica para garantizar relaciones válidas entre tareas y proyectos, como las fechas y límites de longitud de campos.

### Funciones Avanzadas
Vistas Kanban dinámicas con barras de progreso.
Filtros para búsqueda de tareas por proyecto o fase.
Vista Gantt (en versiones Enterprise).

## Diagrama de Clases UML
El módulo utiliza los siguientes modelos:
**Proyecto:** Agrupa las fases y tareas.
**Fase:** Contiene tareas relacionadas con una fase del proyecto.
**Tarea:** Representa una tarea con seguimiento de progreso y asignación de empleados.
**Empleado:** Representa a los empleados encargados de realizar las tareas.

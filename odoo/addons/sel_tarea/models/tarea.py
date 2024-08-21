from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Tarea(models.Model):
    _name = 'sel_tarea.tarea'
    _description = 'Tareas en las que se dividen las fases del proyecto'
    
    name = fields.Char('Nombre')
    description = fields.Text('Descripcion')
    empleado_ids = fields.Many2many('sel_tarea.empleado', string='Empleados')
    f_start = fields.Date(string=('fecha inicio'), default=fields.Date.context_today)
    f_end = fields.Date(string=('fecha fin'), default=fields.Date.context_today)
    fase_id = fields.Many2one('sel_tarea.fase', string='Fase')
    proyecto_id = fields.Many2one('sel_tarea.proyecto', string='Proyecto')

    estado_color = fields.Char(string='Color del Estado', compute='_compute_estado_color')

    estado = fields.Selection(
        string=('Estado'),
        selection=[
            ('0', 'To Do'),
            ('1', 'In Progress'),
            ('2', 'Blocked'),
            ('3', 'In Review'),
            ('4', 'Done')
        ],
    )

    prioridad = fields.Selection(
        string=('prioridad'),
        selection=[
            ('0', 'baja'),
            ('1', 'media'),
            ('2', 'alta'),
            ('3', 'urgente'),
        ],
    )

    @api.depends('estado')
    def _compute_estado_color(self):
        for tarea in self:
            if tarea.estado == '0':
                tarea.estado_color = '#17a2b8'  
            elif tarea.estado == '1':
                tarea.estado_color = '#007bff' 
            elif tarea.estado == '2':
                tarea.estado_color = '#dc3545'  
            elif tarea.estado == '3':
                tarea.estado_color = '#ffc107'  
            elif tarea.estado == '4':
                tarea.estado_color = '#28a745' 
            else:
                tarea.estado_color = '#000000'

    @api.constrains('f_start', 'f_end')
    def sel_tarea_tarea_check_fechas(self):
        for tarea in self:
            if tarea.f_start and tarea.f_end and tarea.f_start > tarea.f_end:
                raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
            
    @api.constrains('f_start', 'f_end')
    def _check_dates(self):
        for tarea in self:
            if tarea.f_start < tarea.fase_id.f_start:
                raise ValidationError("La fecha de inicio de la tarea no puede ser menor que la fecha de inicio de la fase.")
            if tarea.f_end > tarea.fase_id.f_end:
                raise ValidationError("La fecha de fin de la tarea no puede ser mayor que la fecha de fin de la fase.")
            if tarea.f_end < tarea.f_start:
                raise ValidationError("La fecha de fin de la fase debe ser posterior a la fecha de inicio.")
            
    @api.constrains('name')
    def _check_nombre_vacio(self):
        for record in self:
            if not record.name:
                raise ValidationError("El nombre no puede estar vacío.")

    @api.constrains('description')
    def _check_descripcion(self):
        for record in self:
            if not record.description and len(record.description) > 250:
                raise ValidationError("La descripción no puede superar los 250 caracteres.")
    
    _sql_constraints = [
        ('check_nombre_vacio', 'CHECK(name IS NOT NULL)', 'El nombre no puede estar vacío.'),
        ('check_descripcion_length', 'CHECK(LENGTH(description) <= 250)', 'La descripción no puede superar los 250 caracteres.')
    ]
    


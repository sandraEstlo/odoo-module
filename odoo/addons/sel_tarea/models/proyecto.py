from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Proyecto(models.Model):
    _name = 'sel_tarea.proyecto'
    _description = 'Proyectos al que pertenecen las tareas'
    
    id = fields.Integer(string=('id'))
    name = fields.Char('Nombre')
    description = fields.Char('Descripcion')
    f_start = fields.Date('fecha_inicio')
    f_end = fields.Date('fecha fin')
    fases_ids = fields.One2many('sel_tarea.fase', 'proyecto_id', string='Fases')
    total_fases_completadas = fields.Float(string="Porcentaje", compute="_porcentaje_total_fase", store=True)
    tareas_ids = fields.One2many('sel_tarea.tarea', 'proyecto_id', string='Tareas')

    @api.depends('fases_ids')
    def _porcentaje_total_fase(self):
        for proyecto in self:
            total_fases = len(proyecto.fases_ids)
            suma_total_fases = sum(fase.total_tareas_completadas for fase in proyecto.fases_ids)

            proyecto.total_fases_completadas = (suma_total_fases / total_fases) if total_fases > 0 else 0

    @api.constrains('name')
    def _check_nombre_vacio(self):
        for record in self:
            if not record.name:
                raise ValidationError("El nombre no puede estar vacío.")

    @api.constrains('f_start', 'f_end')
    def _check_dates(self):
        for proyecto in self:
            if proyecto.f_start and proyecto.f_end and proyecto.f_start > proyecto.f_end:
                raise ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")   
    
    _sql_constraints = [
        ('check_nombre_vacio', 'CHECK(name IS NOT NULL)', 'El nombre no puede estar vacío.'),
        ('check_dates', 'CHECK(f_start IS NULL OR f_end IS NULL OR f_start < f_end)', 'La fecha de inicio no puede ser posterior a la fecha de fin.'),
        ('name_unique','UNIQUE(name)',"El nombre del proyecto debe ser unico")
    ]
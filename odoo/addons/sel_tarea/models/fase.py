from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Fase(models.Model):
    _name = 'sel_tarea.fase'
    _description = 'Fases del proyecto'
    
    name = fields.Char('Nombre')
    description = fields.Char('Descripcion')
    tareas_ids = fields.One2many('sel_tarea.tarea', 'fase_id', string='Tareas')
    f_start = fields.Date('fecha_inicio')
    f_end = fields.Date('fecha_fin')
    proyecto_id = fields.Many2one('sel_tarea.proyecto', string='Proyecto')
    total_tareas_completadas = fields.Float(string="Porcetaje", compute="_compute_total_tareas_completadas", store=True)
    
    @api.depends('tareas_ids')
    def _compute_total_tareas_completadas(self):
        for fase in self:
            total_tareas = len(fase.tareas_ids)
            if total_tareas > 0:
                total_completadas = len(fase.tareas_ids.filtered(lambda tarea: tarea.estado == '4'))
                fase.total_tareas_completadas = (total_completadas / total_tareas) * 100
            else:
                fase.total_tareas_completadas = 0

    @api.constrains('name')
    def _check_nombre_vacio(self):
        for record in self:
            if not record.name:
                raise ValidationError("El nombre no puede estar vacío.")
                
    @api.constrains('f_start', 'f_end')
    def _check_dates(self):
        for fase in self:
            if fase.f_start < fase.proyecto_id.f_start:
                raise ValidationError("La fecha de inicio de la fase no puede ser menor que la fecha de inicio del proyecto.")
            if fase.f_end > fase.proyecto_id.f_end:
                raise ValidationError("La fecha de fin de la fase no puede ser mayor que la fecha de fin del proyecto.")
            if fase.f_end <= fase.f_start:
                raise ValidationError("La fecha de fin de la fase debe ser posterior a la fecha de inicio.")
    
    _sql_constraints = [
        ('check_nombre_vacio', 'CHECK(name IS NOT NULL)', 'El nombre no puede estar vacío.')
    ]
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'sel_tarea.empleado'
    _description = 'Empleado que realiza la tarea'

    name = fields.Char(string=('Name'))
    correo = fields.Char(string=('Correo'))
    tarea_ids = fields.Many2many('sel_tarea.tarea', string='Tareas')
    avatar = fields.Image(string=('avatar'),store=True, max_width=150, max_height=150)

    @api.model_create_single
    def create(self, vals):
        empleado = super(Empleado, self).create(vals)

        user_vals = {
            'name': empleado.name,
            'login': empleado.correo,
            'password': 'contrasena',
            'groups_id': [(6, 0, [
                self.env.ref('sel_tarea.sel_tarea_user').id,
                self.env.ref('base.group_user').id
            ])]
        }

        self.env['res.users'].create(user_vals)
        return empleado
    
    @api.model
    def unlink(self):
        users_to_delete = self.env['res.users'].search([('login', 'in', self.mapped('correo'))])
        users_to_delete.unlink()

        return super(Empleado, self).unlink()

    @api.constrains('name')
    def _check_nombre_vacio(self):
        for record in self:
            if not record.name:
                raise ValidationError("El nombre no puede estar vacio.")
            
    @api.constrains('correo')
    def _check_correo_vacio(self):
        for record in self:
            if not record.correo:
                raise ValidationError("El correo no puede estar vacio.")

    _sql_constraints = [
        ('name_not_empty', 'CHECK(length(name) > 0)', 'El nombre no puede estar vacío.'),
        ('correo_not_empty', 'CHECK(length(correo) > 0)', 'El correo no puede estar vacío.'),
        ('correo_uniqque', 'UNIQUE(correo)', 'El correo introducido ya se encuentra registrado')
    ]
    
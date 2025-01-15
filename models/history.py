from odoo import models, fields, api

class History(models.Model):
    _name = 'managealvaro.history'
    _description = 'managealvaro.history'

    name = fields.Char(string="Nombre", required=True, help="Nombre del la historia")
    description = fields.Text(string="Descripción")

    # Relaciones:
#    used_technologies = fields.Many2many("managealvaro.technology", compute="_get_used_technologies")
    project_id = fields.Many2one('managealvaro.project', string="Project", ondelete='cascade', required=True)
    task_ids = fields.One2many('managealvaro.task', 'history_id', string="Task")

"""
    @api.depends('task_ids.technology_ids')
    def _get_used_technologies(self):
        for history in self:
            technologies = self.env['managealvaro.technology']
            for task in history.task_ids:
                technologies |= task.technology_ids
            history.used_technologies = [(6, 0, technologies.ids)]
"""

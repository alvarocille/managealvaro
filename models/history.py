# -*- coding: utf-8 -*-

from odoo import models, fields

class history(models.Model):
    _name = 'managealvaro.history'
    _description = 'managealvaro.history'

    name = fields.Char(string="Nombre", required=True, help="Nombre del la historia")
    description = fields.Text(string="Descripción")

    # Relaciones:
    project_id = fields.Many2one('managealvaro.project', string="Project", ondelete='cascade', required=True)
    task_ids = fields.One2many('managealvaro.task', 'history_id', string="Task")

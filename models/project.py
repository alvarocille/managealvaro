# -*- coding: utf-8 -*-

from odoo import models, fields

class project(models.Model):
    _name = 'managealvaro.project'
    _description = 'managealvaro.project'

    name = fields.Char(string="Nombre", required=True, help="Nombre del proyecto")
    description = fields.Text(string="Descripción")

    # Relaciones:
    history_ids = fields.One2many('managealvaro.history', 'project_id', string="History")
    sprint_ids = fields.One2many('managealvaro.sprint', 'project_id', string="Sprint")
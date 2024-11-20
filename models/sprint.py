# -*- coding: utf-8 -*-

from odoo import models, fields


class sprint(models.Model):
    _name = 'managealvaro.sprint'
    _description = 'managealvaro.sprint'

    name = fields.Char(string="Nombre", required=True, help="Nombre del sprint")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")

    # Relaciones:
    task_id = fields.One2many('managealvaro.task', "sprint_id", "Task" )

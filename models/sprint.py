# -*- coding: utf-8 -*-
from datetime import datetime

from odoo import models, fields, api
import datetime


class sprint(models.Model):
    _name = 'managealvaro.sprint'
    _description = 'managealvaro.sprint'

    name = fields.Char(string="Nombre", required=True, help="Nombre del sprint")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    duration = fields.Integer()
    end_date = fields.Datetime(string="Fecha de finalización", compute="_get_end_date", store=True)

    # Relaciones:
    task_id = fields.One2many('managealvaro.task', "sprint_id", "Task" )
    project_id = fields.Many2one('managealvaro.project', 'Project', ondelete='cascade', required=True)

    # Métodos:
    @api.depends('start_date', 'duration'   )
    def _get_end_date(self):
        for s in self:
            if isinstance(s.start_date, datetime.date) and s.duration > 0:
                s.end_date = s.start_date + datetime.timedelta(days=s.duration)
            else:
                s.end_date = s.start_date
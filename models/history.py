# -*- coding: utf-8 -*-

from odoo import models, fields

class history(models.Model):
    _name = 'managealvaro.history'
    _description = 'managealvaro.history'

    name = fields.Char(string="Nombre", required=True, help="Nombre del la historia")
    description = fields.Text(string="Descripción")

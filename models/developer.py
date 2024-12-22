# -*- coding: utf-8 -*-

from odoo import models, fields

class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    technologies = fields.Many2many('manage.technology', string='Technologies',
                                    relation = 'developer_technologies',
                                    column1='developer_id',
                                    column2='technologies_id')
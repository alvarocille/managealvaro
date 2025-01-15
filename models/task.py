# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
from odoo import models, fields, api

class Task(models.Model):
    _name = "managealvaro.task"
    _description = "managealvaro.task"

    name = fields.Char(string="Nombre", required=True, help="Nombre de la tarea")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de finalización")
    is_paused = fields.Boolean(string="Pausada")
    code = fields.Char(string="Code", compute="_get_code")

    # Relaciones:
    sprint_id = fields.Many2one('managealvaro.sprint', 'Sprint', compute="_get_sprint", store=True)
    technology_ids = fields.Many2many(
        "managealvaro.technology",
        string="Tecnologías",
        ondelete="cascade",
        relation="task_technology",
        column1="technology_ids",
        column2="task_ids"
    )
    history_id = fields.Many2one('managealvaro.history', 'History', ondelete='cascade', required=True)

    # Métodos:
    def _get_code(self):
        for t in self:
            t.code = "TSK_" + str(t.id)

    @api.depends('code')
    def _get_sprint(self):
        for t in self:
            sprints = self.env['managealvaro.sprint'].search([('project_id.id', '=', t.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime) and sprint.end_date > datetime.now():
                    t.sprint_id = sprint.id
                    found = True

            if not found:
                t.sprint_id = False

    def create_deadline_notifications(self):
        for task in self:
            if task.end_date:
                self.env['managealvaro.notification'].create({
                    'name': f'Recordatorio: Tarea {task.name} próxima a vencer',
                    'description': f'La tarea {task.name} está próxima a su fecha límite.',
                    'notification_date': task.end_date - timedelta(days=1),  # Un día antes de la fecha límite
                    'user_id': self.env.user.id,  # Usuario actual
                    'task_id': task.id,
                })

    @api.model
    def create(self, vals):
        task = super(Task, self).create(vals)
        task.create_deadline_notifications()
        return task

    def write(self, vals):
        res = super(Task, self).write(vals)
        if 'end_date' in vals:
            self.create_deadline_notifications()
        return res
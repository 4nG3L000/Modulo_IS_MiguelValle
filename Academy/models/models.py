# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Course(models.Model):
    _name = 'academy.course'

    title = fields.Char('Titulo')
    description = fields.Char('Descripcion')
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    hora = fields.Char()
    image = fields.Binary('Logo')

    participant_ids = fields.Many2many('academy.participant', string="Participantes:") 
    # en este campo se muestra el campo name del modelo academy.teacher        
    teacher_id = fields.Many2one('academy.teacher', string="Docente:")         

class Participant(models.Model):
    _name = "academy.participant"

    first_name = fields.Char('Nombre')
    last_name = fields.Char('Epellido')
    doc_id = fields.Char('identificacion')
    phone = fields.Char('Telefono')
    email = fields.Char('Correo')
    image = fields.Binary('Foto de perfil')

    course_ids = fields.Many2many('academy.course', string="Inscrito a:")

class Teacher(models.Model):
    _name = "academy.teacher"
#   _rec_name = "other_name" usar esta linea conado entre los campos no se tenga el campo name

    name = fields.Char('Nombre completo')
    doc_id = fields.Char('identificacion')
    phone = fields.Char('Telefono')
    email = fields.Char('Correo')
    image = fields.Binary('Foto de perfil')

    course_ids = fields.One2many('academy.course', 'teacher_id', string="Imparte:")

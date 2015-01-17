# -*- coding: utf-8 -*-
from openerp import models, fields


class biblioteca_libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Informacion de libro de la biblioteca'

    name = fields.Char('Titulo', size=255, help='Título del libro')
    active = fields.Boolean('Active', help='Activo/Inactivo')
    descripcion = fields.Text('Descripción')
    fecha_publicacion = fields.Date('Fecha', help='Fecha de publicación')
    precio = fields.Float('Precio', help='Precio de compra', digits=(10, 2))
    state = fields.Selection(
        [
            ('solicitud', 'Solicitado'),
            ('en_compra', 'Proceso de compra'),
            ('adquirido', 'Adquirido'),
            ('catalogado', 'Catalogado'),
            ('baja', 'De baja')
        ],
        'Estado',
        help='Estado actual del libro en el catálogo'
    )
    isbn = fields.Char(
        'ISBN', size=255,
        help="International Standard Book Number",
    )
    paginas = fields.Integer(
        'Número de Páginas',
        help="Número de páginas que tiene el libro",
    )
    fecha_compra = fields.Date(
        'Fecha de compra',
        help="Fecha en la que se realizó la compra del libro",
    )
    nombre_autor = fields.Char(
        'Nombre del Autor', size=255,
        help="Nombre completo del autor",
    )


class biblioteca_prestamo(models.Model):
    _name = 'biblioteca.prestamo'
    _description = 'Informacion de prestamo de libros'

    fecha = fields.Datetime(
        'Fecha del prestamo',
        help="Fecha en la que se presta el libro",
    )
    duracion_dias = fields.Integer(
        'Duración del prestamo(días)',
        help="Número días por los cuales se presta el libro",
    )
    fecha_devolucion = fields.Datetime(
        'Fecha devolución',
        help="Fecha de devolución del libro",
    )

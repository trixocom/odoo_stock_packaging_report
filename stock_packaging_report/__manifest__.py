# -*- coding: utf-8 -*-
{
    'name': 'Stock Packaging Report',
    'version': '18.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Muestra cantidad de embalajes en el reporte de stock',
    'description': """
        Stock Packaging Report
        ======================
        
        Este módulo añade una columna en el reporte de stock que muestra la cantidad
        de embalajes en lugar de la cantidad de unidades.
        
        El tamaño del embalaje es parametrizable desde:
        Configuración > Técnico > Parámetros del sistema > stock_packaging_report.packaging_size
        
        Características:
        ----------------
        * Nueva columna "Cantidad de Embalajes" en el reporte de stock
        * Parámetro de sistema configurable para definir el tamaño del embalaje
        * Cálculo automático basado en la cantidad disponible
    """,
    'author': 'Trixocom',
    'website': 'https://github.com/trixocom/odoo_stock_packaging_report',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_quant_views.xml',
        'data/system_parameters.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

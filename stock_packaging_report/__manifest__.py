# -*- coding: utf-8 -*-
{
    'name': 'Stock Packaging Report',
    'version': '18.0.5.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'Muestra cantidad de embalajes en el reporte de Existencias',
    'description': """
        Stock Packaging Report
        ======================
        
        Este módulo añade una columna "Embalajes Disponibles" en el reporte de Existencias 
        (Inventario > Reportes > Existencias) que muestra la cantidad de embalajes calculada 
        automáticamente según el tipo de embalaje configurado.
        
        Funcionamiento:
        ---------------
        1. Configure el nombre del tipo de embalaje en:
           Inventario > Configuración > Ajustes > Nombre del Embalaje para Stock
        
        2. El sistema buscará en cada producto el embalaje (product.packaging) que
           tenga ese nombre exacto.
        
        3. Utilizará el campo "qty" (Unidades por embalaje) de ese packaging para
           calcular: Stock Disponible / qty = Cantidad de Embalajes
        
        Ejemplo:
        --------
        * Configuración: Nombre del embalaje = "Caja"
        * Producto X tiene un packaging con name="Caja" y qty=12 (12 unidades por caja)
        * Stock disponible del Producto X = 144 unidades
        * Resultado mostrado = 144 / 12 = 12.0 cajas
        
        Características:
        ----------------
        * Nueva columna "Embalajes Disponibles" en Inventario > Reportes > Existencias
        * Configuración sencilla desde Ajustes de Inventario
        * Cálculo automático basado en los packagings ya definidos en Odoo
        * No requiere duplicar información: usa el qty existente en product.packaging
        * Compatible con Odoo 18 Enterprise Edition
        
        Changelog v5.0.0:
        ----------------
        * Fix CRÍTICO: Corregido el modelo - ahora usa product.product en lugar de stock.quant
        * Fix: Heredar de stock.view_stock_product_tree (vista correcta del reporte Existencias)
        * Fix: Removida dependencia de product_stock_state (no siempre está instalado)
        * El campo ahora aparece en el reporte correcto: Inventario > Reportes > Existencias
    """,
    'author': 'Trixocom',
    'website': 'https://github.com/trixocom/odoo_stock_packaging_report',
    'license': 'LGPL-3',
    'depends': ['stock', 'product'],
    'data': [
        'data/system_parameters.xml',
        'views/res_config_settings_views.xml',
        'views/product_product_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

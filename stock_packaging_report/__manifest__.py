# -*- coding: utf-8 -*-
{
    'name': 'Stock Packaging Report',
    'version': '18.0.11.5.0',
    'category': 'Inventory/Inventory',
    'summary': 'Muestra cantidad de embalajes en el reporte de Existencias y en los smart buttons del producto',
    'description': """
        Stock Packaging Report
        ======================
        
        Este módulo añade funcionalidad para mostrar cantidades en embalajes en lugar de unidades:
        
        1. Columna "Embalajes Disponibles" en el reporte de Existencias 
           (Inventario > Reportes > Existencias)
        
        2. Smart Buttons del producto modificados para mostrar embalajes:
           - "Disponible": En lugar de "5.030 U", muestra "503 Cajas"
           - "Pronosticado": En lugar de "4.890 U", muestra "489 Cajas"
           (o el nombre del embalaje configurado)
        
        Funcionamiento:
        ---------------
        1. Configure el nombre del tipo de embalaje en:
           Inventario > Configuración > Ajustes > Nombre del Embalaje para Stock
        
        2. Defina los packagings en cada producto con el nombre configurado
           (pestaña Inventario > sección Embalajes)
        
        3. El sistema calculará automáticamente:
           - Disponible: qty_available / unidades_por_embalaje
           - Pronosticado: virtual_available / unidades_por_embalaje
        
        Ejemplo:
        --------
        * Configuración: Nombre del embalaje = "Caja"
        * Producto "Azúcar" tiene packaging con name="Caja" y qty=10 (10 unidades por caja)
        * Stock disponible = 5.030 unidades → Mostrará: "503 Cajas"
        * Stock pronosticado = 4.890 unidades → Mostrará: "489 Cajas"
        
        Características:
        ----------------
        * Dos smart buttons modificados: "Disponible" y "Pronosticado"
        * Nueva columna "Embalajes Disponibles" en Inventario > Reportes > Existencias
        * Botones ensanchados para evitar amontonamiento de texto
        * Configuración sencilla desde Ajustes de Inventario
        * Cálculo automático basado en los packagings ya definidos en Odoo
        * No requiere duplicar información: usa el qty existente en product.packaging
        * Compatible con Odoo 18 Enterprise Edition
        
        Changelog v11.5.0:
        ------------------
        * FEATURE: Agregado botón "Pronosticado" con embalajes (packaging_virtual_available)
        * IMPROVE: Botones ensanchados (min-width: 140px) para evitar amontonamiento de texto
        * REFACTOR: Método auxiliar _calculate_packaging_qty para evitar duplicación de código
        * Ambos botones ahora muestran cantidad de embalajes en lugar de unidades
        
        Changelog v11.4.0:
        ------------------
        * FIX CRÍTICO: Corregido nombre del botón en Odoo 18
        * En Odoo 18 el botón se llama 'action_update_quantity_on_hand' (NO 'action_open_quants')
    """,
    'author': 'Trixocom',
    'website': 'https://github.com/trixocom/odoo_stock_packaging_report',
    'license': 'LGPL-3',
    'depends': ['stock', 'product'],
    'data': [
        'data/system_parameters.xml',
        'views/res_config_settings_views.xml',
        'views/product_product_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}

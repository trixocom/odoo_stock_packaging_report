# Cambios en la versión 2.0.0

## Resumen de cambios

Esta versión refactoriza completamente el módulo para usar el enfoque correcto basado en los packagings existentes en Odoo.

## ❌ Enfoque anterior (v1.0.0) - INCORRECTO

**Problema:** Se parametrizaba una cantidad fija de unidades por embalaje en los parámetros del sistema.

```python
# Guardaba un número fijo (ej: 12.0)
packaging_size = 12.0  

# Calculaba: Stock / número fijo
packaging_quantity = available_quantity / packaging_size
```

**Desventajas:**
- Duplicaba información que ya existe en `product.packaging`
- Cada producto podría tener diferentes cantidades por embalaje
- No aprovechaba la funcionalidad nativa de Odoo

## ✅ Enfoque nuevo (v2.0.0) - CORRECTO

**Solución:** Se usa el campo `qty` que ya existe en `product.packaging`.

```python
# Guarda el NOMBRE del tipo de embalaje (ej: "Caja")
packaging_name = "Caja"

# Busca el packaging con ese nombre para cada producto
packaging = product.packaging.search([
    ('product_id', '=', product.id),
    ('name', '=', packaging_name)
])

# Usa el qty (unidades por embalaje) de ese packaging
packaging_quantity = available_quantity / packaging.qty
```

**Ventajas:**
- ✅ No duplica información
- ✅ Usa datos ya existentes en Odoo
- ✅ Cada producto puede tener su propio qty de embalaje
- ✅ Flexible para diferentes tipos de embalaje (Caja, Pallet, Bulto, etc.)

## 📋 Archivos modificados

### 1. `models/stock_quant.py`
**Cambio principal:** El método `_compute_packaging_quantity` ahora:
- Lee el parámetro `packaging_name` (en lugar de `packaging_size`)
- Busca el `product.packaging` que coincida con ese nombre
- Usa el campo `qty` de ese packaging para el cálculo

**Antes:**
```python
packaging_size = float(get_param('stock_packaging_report.packaging_size'))
packaging_quantity = available_quantity / packaging_size
```

**Ahora:**
```python
packaging_name = get_param('stock_packaging_report.packaging_name')
packaging = env['product.packaging'].search([
    ('product_id', '=', product_id),
    ('name', '=', packaging_name)
])
packaging_quantity = available_quantity / packaging.qty
```

### 2. `models/res_config_settings.py` (NUEVO)
- Añade interfaz amigable en Ajustes de Inventario
- Campo `packaging_name_for_stock` para configurar el nombre del embalaje
- Tooltips explicativos del funcionamiento

### 3. `data/system_parameters.xml`
**Antes:**
```xml
<field name="key">stock_packaging_report.packaging_size</field>
<field name="value">1.0</field>
```

**Ahora:**
```xml
<field name="key">stock_packaging_report.packaging_name</field>
<field name="value">Caja</field>
```

### 4. `views/res_config_settings_views.xml` (NUEVO)
- Nueva vista de configuración en Inventario > Configuración > Ajustes
- Sección "Reporte de Embalajes en Stock"
- Explicación visual del funcionamiento

### 5. `__manifest__.py`
- Actualizada versión a 18.0.2.0.0
- Añadida dependencia a módulo `product`
- Documentación actualizada
- Referencia al nuevo archivo de vista de configuración

### 6. `README.md`
- Documentación completa reescrita
- Ejemplos prácticos paso a paso
- Sección de "Cómo funciona"
- Casos de uso detallados
- Notas importantes sobre el uso

## 🔧 Cómo migrar desde v1.0.0

Si ya tenías instalada la versión anterior:

1. **Actualiza el módulo:**
   ```bash
   cd /ruta/a/odoo/addons/stock_packaging_report
   git pull origin main
   ```

2. **Actualiza en Odoo:**
   - Ve a Aplicaciones
   - Busca "Stock Packaging Report"
   - Haz clic en "Actualizar"

3. **Reconfigura el parámetro:**
   - Ve a: Inventario > Configuración > Ajustes
   - En "Reporte de Embalajes en Stock"
   - Configura el nombre del embalaje (ej: "Caja")
   - El parámetro anterior `packaging_size` ya no se usa

4. **Verifica tus packagings:**
   - Revisa que cada producto tenga configurado un packaging con el nombre correcto
   - El packaging debe tener el campo `qty` con el valor de unidades por embalaje

## 📝 Ejemplo completo

### Configuración:

1. **En Ajustes:**
   - Nombre del Embalaje para Stock = `"Caja"`

2. **Producto: Tornillo M6**
   - Ve a: Inventario > Productos > Productos > Tornillo M6
   - Pestaña "Inventario" > Sección "Embalajes"
   - Crea/edita un packaging:
     - Nombre: `Caja`
     - Cantidad: `100` (100 tornillos por caja)

3. **Stock actual:**
   - Ubicación: WH/Stock
   - Cantidad disponible: 2,500 tornillos

### Resultado:

En el reporte de stock verás:
- **Cantidad Disponible:** 2,500.00
- **Cantidad de Embalajes:** 25.00 (2500 / 100 = 25 cajas)

## 🎯 Ventajas de este cambio

1. **Simplicidad:** No hay que mantener dos fuentes de verdad
2. **Flexibilidad:** Cada producto puede tener diferentes unidades por embalaje
3. **Escalabilidad:** Fácil cambiar entre tipos de embalaje (Caja, Pallet, etc.)
4. **Mantenibilidad:** Usa funcionalidad nativa de Odoo
5. **Precisión:** Los datos siempre están sincronizados

## ⚠️ Consideraciones importantes

1. **Nombre exacto:** El nombre del packaging debe coincidir EXACTAMENTE (case-sensitive)
   - ✅ Correcto: `Caja` = `Caja`
   - ❌ Incorrecto: `Caja` ≠ `caja` ≠ `CAJA`

2. **Sin packaging:** Si un producto no tiene el packaging configurado, mostrará 0.0

3. **Múltiples packagings:** Solo se usa el que coincida con el nombre configurado

## 🔗 Referencias

- Documentación de Odoo sobre Packagings: https://www.odoo.com/documentation/18.0/applications/inventory_and_mrp/inventory/product_management/product_replenishment/uom.html
- Modelo `product.packaging`: https://github.com/odoo/odoo/blob/18.0/addons/product/models/product_packaging.py

---

**Versión:** 2.0.0  
**Fecha:** 2025-10-11  
**Autor:** Trixocom

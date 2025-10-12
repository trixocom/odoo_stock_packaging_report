# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [4.0.0] - 2025-10-12

### 🔧 Correcciones (Fixed)
- **XPath en vistas:** Corregidos los XPath para usar `//field[@name='available_quantity']` en lugar de `//list/field[@name='product_uom_id']`
  - Esto soluciona el problema donde la columna no se mostraba en las vistas
  - La columna ahora se posiciona correctamente después de "Cantidad Disponible"

### 🧹 Limpieza (Removed)
- Removida dependencia innecesaria `product_stock_state` del manifest
- Removida vista `product_product_views.xml` del manifest (archivo existe pero no se usa)

### 📝 Documentación (Documentation)
- README completamente reescrito con:
  - Instrucciones de instalación paso a paso
  - Ejemplos prácticos de uso
  - Guía de troubleshooting
  - Estructura del proyecto explicada
- Añadido CHANGELOG.md para seguir los cambios del proyecto

### 🎯 Mejoras (Changed)
- Orden de archivos en el manifest reorganizado para mejor legibilidad
- Versión actualizada a 4.0.0 para reflejar correcciones importantes

---

## [3.0.0] - 2025-10-11

### ✨ Nuevas características (Added)
- Añadido campo calculado `packaging_quantity_available` en el modelo `product.product`
  - Permite ver la cantidad de embalajes directamente en la vista de producto
- Añadido archivo `models/product_product.py` con el nuevo campo
- Añadido archivo `views/product_product_views.xml` (no utilizado en esta versión)

### 🔧 Dependencias (Changed)
- Añadida dependencia `product_stock_state` al manifest

### 📝 Notas
Esta versión añade funcionalidad extra al módulo que no se está usando completamente.
En la versión 4.0.0 se limpia esta implementación.

---

## [2.0.0] - 2025-10-11

### 🎉 Refactorización completa (Changed)

#### ⚠️ BREAKING CHANGES
- **Cambio fundamental en el enfoque:**
  - **Antes (v1.x):** Se parametrizaba una cantidad fija de unidades por embalaje
  - **Ahora (v2.x):** Se parametriza el NOMBRE del tipo de embalaje y se usa el `qty` de `product.packaging`

#### ✨ Nuevas características (Added)
- Configuración por nombre de packaging en lugar de cantidad fija
- Búsqueda dinámica del packaging correcto para cada producto
- Uso del campo `qty` nativo de `product.packaging`
- Interfaz de configuración mejorada en Ajustes de Inventario

#### 🔧 Correcciones (Fixed)
- Ya no se duplica información: aprovecha los packagings existentes en Odoo
- Cada producto puede tener diferentes cantidades por embalaje
- Solución más elegante y alineada con la filosofía de Odoo

#### 📝 Archivos modificados
- `models/stock_quant.py`: Lógica de cálculo completamente reescrita
- `models/res_config_settings.py`: Campo cambiado de Float a Char para nombre
- `data/system_parameters.xml`: Parámetro cambiado a `packaging_name`
- `views/res_config_settings_views.xml`: Nueva interfaz más descriptiva
- `__manifest__.py`: Descripción actualizada con el nuevo funcionamiento

#### 💡 Ejemplo del cambio
```python
# ❌ Antes (v1.0)
packaging_size = 12.0  # Valor fijo configurado
qty_packaging = available_qty / packaging_size

# ✅ Ahora (v2.0)
packaging = search([('name', '=', 'Caja')])  # Busca por nombre
qty_packaging = available_qty / packaging.qty  # Usa qty del packaging
```

---

## [1.0.0] - 2025-10-10

### 🎉 Lanzamiento inicial (Added)

#### ✨ Características principales
- Campo calculado `packaging_quantity` en el modelo `stock.quant`
- Nueva columna "Cantidad de Embalajes" en reportes de stock
- Configuración de cantidad de unidades por embalaje en Ajustes
- Cálculo automático basado en stock disponible

#### 📁 Estructura del módulo
- `models/stock_quant.py`: Modelo con campo calculado
- `models/res_config_settings.py`: Configuración del módulo
- `views/stock_quant_views.xml`: Vista con nueva columna
- `views/res_config_settings_views.xml`: Interfaz de configuración
- `data/system_parameters.xml`: Parámetros del sistema
- `__manifest__.py`: Manifest del módulo

#### 🎯 Funcionalidad
- Permite configurar una cantidad fija de unidades por embalaje
- Calcula automáticamente: `Stock Disponible / Unidades por Embalaje`
- Muestra el resultado en una nueva columna en las vistas de stock

#### ⚠️ Limitaciones (resueltas en v2.0)
- Cantidad de unidades por embalaje era global para todos los productos
- No aprovechaba los packagings ya definidos en Odoo
- Duplicaba información que ya existía en el sistema

---

## Tipos de cambios

- **Added** (✨ Nuevas características): para funcionalidades nuevas
- **Changed** (🎯 Mejoras): para cambios en funcionalidades existentes
- **Deprecated** (⚠️ Obsoleto): para características que se eliminarán pronto
- **Removed** (🧹 Limpieza): para características eliminadas
- **Fixed** (🔧 Correcciones): para corrección de bugs
- **Security** (🔒 Seguridad): para correcciones de vulnerabilidades

---

## Enlaces

- [GitHub Repository](https://github.com/trixocom/odoo_stock_packaging_report)
- [Issues](https://github.com/trixocom/odoo_stock_packaging_report/issues)
- [Releases](https://github.com/trixocom/odoo_stock_packaging_report/releases)

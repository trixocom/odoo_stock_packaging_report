# Stock Packaging Report - Módulo Odoo 18

[![License: LGPL-3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![Odoo Version](https://img.shields.io/badge/Odoo-18.0-875A7B.svg)](https://www.odoo.com/)
[![Version](https://img.shields.io/badge/version-4.0.0-brightgreen.svg)](https://github.com/trixocom/odoo_stock_packaging_report)

## 📦 Descripción

Este módulo añade una columna en el reporte de stock (Existencias) que muestra la **cantidad de embalajes** calculada automáticamente según el tipo de embalaje configurado.

### ✨ Características principales

- ✅ **Nueva columna "Cantidad de Embalajes"** en reportes de stock.quant
- ✅ **Configuración sencilla** desde Ajustes de Inventario
- ✅ **Cálculo automático** basado en los packagings ya definidos en Odoo
- ✅ **No duplica información**: usa el `qty` existente en `product.packaging`
- ✅ Compatible con **Odoo 18.0**

---

## 🚀 Funcionamiento

### Paso 1: Configuración

1. Ve a: **Inventario > Configuración > Ajustes**
2. Busca la sección: **"Reporte de Embalajes en Stock"**
3. Configura el campo: **"Nombre del Embalaje para Stock"**
   - Ejemplo: `Caja`, `Pallet`, `Bulto`, etc.

![Configuración](https://via.placeholder.com/800x200?text=Configuración+del+módulo)

### Paso 2: Sistema busca el packaging

El sistema buscará en cada producto el embalaje (`product.packaging`) que tenga ese nombre exacto.

### Paso 3: Cálculo automático

Utilizará el campo **`qty`** (Unidades por embalaje) de ese packaging para calcular:

```
Cantidad de Embalajes = Stock Disponible / qty (unidades por embalaje)
```

---

## 💡 Ejemplo práctico

### Configuración
- **Nombre del embalaje configurado:** `"Caja"`

### Producto X
- Tiene un packaging con:
  - `name = "Caja"`
  - `qty = 12` (12 unidades por caja)
- **Stock disponible:** 144 unidades

### Resultado
```
144 unidades / 12 unidades por caja = 12.0 cajas
```

La columna "Cantidad de Embalajes" mostrará: **12.0**

---

## 📋 Instalación

### Método 1: Desde interfaz de Odoo

1. Copia el módulo en tu carpeta de addons:
   ```bash
   cd /path/to/odoo/addons
   git clone https://github.com/trixocom/odoo_stock_packaging_report.git
   ```

2. Actualiza la lista de aplicaciones:
   - Ve a **Aplicaciones**
   - Elimina el filtro "Apps"
   - Busca "Stock Packaging Report"
   - Haz clic en **Instalar**

### Método 2: Desde línea de comandos

```bash
cd /path/to/odoo
./odoo-bin -d tu_base_de_datos -i stock_packaging_report --stop-after-init
```

---

## 🔄 Actualización

Si ya tienes una versión anterior instalada:

### Desde interfaz
1. Ve a **Aplicaciones**
2. Busca "Stock Packaging Report"
3. Haz clic en **Actualizar**

### Desde línea de comandos
```bash
cd /path/to/odoo/addons/odoo_stock_packaging_report
git pull origin main

cd /path/to/odoo
./odoo-bin -d tu_base_de_datos -u stock_packaging_report --stop-after-init
```

---

## 📁 Estructura del módulo

```
stock_packaging_report/
├── __init__.py                          # Inicialización del módulo
├── __manifest__.py                      # Manifest del módulo
│
├── models/
│   ├── __init__.py                      # Inicialización de modelos
│   ├── stock_quant.py                   # ⭐ Modelo principal - Añade campo packaging_quantity
│   ├── res_config_settings.py           # Configuración del módulo
│   └── product_product.py               # Campo adicional en product (opcional)
│
├── views/
│   ├── stock_quant_views.xml            # ⭐ Vista principal - Columna en reportes de stock
│   ├── res_config_settings_views.xml    # Vista de configuración
│   └── product_product_views.xml        # Vista de producto (opcional, sin usar)
│
├── data/
│   └── system_parameters.xml            # Parámetros del sistema
│
├── README.md                            # Este archivo
└── CHANGELOG.md                         # Historial de cambios
```

### ⭐ Archivos principales

| Archivo | Descripción |
|---------|-------------|
| `models/stock_quant.py` | Añade el campo calculado `packaging_quantity` al modelo `stock.quant` |
| `views/stock_quant_views.xml` | Añade la columna "Cantidad de Embalajes" en las vistas tree de stock |
| `models/res_config_settings.py` | Configuración para definir el nombre del embalaje |
| `views/res_config_settings_views.xml` | Interfaz de configuración en Ajustes de Inventario |

---

## 🔧 Uso

### Ver la columna en reportes de stock

1. Ve a: **Inventario > Reportes > Existencias**
2. Verás la nueva columna: **"Cantidad de Embalajes"**
3. Si no la ves, haz clic en el icono de columnas (☰) y actívala

### Configurar packagings en productos

Para que el cálculo funcione correctamente:

1. Ve a: **Inventario > Productos > Productos**
2. Abre un producto
3. Ve a la pestaña: **Inventario**
4. En la sección **"Empaquetado"**, añade un packaging:
   - **Nombre:** `Caja` (debe coincidir exactamente con la configuración)
   - **Unidades por embalaje (qty):** `12`

---

## 📊 Dependencias

- `stock` - Módulo de inventario de Odoo
- `product` - Módulo de productos de Odoo

---

## 🐛 Problemas conocidos

### La columna no aparece

**Solución 1:** Activa la columna manualmente
- Haz clic en el icono de columnas (☰) en la vista tree
- Busca "Cantidad de Embalajes"
- Actívala

**Solución 2:** Actualiza el módulo
```bash
./odoo-bin -d tu_bd -u stock_packaging_report --stop-after-init
```

### El cálculo muestra 0.0

**Causas posibles:**
1. No has configurado el nombre del embalaje en Ajustes
2. El producto no tiene un packaging con ese nombre exacto
3. El packaging tiene `qty = 0` o negativo

**Solución:**
- Verifica la configuración en Inventario > Configuración > Ajustes
- Verifica que el producto tenga un packaging con el nombre correcto
- Verifica que el packaging tenga un `qty` mayor a 0

---

## 📝 Changelog

### Version 4.0.0 (2025-10-12)
- ✅ **Fix:** Corregidos los XPath en las vistas para usar `//field` en lugar de `//list/field`
- ✅ **Fix:** La columna ahora se posiciona después de `available_quantity`
- ✅ **Mejora:** Removidas dependencias innecesarias (`product_stock_state`)
- ✅ **Limpieza:** Reorganización de archivos en el manifest

### Version 3.0.0 (2025-10-11)
- ✅ Añadido campo en `product.product` para ver embalajes en vista de producto
- ✅ Añadida dependencia `product_stock_state`

### Version 2.0.0 (2025-10-11)
- ✅ Refactorización completa del módulo
- ✅ Ahora usa el nombre del packaging en lugar de un valor fijo
- ✅ Búsqueda dinámica del packaging por nombre
- ✅ Uso del campo `qty` existente en `product.packaging`

### Version 1.0.0 (2025-10-10)
- ✅ Versión inicial del módulo

---

## 👥 Autor

**Trixocom**
- GitHub: [@trixocom](https://github.com/trixocom)
- Website: [https://github.com/trixocom/odoo_stock_packaging_report](https://github.com/trixocom/odoo_stock_packaging_report)

---

## 📄 Licencia

Este módulo está licenciado bajo [LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.html).

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún bug o tienes alguna mejora:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 💬 Soporte

Si tienes alguna pregunta o necesitas ayuda:

- 🐛 [Reportar un bug](https://github.com/trixocom/odoo_stock_packaging_report/issues)
- 💡 [Solicitar una feature](https://github.com/trixocom/odoo_stock_packaging_report/issues)
- 📖 [Ver la documentación](https://github.com/trixocom/odoo_stock_packaging_report)

---

⭐ Si este módulo te fue útil, ¡no olvides darle una estrella en GitHub!

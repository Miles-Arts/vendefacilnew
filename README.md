# Vende-Fácil

Vende-Fácil es una aplicación desarrollada para facilitar la conexión entre vendedores de productos agrícolas y compradores de alimentos del campo. Su propósito principal es actuar como intermediaria digital, permitiendo la gestión eficiente de ventas, compras, productos y usuarios dentro del ecosistema agrícola.

---

## Descripción del Proyecto

Vende-Fácil maneja distintos tipos de usuarios (**clientes** y **vendedores**), así como el registro de productos con sus características específicas (tipo, tamaño, precio, disponibilidad). También permite realizar ventas y compras, y relacionarlas con los productos comercializados.

> **Nota:** Este proyecto es exclusivamente para fines de aprendizaje y corresponde a un proyecto de estudios del programa Tecnólogo en Análisis y Desarrollo de Software del SENA. No debe ser utilizado en producción ni para fines comerciales.

---

## Índice

- [Descripción del Proyecto](#descripción-del-proyecto)
- [Crear y activar entorno virtual (Windows)](#crear-y-activar-entorno-virtual-windows)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
- [Migraciones de Base de Datos](#migraciones-de-base-de-datos)
- [Uso](#uso)
- [Ejecutar tests](#ejecutar-tests)
- [Recopilar archivos estáticos](#recopilar-archivos-estáticos)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Sistema Operativo](#sistema-operativo)
- [Conexión a la Base de Datos PostgreSQL](#conexión-a-la-base-de-datos-postgresql)
- [Solución a Errores Comunes](#solución-a-errores-comunes)
- [Metodología de Trabajo](#metodología-de-trabajo)
- [Arquitectura del Proyecto](#arquitectura-del-proyecto)
- [ORM (Object Relational Mapping)](#orm-object-relational-mapping)
- [Patrón de Arquitectura MTV (Modelo-Plantilla-Vista)](#patrón-de-arquitectura-mtv-modelo-plantilla-vista)
- [Importar Funciones Esenciales en las Vistas](#importar-funciones-esenciales-en-las-vistas) ## Bootstrap5 template pack para django-crispy-forms
- [Bootstrap5 template pack para django-crispy-forms](#Bootstrap5-template-pack-para-django-crispy-forms)
- [Ejemplo de Base de Datos](#ejemplo-de-base-de-datos)
- [Contribución](#contribución)
- [Recursos Adicionales](#recursos-adicionales)
- [Versión del Proyecto](#versión-del-proyecto) 
- [Autor e Institución](#autor-e-institución)
- [Licencia](#licencia)

---

## Crear y activar entorno virtual (Windows)

1. Abre una terminal y navega a la ruta de tu proyecto:
   ```bash
   cd /p/GITHUB/PROYECTOS/VENDEFACILNEW/VendeFacil
   ```

2. Crea el entorno virtual:
   ```bash
   python -m venv venv
   ```

3. Activa el entorno virtual:
   ```bash
   source venv/Scripts/activate
   ```

Ahora puedes instalar dependencias y ejecutar tu proyecto dentro del entorno virtual.

## Requisitos
- Python 3.8 o superior
- pip

## Instalación
1. Clona el repositorio:
   ```bash
   git clone https://github.com/Miles-Arts/vendefacilnew.git
   cd vendefacilnew/VendeFacil
   ```
2. Crea y activa el entorno virtual (Windows PowerShell / Git Bash):
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Git Bash
   # o en PowerShell:
   # .\venv\Scripts\Activate.ps1
   ```
   Con esto, puedes instalar dependencias y ejecutar tu proyecto dentro del entorno virtual.
3. Instala las dependencias:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Configuración de Variables de Entorno
Antes de ejecutar la aplicación, debes crear una carpeta llamada `.env` en la raíz del proyecto. Dentro de esta carpeta, crea un archivo para definir las variables de entorno necesarias para la conexión a la base de datos y la seguridad de la aplicación. Ejemplo de variables que debes agregar:

```env
SECRET_KEY=tu_clave_secreta
PGSQL_HOST=localhost
PGSQL_USER=postgres
PGSQL_PASSWORD=tu_contraseña
PGSQL_DATABASE=VendeFacil
```

## Migraciones de Base de Datos
Para gestionar los cambios en el esquema de tu base de datos, sigue estos pasos:
1.  Crea los archivos de migración basados en los cambios de tus modelos:
    ```bash
    python manage.py makemigrations
    ```
2.  Aplica las migraciones para actualizar la base de datos:
    ```bash
    python manage.py migrate
    ```

## Uso
Para levantar el servidor de desarrollo:
```bash
python manage.py runserver
```

## Ejecutar tests
```bash
python manage.py test
```

## Recopilar archivos estáticos
```bash
python manage.py collectstatic
```

## Licencia
Este proyecto está licenciado bajo la [MIT License](LICENSE).


## Tecnologías Utilizadas

### Backend
- Django
- JSON
- PostgreSQL
- ENV o VENV
- Postman

### Frontend
- HTML
- CSS
- JavaScript
- Bootstrap

### Herramientas de Desarrollo
- Git
- GitHub
- Visual Studio Code
- Copilot Pro
- Canva
- Creadores de UML

---

## Sistema Operativo
- **Windows 11**
---

## Conexión a la Base de Datos PostgreSQL

- **Host:** localhost
- **Usuario:** postgres
- **Contraseña:** 1234
- **Base de datos:** VendeFacil
- **Puerto:** 5432

---

## Solución a Errores Comunes

- Verifica las rutas en el navegador.
- Cierra y abre Visual Studio Code si los cambios no se reflejan.
- Actualiza la página web con `Ctrl + F5`.
- Reinicia el servidor local si es necesario.
- Cierra y abre una nueva terminal si el entorno virtual no funciona correctamente.

---

## Metodología de Trabajo

Este proyecto utiliza la metodología **Kanban** para la gestión y organización de tareas. Kanban permite visualizar el flujo de trabajo, identificar cuellos de botella y mejorar la eficiencia del equipo.

---

## Arquitectura del Proyecto

El proyecto sigue la estructura estándar de Django y utiliza una arquitectura **MVC (Modelo-Vista-Controlador)** implícita en el patrón **MTV (Modelo-Plantilla-Vista)** de Django:

- **VendeFacil/**: Contiene la configuración principal del proyecto (`settings.py`, `urls.py`, etc.).
- **Productos/** (y otras apps): Cada aplicación Django gestiona una funcionalidad específica (ej. productos). Contiene:
    - **models.py (Modelo):** Define la estructura de los datos y la interacción con la base de datos.
    - **views.py (Vista en MTV, Controlador en MVC):** Maneja la lógica de la aplicación, procesa las solicitudes HTTP y conecta los modelos con las plantillas.
    - **templates/ (Plantilla):** Archivos HTML que definen la presentación de la interfaz de usuario.
    - **static/**: Archivos estáticos como CSS, JavaScript e imágenes.
    - **urls.py**: Define las rutas URL específicas de la aplicación.

Esta arquitectura permite separar responsabilidades, facilitando el mantenimiento y la escalabilidad del proyecto.

---

## ORM (Object Relational Mapping)

El proyecto utiliza un **ORM (Object Relational Mapping)** para interactuar con la base de datos de manera eficiente y simplificada. Esto permite trabajar con modelos de datos en lugar de escribir consultas SQL directamente, facilitando el desarrollo y mantenimiento del proyecto.

---

## Patrón de Arquitectura MTV (Modelo-Plantilla-Vista)

El proyecto sigue el patrón de arquitectura **MTV (Modelo-Plantilla-Vista)**, que organiza el código en tres componentes principales:

- **Modelo (Model):** Gestiona la lógica de datos y la interacción con la base de datos.
- **Plantilla (Template):** Define la presentación de la interfaz de usuario mediante archivos HTML.
- **Vista (View):** Controla la lógica de la aplicación y conecta los modelos con las plantillas.

Este patrón facilita la separación de responsabilidades, mejorando la escalabilidad y el mantenimiento del proyecto.

---

## Importar Funciones Esenciales en las Vistas

En las vistas de Django, es común utilizar las funciones `render` y `redirect` para manejar la lógica de las respuestas HTTP:

- **`render`**: Se utiliza para renderizar plantillas HTML y devolverlas como respuesta al navegador. Es necesario importarla desde `django.shortcuts`.
- **`redirect`**: Se utiliza para redirigir al usuario a otra URL. También se importa desde `django.shortcuts`.

### Ejemplo de Importación:
```python
from django.shortcuts import render, redirect
```

Estas funciones son fundamentales para manejar la interacción entre las vistas y las plantillas en un proyecto Django.

---

## Bootstrap5 template pack para django-crispy-forms

### Instalación

Instala este plugin usando pip:

```bash
$ pip install crispy-bootstrap5
```

### Uso

Debes actualizar el archivo de configuración (`settings.py`) de tu proyecto para agregar `crispy_forms` y `crispy_bootstrap5` a `INSTALLED_APPS`. También debes establecer `bootstrap5` como un template pack permitido y como el template pack por defecto para tu proyecto:

```python
INSTALLED_APPS = (
    ...
    "crispy_forms",
    "crispy_bootstrap5",
    ...
)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"
```

---

## Ejemplo de Base de Datos

A continuación, se presenta un ejemplo de script para la creación de tablas en PostgreSQL que se utilizarán en el proyecto:

```sql
-- Script de creación de tablas para PostgreSQL
-- Tablas: id_personas y productos

CREATE TABLE id_personas (
    documento INT NOT NULL PRIMARY KEY,
    nombres CHAR(250) NOT NULL,
    apellidos CHAR(250) NOT NULL,
    correo VARCHAR(250) NOT NULL,
    metodo_de_pago INT NOT NULL,
    fecha_nacimiento DATE NOT NULL,
    direccion VARCHAR(250) NOT NULL,
    celular VARCHAR(250) NOT NULL
);

CREATE TABLE productos (
    id_producto INT NOT NULL PRIMARY KEY,
    categoria_producto INT NOT NULL,
    id_compra FLOAT NOT NULL,
    caracteristicas_producto VARCHAR(250) NOT NULL,
    tipo_producto INT NOT NULL,
    tamaño_producto INT NOT NULL,
    precio_producto FLOAT NOT NULL,
    mes_del_producto INT NOT NULL,
    nombre_producto VARCHAR(250) NOT NULL
);
```

---

## Contribución

Si deseas contribuir al proyecto, sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tu funcionalidad o corrección de errores:
   ```bash
   git checkout -b nombre-de-tu-rama
   ```
3. Realiza tus cambios y haz commits descriptivos:
   ```bash
   git commit -m "Descripción de tu cambio"
   ```
4. Sube tus cambios a tu repositorio fork:
   ```bash
   git push origin nombre-de-tu-rama
   ```
5. Abre un pull request en el repositorio original.

---

## Recursos Adicionales

- [Documentación oficial de Django](https://docs.djangoproject.com/)
- [Documentación de Bootstrap](https://getbootstrap.com/)
- [Guía de Git y GitHub](https://guides.github.com/)

---

## Versión del Proyecto

Actualmente en la versión **0.0.1** (etapa temprana de desarrollo). Se sigue el esquema de versionado semántico.

---

## Iconos Redes Sociales

https://www.flaticon.es/autores/grow-studio

---

## Autor e Institución

- **Autor:** Milton Figueredo ([LinkedIn](https://www.linkedin.com/in/milton-figueredo-miles-arts/) | [GitHub](https://github.com/Miles-Arts))
- **Institución:** SENA - Servicio Nacional de Aprendizaje
- **Programa:** Tecnólogo en Análisis y Desarrollo de Software
- **Fecha:** Mayo 2025

---

## Licencia

Este proyecto está licenciado bajo la **Licencia MIT**.

© 2025 Milton Figueredo

---
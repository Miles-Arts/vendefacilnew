# Instrucciones para Contribuir al Proyecto Vende-Fácil

Este archivo contiene las instrucciones necesarias para trabajar en el proyecto Vende-Fácil. Sigue estas pautas para garantizar un flujo de trabajo eficiente y organizado.

---

## Flujo de trabajo de Git
1. Realiza los siguientes pasos cada vez que escribas "push":
    - La rama de trabajo actual es `milton_figueredo`.
   - Ejecuta `git add .` para añadir todos los cambios.
   - Realiza un commit con un mensaje descriptivo, por ejemplo: `git commit -m "Descripción del cambio"`.
   - Haz un push al repositorio remoto con `git push`.
   - Crea un pull request para integrar los cambios.

2. Antes de realizar cualquier cambio en el código o archivos:
   - Verifica que no generen conflictos con el código existente.
   - Si detectas conflictos, sugiere o propone soluciones.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalados los siguientes elementos:

- **Python 3.10 o superior**
- **PostgreSQL**
- **Git**
- **Entorno virtual (virtualenv)**

---

## Configuración del Entorno de Desarrollo

1. **Clona el repositorio:**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd VendeFacil
   ```

2. **Crea un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura las variables de entorno:**
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
   ```env
   SECRET_KEY=tu_clave_secreta
   PGSQL_HOST=localhost
   PGSQL_USER=postgres
   PGSQL_PASSWORD=tu_contraseña
   PGSQL_DATABASE=VendeFacil
   ```

5. **Realiza las migraciones de la base de datos:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

---

## Flujo de Trabajo con Git

1. **Crea una nueva rama para tu tarea:**
   ```bash
   git checkout -b nombre-de-la-rama
   ```

2. **Realiza tus cambios y confirma los commits:**
   ```bash
   git add .
   git commit -m "Descripción de los cambios"
   ```

3. **Sube tu rama al repositorio remoto:**
   ```bash
   git push -u origin nombre-de-la-rama
   ```

4. **Crea un Pull Request (PR):**
   Ve al repositorio en GitHub y crea un PR para que tus cambios sean revisados.

---

## Crear Carpetas desde la Terminal Bash

Puedes crear carpetas para organizar tu proyecto directamente desde la terminal Bash utilizando el comando `mkdir`. Por ejemplo:

```bash
mkdir nombre_de_la_carpeta
```

Esto creará una nueva carpeta con el nombre especificado en el directorio actual. Puedes usar este comando para estructurar tu proyecto de manera eficiente.

---

## Solución de Problemas

- **El entorno virtual no funciona:** Cierra y abre una nueva terminal, luego activa el entorno virtual nuevamente.
- **Los cambios no se reflejan en el navegador:** Actualiza la página con `Ctrl + F5` o reinicia el servidor local.
- **Errores de conexión a la base de datos:** Verifica las credenciales en el archivo `.env`.

---

## Buenas Prácticas

- Sigue la arquitectura **MVC** (Modelo-Vista-Controlador) para mantener el código organizado.
- Escribe mensajes de commit claros y descriptivos.
- Asegúrate de que tu código pase las pruebas antes de enviar un PR.

---

### Entorno de Desarrollo
- Sistema Operativo: Windows
- Editor de Código: Visual Studio Code
- Navegador: Cualquier navegador compatible con HTML5

### Notas
Este stack puede expandirse en el futuro según las necesidades del proyecto.

## Metodología de Trabajo
El proyecto utiliza la metodología **Kanban** para la gestión de tareas. Esto permite visualizar el flujo de trabajo, identificar cuellos de botella y mejorar la eficiencia del equipo.

## Versionado del Proyecto
El proyecto sigue el esquema de versionado semántico. La versión actual es **0.0.1**, lo que indica que está en una etapa temprana de desarrollo.

## Notas adicionales
- Siempre sigue las mejores prácticas de código según los lenguajes utilizados en el proyecto.
- Responde en español primero.

## Contacto

Si tienes preguntas o necesitas ayuda, contacta al autor del proyecto:

- **Autor:** Milton Figueredo
- **Correo:** [tu_correo@example.com](milton_figueredo@soy.sena.edu.co)
- **LinkedIn:** [Perfil de LinkedIn](https://www.linkedin.com/in/milton-figueredo-miles-arts/)
- **GitHub:** [Perfil de GitHub](https://github.com/Miles-Arts)

---

¡Gracias por contribuir al proyecto Vende-Fácil!

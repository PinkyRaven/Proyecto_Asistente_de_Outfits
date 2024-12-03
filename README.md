# Asistente Virtual de Outfits de Moda con OpenAI y DALL-E

## Introducción
### Nombre del Proyecto
Asistente Virtual de Outfits de Moda con OpenAI y DALL-E

### Presentación del Problema
Los usuarios suelen encontrar difícil visualizar outfits personalizados utilizando herramientas de IA debido a la necesidad de escribir prompts detallados y precisos. Esto puede limitar la accesibilidad y creatividad de quienes desean explorar opciones de moda.

### Propuesta de Solución
Este proyecto ofrece una solución interactiva que automatiza la generación de prompts basados en las selecciones del usuario, permitiendo obtener imágenes generadas automáticamente por DALL-E de manera sencilla y visual.

## Objetivos
- Crear una interfaz amigable para seleccionar prendas y accesorios.
- Automatizar la generación de prompts para la API de DALL-E.
- Proporcionar visualizaciones de outfits personalizadas basadas en elecciones de los usuarios.

## Metodología
1. **Interfaz de Usuario**: Implementar una página web interactiva para la selección de prendas.
2. **Backend**: Utilizar Flask para procesar las selecciones y generar prompts dinámicos.
3. **Integración con OpenAI**: Generar imágenes de outfits utilizando DALL-E.

## Herramientas y Tecnologías
- Lenguaje: Python (Flask).
- API: OpenAI GPT-3.5 y DALL-E.
- Frontend: HTML, CSS, JavaScript.

---

## Instrucciones para Ejecutar el Proyecto

1. Instala las dependencias necesarias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicia la aplicación:
   ```bash
   python src/app.py
   ```
3. Abre tu navegador y accede a `http://127.0.0.1:5000`.

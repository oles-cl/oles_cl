# Recomendaciones Netlify (plan básico)

Tu sitio se publica desde la carpeta `docs`. Este archivo está en la raíz del repo (no se publica).

## Límites del plan gratuito (referencia)

- **Ancho de banda:** 100 GB/mes  
- **Almacenamiento:** 10 GB  
- **Minutos de build:** 300/mes (si usas build en Netlify)

## Qué ya está hecho

- **`netlify.toml`** en la raíz con cabeceras de **caché**:
  - Imágenes y assets estáticos: caché largo (1 año) → menos GB en visitas repetidas.
  - HTML: revalidación en cada visita.
  - CSS/JS: 1 día con revalidación en segundo plano.

## Recomendaciones para que “aguante” bien

### 1. Reducir peso del sitio (prioritario)

- **Video en la portada:** solo `images/logos/download.mp4`. Si puedes:
  - Dejar solo **una** versión en MP4 (mejor compatibilidad y menor tamaño).
  - Comprimir el video (resolución moderada, bitrate bajo) o subirlo a YouTube/Vimeo y embeber.
- **Imágenes:** Comprimir fotos (equipo, noticias) antes de subir. Herramientas: [Squoosh](https://squoosh.app), TinyPNG.
- **Evitar** subir a `docs/` archivos que no use el sitio (.RData, .mov de respaldo, etc.).

### 2. No usar build en Netlify (como ahora)

- Dejar **Build command** vacío y publicar la carpeta **docs** ya generada en tu máquina.
- Así no gastas minutos de build. Flujo: en local `Rscript compilar_publicaciones_perfiles.R` + `quarto render`, luego commit de `docs/` y push.

### 3. Revisar uso en el panel de Netlify

- En **Site configuration → Usage** (o Billing) ves ancho de banda y almacenamiento.
- Netlify avisa al 50%, 75% y 90% del límite.

### 4. Si en el futuro quieres build en Netlify

- El pre-render en R requiere R en el servidor. Opción: GitHub Actions que haga el build y suba `docs/`, o plan con soporte para R.

## Resumen

- Caché configurado en `netlify.toml` para ahorrar ancho de banda.  
- Mantén el sitio liviano (videos e imágenes comprimidos).  
- Sigue construyendo en local y publicando `docs/` para no gastar build minutes.

# Sitio web OLES — Guía principal

Sitio del **Observatorio de Violencia y Legitimidad Social (OLES)** con [Quarto](https://quarto.org). La salida compilada va a la carpeta **`docs/`** (es lo que se publica en GitHub Pages, Netlify, etc.).

Para el detalle campo a campo (YAML, imágenes, ejemplos largos), está **[MANUAL.md](MANUAL.md)**. Este README resume **cómo aparecen las tarjetas/listados** y **cómo dar de alta** estudios, personas y noticias.

---

## 1. Cómo se construyen las tarjetas en cada parte del sitio

| Página | ¿Cómo salen las cards? | Qué tocar normalmente |
|--------|-------------------------|------------------------|
| **Inicio** (`index.qmd`) | **Destacados:** un bloque R recorre las carpetas `noticias/AAAA-MM-DD/` y arma cards solo de quienes tienen `destacado: true` en el YAML, ordenados por fecha.<br>**Noticias recientes:** otro bloque R toma las **3** noticias más recientes por `date`.<br>**Líneas de investigación (4 cuadrantes):** HTML **fijo** en `index.qmd` (enlaces, textos e imágenes bajo `images/lineas/`). | Para destacados/recientes: crear o editar noticias (véase §2). Para los 4 bloques de líneas en la portada: editar HTML en `index.qmd` y, si aplica, imágenes en `images/lineas/`. |
| **Noticias** (`noticias/index.qmd`) | **Listing** de Quarto: `contents: "*/index.qmd"`, rejilla, orden `date desc`. Cualquier carpeta `noticias/AAAA-MM-DD/index.qmd` entra sola. | No hace falta “registrar” la noticia en otro archivo; basta la carpeta + `index.qmd` con buen YAML e imagen. |
| **Equipo** (`equipo/index.qmd`) | Varios **listings** en el YAML (`direccion`, `comite`, `investigadores-principales`, etc.). Cada bloque tiene `contents:` con **lista explícita de archivos** `.qmd`. Las cards salen de `title`, `image` y `orden` de cada perfil. | **Al agregar alguien nuevo:** crear `equipo/apellido-nombre.qmd` (y foto), luego **añadir la ruta del `.qmd` al `contents` del bloque correcto** en `equipo/index.qmd`. Cada perfil solo debe aparecer en **un** listing. |
| **Proyectos / Estudios** (`estudios/index.qmd`) | Las tarjetas las genera un **bloque R**: la lista `cards` (con `slug`, `picsum`, `lineas`, y opcionalmente `titulo_tarjeta`) más el YAML de cada `estudios/{slug}.qmd` (`title`, `estado`, `etiqueta`). Imagen de tarjeta vía seed de picsum.<br>Filtros por línea usan `data-lineas` (`"1"`, `"2"`, `"3"`, `"4"`, varias separadas por coma, o `""` para “sin línea”). | **Nuevo proyecto:** (1) crear `estudios/mi-proyecto.qmd`; (2) añadir una entrada `list(...)` en el vector `cards` dentro de `estudios/index.qmd`. Opcional: `titulo_tarjeta` si el título largo del YAML no sirve para la card. |
| **Líneas de investigación** (`estudios/lineas.qmd` y `estudios/lineas/linea-*.qmd`) | La **portada de líneas** es HTML en `lineas.qmd` (tarjetas `linea-index-card`). Las páginas por línea son Markdown con secciones e integrantes/proyectos enlazados.<br>Índice `/estudios/lineas/` no usa el mismo motor que “Proyectos”. | Editar `estudios/lineas.qmd` para cambiar textos de índice de líneas; cada `linea-X.qmd` para contenido de esa línea. |
| **Publicaciones** (`publicaciones/index.qmd`) | Bloque R que lee **todos** los `.qmd` en `publicaciones/` salvo `index.qmd`, ordena por `date` en el YAML y pinta el grid con filtros por `tipo`. | Añadir archivo `publicaciones/AAAA-tema-slug.qmd` con metadatos coherentes (`tipo`, `date`, `author`, DOI, etc.); al compilar, la card aparece sola. |

**Resumen:** equipo y proyectos exigen **tocar el índice** (`equipo/index.qmd` / `estudios/index.qmd`). Noticias listado y publicaciones se alimentan sobre todo **añadiendo archivos** en sus carpetas; la portada de noticias se alimenta igual más el flag `destacado`.

---

## 2. Cómo subir o actualizar contenido: estudios, perfiles y noticias

### 2.1 Estudios (proyectos de investigación)

1. Crear **`estudios/<slug>.qmd`** con el front matter del proyecto (`title`, `estado` como `en-curso` / `finalizado`, etc.) y el cuerpo en Markdown. Puedes guiarte por un `estudios/fondecyt-*.qmd` existente.
2. Abrir **`estudios/index.qmd`**, localizar la lista R `cards <- list(` y añadir algo como:
   - `list(slug = "mi-slug", picsum = "olesproj-nombre", lineas = "1", titulo_tarjeta = "Nombre corto opcional")`
   - **`slug`** = nombre del archivo sin `.qmd`.
   - **`lineas`:** números de línea institucional (`"1"` … `"4"`). Varios: `"1,4"`. Vacío `""` si no aplica filtro por línea.
3. Opcional: enlazar el proyecto desde **`estudios/lineas/linea-X.qmd`** en “Proyectos asociados”.
4. Ejecutar **`quarto render`** (o al menos `quarto render estudios/index.qmd` y el `.qmd` nuevo).

### 2.2 Perfiles (equipo)

1. **Foto:** colocar archivo en **`equipo/image/`** (Convención: `apellido-nombre.jpg` o similar). `_quarto.yml` declara `equipo/image/*` como recurso para que llegue a `docs/`.
2. **Perfil:** nuevo **`equipo/apellido-nombre.qmd`** (o ruta bajo `equipo/asistentes-anteriores/` si corresponde). Incluir YAML mínimo (`title`, `cargo`, `categories`, `orden`, `image`, etc.) y el cuerpo del perfil. Para publicaciones en el perfil, usar el `include` del `_pub-*.md` que genera el script (ver MANUAL §3).
3. **Listado del equipo:** editar **`equipo/index.qmd`** y añadir el archivo al array `contents` del bloque adecuado (Dirección, Comité, Investigadores, etc.).
4. **`quarto render`** dispara **`compilar_publicaciones_perfiles.R`** (pre-render) y actualiza los fragmentos `_pub-*.md` según `publicaciones/*.qmd` y el campo `authors`.

### 2.3 Noticias

1. Crear carpeta **`noticias/AAAA-MM-DD/`** (fecha de la noticia).
2. Dentro, **`index.qmd`** con YAML: `title`, `description`, `date`, `categories`, `image`, etc. Para la **portada** en “Destacados”, añadir **`destacado: true`** (orden automático por fecha; las más recientes arriba).
3. Poner la imagen principal en **la misma carpeta** (nombre acordado al campo `image`).
4. Opcional: partir de **`_templates/noticia-template.qmd`**.
5. **`quarto render`:** el listado en `noticias/index.html` se actualiza solo; la portada incorpora destacados y las tres noticias más recientes sin editar `index.qmd` manualmente.

---

## 3. Compilar y publicar

```bash
# Sitio completo (recomendado; ejecuta R pre-render y Quarto)
quarto render
```

Requisitos: **R** y el paquete **`yaml`** (`install.packages("yaml")`) para el script de publicaciones/perfiles y varios chunks del sitio.

Tras compilar, hacer commit de los cambios en fuentes y de **`docs/`** según el flujo de tu hosting.

---

## 4. Referencias

- **[MANUAL.md](MANUAL.md)** — Manual extendido de contenidos.
- Diagrama de carpetas y tabla resumida (versión anterior más visual) se puede seguir leyendo el historial git de este README si lo necesitas; la fuente de verdad del comportamiento actual está en los `.qmd` citados arriba.

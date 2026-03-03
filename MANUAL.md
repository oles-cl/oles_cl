# Manual de contenidos – Sitio OLES

Guía paso a paso para mantener noticias, equipo, publicaciones y proyectos del sitio Quarto de OLES.

---

## 1. Noticias y destacadas

### 1.1 Crear una noticia nueva

**Paso 1 – Carpeta con fecha**

Crear una carpeta en `noticias/` con formato `YYYY-MM-DD`:

```
noticias/2026-03-01/
```

**Paso 2 – Archivo de la noticia**

Dentro de esa carpeta, crear `index.qmd`. Puedes basarte en `_templates/noticia-template.qmd`.

Campos YAML importantes:

| Campo          | Uso |
|----------------|-----|
| `title`        | Título que se ve en listados y en la página. |
| `description`  | Bajada/resumen (cards y “Noticias recientes”). |
| `date`         | Fecha de la noticia, formato `YYYY-MM-DD`. |
| `author`       | Autor del texto. |
| `categories`   | Ej.: `[Noticias]`. |
| `image`        | Nombre del archivo de imagen en la misma carpeta (ej. `featured.jpg`). |
| `destacado`    | `true` para que aparezca en la sección Destacados de la portada (orden por fecha, más reciente arriba). Opcional; por defecto no se muestra. |

Ejemplo mínimo:

```yaml
---
title: "Título de la noticia"
description: "Breve descripción para las cards."
date: "2026-03-01"
author: "Nombre"
categories: [Noticias]
image: "featured.jpg"
title-block-banner: false
---

::: {.featured-image}
![](featured.jpg)
:::

Contenido en Markdown...

[← Volver a Noticias](../index.html)
```

**Paso 3 – Imagen principal**

- Poner en la **misma carpeta** una imagen: `featured.jpg`, `featured.png` o `featured.jpeg`.
- Esa imagen se usa en la noticia, en el listado de noticias y (si aplica) en “Noticias recientes” de la portada.

**Paso 4 – Galería (opcional)**

Para varias imágenes en bloque:

```markdown
::: {.gallery}
![](foto1.jpg) ![](foto2.jpg) ![](foto3.jpg)
:::
```

Las noticias se listan solas en `/noticias/` por fecha (más recientes primero). No hace falta registrarlas en otro archivo.

---

### 1.2 Noticias destacadas (portada)

Las noticias que aparecen en la sección **Destacados** de la portada se generan **solas al compilar**: solo hace falta marcar en cada noticia si es destacada o no.

**Cómo:** En el YAML del `index.qmd` de la noticia, agrega:

```yaml
destacado: true
```

- Todas las noticias con `destacado: true` salen en la sección Destacados.
- Se ordenan por **fecha**: la más reciente **arriba**.
- Si no pones `destacado` o pones `destacado: false`, esa noticia no sale en Destacados (sí puede salir en el listado de noticias y en “Noticias recientes”).

No hace falta tocar `index.qmd` de la portada para cambiar qué noticias están destacadas; solo editar el YAML de cada noticia y volver a ejecutar `quarto render`.

---

### 1.3 Noticias recientes (portada)

La sección “Noticias recientes” de la portada se genera con **R** dentro de `index.qmd`: toma automáticamente las **3 noticias más recientes** por `date` de todas las carpetas `noticias/YYYY-MM-DD/`. No hay que configurar nada más; solo asegurarse de que cada noticia tenga `date` en el YAML.

---

## 2. Equipo: agregar y ordenar personas

### 2.1 Dónde va cada persona

- **Equipo actual:** archivos `.qmd` en `equipo/` (ej. `equipo/monica-gerber.qmd`).
- **Asistentes anteriores:** archivos en `equipo/asistentes-anteriores/` (ej. `equipo/asistentes-anteriores/bruno-rojas.qmd`).

El listado de la página “Equipo” se arma solo según esos archivos y su categoría.

### 2.2 Crear un perfil nuevo (equipo actual)

**Paso 1 – Archivo del perfil**

Crear en `equipo/` un archivo con nombre en minúsculas y guiones, por ejemplo: `nombre-apellido.qmd`.

**Paso 2 – Foto**

Subir la foto a `equipo/image/` con un nombre coherente al perfil, por ejemplo `nombre-apellido.jpg` o `.png`.

**Paso 3 – YAML del perfil**

Campos importantes:

| Campo          | Uso |
|----------------|-----|
| `title`        | Nombre completo (aparece en la card y en el perfil). |
| `cargo`        | Cargo o rol breve. |
| `categories`   | **Una** de: `Dirección`, `Subdirección`, `Investigadores`, `Coordinador`, `Asistentes`. Define en qué bloque aparece en `/equipo/`. |
| `orden`        | Número para ordenar dentro del mismo bloque (menor = primero). |
| `image`        | Ruta a la foto desde `equipo/`, ej. `image/nombre-apellido.jpg`. |
| `email`, `organizacion` | Opcionales. |
| `about`, `links`, `areas-interes`, `educacion` | Opcionales; ver perfiles existentes. |

Ejemplo mínimo:

```yaml
---
title: "Nombre Apellido"
cargo: "Rol o cargo"
categories: [Investigadores]
orden: 10
image: "image/nombre-apellido.jpg"
email: "email@institucion.cl"
organizacion: "Universidad X"
---
```

**Paso 4 – Texto del perfil**

Debajo del YAML, escribir en Markdown: descripción, áreas de interés, educación, etc. Al final, incluir el bloque de publicaciones y el enlace de vuelta:

```markdown
## Últimas publicaciones

&#123;&#123;&lt; include _pub-nombre-apellido.md &gt;&#125;&#125;

[← Volver al Equipo](index.html)
```

El archivo `_pub-nombre-apellido.md` **no se escribe a mano**: lo genera el script de publicaciones (ver sección 3).

### 2.3 Asistentes anteriores

Mismo esquema que el equipo actual, pero:

- El archivo va en `equipo/asistentes-anteriores/nombre-apellido.qmd`.
- La foto puede estar en `equipo/image/` y referenciarse igual: `image/nombre-apellido.jpg`.
- En “Últimas publicaciones” se usa `&#123;&#123;&lt; include _pub-nombre-apellido.md &gt;&#125;&#125;`; el script genera `_pub-*.md` en `equipo/asistentes-anteriores/` para quienes estén ahí.

### 2.4 Proyectos en el perfil

Los “Proyectos de investigación” que ves en cada perfil son **enlaces fijos** que cada quien escribe en su `.qmd`, por ejemplo:

```markdown
## Proyectos de investigación

- [Nombre del estudio](../estudios/slug-del-estudio.html) — Investigador responsable
```

No hay anclaje automático estudio ↔ persona; se mantiene a mano.

---

## 3. Publicaciones y vínculo con el equipo

### 3.1 Crear una publicación

**Paso 1 – Archivo**

Crear en `publicaciones/` un archivo `.qmd` con un slug estable, por ejemplo `2025-apellido-tema.qmd`. No usar `index.qmd` para una publicación concreta.

**Paso 2 – YAML**

Campos importantes:

| Campo        | Uso |
|-------------|-----|
| `title`     | Título del artículo o libro. |
| `description` | Resumen breve (listado de publicaciones). |
| `date`      | Fecha de publicación, formato `YYYY-MM-DD`. |
| `authors`   | **Lista de slugs** de perfiles de equipo/asistentes que son autores, en el orden que quieras. Ej.: `[monica-gerber, ana-figueiredo, joaquin-bahamondes]`. |
| `reference` | Referencia bibliográfica en texto (cita corta o enlace). |

Cada valor en `authors` debe coincidir con el **nombre del archivo** del perfil (sin `.qmd`):

- Si el perfil es `equipo/monica-gerber.qmd` → en `authors` pones `monica-gerber`.
- Si es `equipo/asistentes-anteriores/bruno-rojas.qmd` → en `authors` pones `bruno-rojas`.

Ejemplo:

```yaml
---
title: "Título del artículo"
description: "Resumen breve."
date: "2025-06-01"
authors: [monica-gerber, ana-figueiredo, loreto-quiroz]
reference: "Apellido et al. (2025). Revista X. [DOI](url)"
---
```

**Paso 3 – Cuerpo del .qmd**

En el cuerpo puedes poner resumen, enlaces, DOI y la lista “Autores OLES” con enlaces a los perfiles. Puedes copiar la estructura de `publicaciones/2025-gerber-police-postures.qmd`.

### 3.2 Anidar la publicación a las personas (listado en su perfil)

El listado “Últimas publicaciones” en cada perfil **no se edita a mano**. Lo generan los scripts así:

1. **Script:** `compilar_publicaciones_perfiles.R`  
   - Lee todos los `.qmd` de `publicaciones/` (salvo `index.qmd`).  
   - Para cada uno lee el YAML y el campo `authors`.  
   - Para cada autor (slug) escribe o actualiza un archivo `equipo/_pub-{slug}.md` o `equipo/asistentes-anteriores/_pub-{slug}.md` con la lista de sus publicaciones (enlaces y referencia).

2. **Cuándo se ejecuta:** Está configurado como `pre-render` en `_quarto.yml`, así que al hacer `quarto render` (o render del sitio completo) primero se ejecuta este script y luego se compila el sitio. Así, cada perfil incluye con `&#123;&#123;&lt; include _pub-nombre-apellido.md &gt;&#125;&#125;` su lista actualizada.

**Resumen:**

- Agregas o editas una publicación en `publicaciones/XXXX-slug.qmd` con `authors: [slug1, slug2, ...]`.
- Ejecutas `quarto render` (o al menos el pre-render que corre el R).
- Los perfiles de esos `slug` muestran automáticamente la publicación en “Últimas publicaciones”.

Si cambias `authors` o añades una publicación nueva, hace falta volver a ejecutar el render para que los `_pub-*.md` se regeneren.

---

## 4. Proyectos de investigación (estudios)

### 4.1 Cómo está armado

- Cada proyecto es una **página** con su propio `.qmd` en `estudios/` (ej. `estudios/esep.qmd`, `estudios/panel-legitimidad-policial.qmd`).
- El **listado** que se ve en “Proyectos de Investigación” **no** se genera automáticamente desde los `.qmd`: está escrito en **HTML** dentro de `estudios/index.qmd`. Ahí hay un bloque con tarjetas/enlaces a cada proyecto.

Por tanto, para que un proyecto aparezca en la página de estudios hay que:
1. Tener (o crear) su `.qmd` en `estudios/`.
2. Añadir o modificar la tarjeta correspondiente en `estudios/index.qmd`.

### 4.2 Crear un proyecto nuevo

**Paso 1 – Página del proyecto**

Crear en `estudios/` un archivo con nombre descriptivo, por ejemplo `mi-proyecto.qmd`:

```yaml
---
title: "Nombre del proyecto"
description: "Descripción breve para cards o metadatos."
categoria: "encuestas"
estado: "en-curso"
fecha-inicio: "2024"
fecha-fin: "Presente"
---

## Descripción

Texto del proyecto en Markdown...

[← Volver a Estudios](index.qmd)
```

**Paso 2 – Enlazarlo en el listado**

Abrir `estudios/index.qmd` y, dentro del bloque HTML del grid (donde están las otras tarjetas), añadir una tarjeta que apunte a tu página:

```html
<a href="mi-proyecto.html" class="estudio-card">
  <div class="estudio-card-body">
    <span class="estudio-estado en-curso">En curso</span>
    <h3 class="estudio-titulo">Nombre del proyecto</h3>
  </div>
</a>
```

- `href` debe ser el nombre del `.qmd` cambiado a `.html` (ej. `mi-proyecto.html`).
- Para “Finalizado” usa la clase `estudio-estado finalizado` en lugar de `en-curso`.

### 4.3 Modificar un proyecto existente

- **Solo contenido:** Editar el `.qmd` correspondiente en `estudios/` (título, descripción, estado, texto).
- **Cambiar título o estado en el listado:** Editar `estudios/index.qmd` y actualizar la tarjeta que tenga ese `href` (texto del `<h3>` y clase `en-curso` / `finalizado` si aplica).
- **Quitar un proyecto del listado:** Borrar o comentar la tarjeta en `estudios/index.qmd`. La página `.qmd` puede seguir existiendo si quieres mantener el enlace directo.

---

## Flujo rápido de trabajo

| Tarea | Dónde | Luego |
|-------|--------|--------|
| Nueva noticia | `noticias/YYYY-MM-DD/index.qmd` + imagen en esa carpeta | `quarto render` |
| Destacadas (portada) | En cada noticia: YAML `destacado: true` (se compilan solas, orden por fecha) | `quarto render` |
| Nueva persona en equipo | `equipo/nombre-apellido.qmd` + foto en `equipo/image/` | `quarto render` |
| Asistente anterior | `equipo/asistentes-anteriores/nombre-apellido.qmd` | `quarto render` |
| Nueva publicación | `publicaciones/YYYY-slug.qmd` con `authors: [slug1, ...]` | `quarto render` (corre R y regenera _pub-*.md) |
| Nuevo proyecto | `estudios/slug.qmd` + tarjeta en `estudios/index.qmd` | `quarto render` |
| Modificar proyecto | `estudios/slug.qmd` y/o tarjeta en `estudios/index.qmd` | `quarto render` |

Siempre que cambies publicaciones o equipo, conviene ejecutar **`quarto render`** desde la raíz para que el pre-render actualice los `_pub-*.md` y todo el sitio quede consistente.

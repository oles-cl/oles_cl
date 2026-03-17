# Tutorial de Edición del Sitio OLES

Esta guía está pensada para **editar y mantener la web**, no para navegarla como visitante. Explica cómo agregar personas, publicaciones, proyectos, noticias y cómo funciona la portada (`index.qmd`) y la configuración general del sitio.

---

## 1. Cómo está organizado el sitio

El sitio está hecho en **Quarto**. Los archivos fuente están en `.qmd` y el sitio compilado se genera en la carpeta `docs/`.

Archivos y carpetas clave:

- `_quarto.yml` → configuración general del sitio, navbar, salida a `docs/`.
- `index.qmd` → portada.
- `somos.qmd` → página “Acerca de OLES”.
- `contacto.qmd` → página de contacto.
- `styles.css` → estilos globales.
- `equipo/` → perfiles del equipo.
- `noticias/` → noticias, una carpeta por fecha.
- `estudios/` → proyectos y líneas de investigación.
- `publicaciones/` → publicaciones académicas.
- `repositorio/` → repositorio de datos, como EPSEP.
- `_templates/` → plantillas base para crear nuevo contenido.

Importante:

- El archivo `_quarto.yml` indica que el sitio se compila en `docs/`.
- Antes del render se ejecuta `compilar_publicaciones_perfiles.R`, que arma automáticamente los listados de publicaciones dentro de los perfiles del equipo.

---

## 2. Flujo básico para editar

Cada vez que hagas cambios, el flujo normal es:

1. Editar o crear el archivo `.qmd`.
2. Guardar imágenes o PDFs en la carpeta correcta.
3. Ejecutar `quarto render`.
4. Revisar el resultado generado en `docs/`.

Si el sitio se publica desde GitHub Pages o Netlify usando `docs/`, esa carpeta debe quedar actualizada.

---

## 3. Cómo agregar una persona al equipo

La plantilla base está en:

- `_templates/PERSONA.qmd`

### Dónde crear el archivo

Depende de la categoría:

- `equipo/` → Dirección, Subdirección, Investigadores, Coordinador, Asistentes.
- `equipo/asistentes-anteriores/` → asistentes anteriores.
- `equipo/tesistas/` → tesistas y pasantes.

### Nombre del archivo

Usa un slug simple, por ejemplo:

- `equipo/matias-deneken.qmd`
- `equipo/ana-figueiredo.qmd`

Ese nombre importa porque:

- define la URL final;
- se usa también para vincular publicaciones con la persona.

### Campos importantes del YAML

Ejemplo:

```yaml
---
title: "Nombre Apellido"
cargo: "Cargo o Posición"
categories: [Asistentes]
orden: 50
email: "correo@ejemplo.com"
organizacion: "Universidad o Institución"
image: "image/foto.jpg"
about:
  template: trestles
  image-shape: round
  image-width: 12em
  links:
    - icon: envelope
      text: Email
      href: mailto:correo@ejemplo.com
areas-interes:
  - "Área 1"
educacion:
  - titulo: "Grado"
    institucion: "Universidad"
---
```

### Qué hace cada campo

- `title` → nombre que aparecerá en la tarjeta y en el perfil.
- `cargo` → cargo visible en el perfil.
- `categories` → define en qué bloque aparece en `equipo/index.qmd`.
- `orden` → orden dentro de la categoría; números más bajos aparecen primero.
- `image` → foto del perfil.
- `areas-interes` y `educacion` → se usan en el contenido del perfil.

### Categorías válidas en `equipo/`

- `Dirección`
- `Subdirección`
- `Investigadores`
- `Coordinador`
- `Asistentes`

### Fotos

Lo normal en este proyecto es guardar imágenes del equipo en:

- `equipo/image/`

Y luego usar, por ejemplo:

- `image: "image/matias-deneken.jpg"`

### Cómo aparece en la página Equipo

La página `equipo/index.qmd` usa listings automáticos por categoría. Si el archivo está en la carpeta correcta y el YAML tiene la categoría correcta, la persona aparece sola tras `quarto render`.

### Publicaciones dentro del perfil

Muchos perfiles incluyen una línea como esta:

```md
\{\{< include _pub-matias-deneken.md >\}\}
```

Ese archivo `_pub-...md` no se edita a mano: lo genera `compilar_publicaciones_perfiles.R` a partir de `publicaciones/*.qmd`.

---

## 4. Cómo agregar una publicación

La plantilla base está en:

- `_templates/publicacion.qmd`

### Dónde crear el archivo

En:

- `publicaciones/`

Ejemplo:

- `publicaciones/2026-articulo-ejemplo.qmd`

### Estructura mínima

```yaml
---
title: "Título de la publicación"
description: "Una línea descriptiva."
date: "2026-01-20"
author: "Apellido, N., Apellido, N."
authors: [slug-perfil-1, slug-perfil-2]
reference: "Revista, volumen, DOI"
---
```

### Diferencia entre `author` y `authors`

- `author` → texto visible para la publicación.
- `authors` → lista de slugs de personas OLES para enlazar la publicación a sus perfiles.

Esto es clave. Si en `authors` pones:

```yaml
authors: [matias-deneken, monica-gerber]
```

el script `compilar_publicaciones_perfiles.R` agregará esa publicación a:

- `equipo/_pub-matias-deneken.md`
- `equipo/_pub-monica-gerber.md`

### Qué hace `reference`

`reference` se usa como referencia corta en los perfiles del equipo. Conviene completarla siempre.

### Cómo aparece en la web

- Aparece automáticamente en `publicaciones/index.qmd`, porque esa página lista todos los `.qmd` dentro de `publicaciones/`.
- También puede aparecer en los perfiles si `authors` está bien definido.

### Si hay DOI o enlace externo

Puedes agregar una sección como:

```md
## DOI

[10.xxxx/xxxxx](https://doi.org/...)
```

### Regla importante

Si el slug de una persona en `authors` no coincide exactamente con el nombre del archivo en `equipo/` o `equipo/asistentes-anteriores/`, la publicación no se asociará bien a su perfil.

---

## 5. Cómo agregar una noticia

La plantilla base está en:

- `_templates/noticia-template.qmd`

### Dónde crearla

Cada noticia va en su propia carpeta con fecha:

- `noticias/AAAA-MM-DD/`

Dentro de esa carpeta debe existir:

- `index.qmd`
- `featured.jpg` o `featured.png` si tiene imagen principal
- otras imágenes, si hay galería

Ejemplo:

- `noticias/2026-01-20/index.qmd`

### Estructura mínima

```yaml
---
title: "Título de la noticia"
description: "Breve descripción"
date: "2026-01-20"
author: "Nombre"
categories: [Noticia]
image: "featured.jpg"
destacado: false
title-block-banner: false
---
```

### Categorías recomendadas

Hoy el sitio usa categorías como:

- `Noticia`
- `Evento`
- `Entrevista`
- `Publicación`
- `Proyecto`
- `Reconocimiento`

Se recomienda usar **1 o máximo 2**.

### Campo `destacado`

Si pones:

```yaml
destacado: true
```

la noticia puede aparecer en la sección **Destacados** de la portada, porque `index.qmd` busca las noticias con ese campo activado.

### Cómo aparece en la web

- Aparece automáticamente en `noticias/index.qmd`.
- Puede aparecer en la portada si es reciente y/o si está marcada como destacada.

### Imágenes

La imagen principal suele ir así:

```md
::: {.featured-image}
![](featured.jpg)
:::
```

Si hay más imágenes:

```md
::: {.gallery}
![](foto1.jpg) ![](foto2.jpg)
:::
```

---

## 6. Cómo agregar un proyecto o estudio

La plantilla base está en:

- `_templates/proyecto.qmd`

### Dónde crearlo

En:

- `estudios/`

Ejemplo:

- `estudios/nuevo-estudio.qmd`

### Estructura base

```yaml
---
title: "Título del proyecto"
estado: "en-curso"
investigador_responsable: "Nombre"
format:
  html:
    body-classes: estudio-page
---
```

Después viene el cuerpo con dos columnas:

- columna izquierda → equipo del proyecto;
- columna derecha → introducción, objetivos, métodos, etc.

### Qué campos conviene completar

- `title` → nombre visible del proyecto.
- `estado` → normalmente `en-curso` o `finalizado`.
- `investigador_responsable` → sirve como metadato del estudio.

### Importante: crear el archivo no basta

Aunque el proyecto exista en `estudios/nuevo-estudio.qmd`, para que se vea en la página de proyectos hay que agregar manualmente su tarjeta en:

- `estudios/index.qmd`

Eso es porque `estudios/index.qmd` no usa listing automático; está armado a mano con tarjetas HTML.

### Qué editar en `estudios/index.qmd`

Debes agregar un bloque como este dentro del grid:

```html
<a href="nuevo-estudio.html" class="estudio-card">
  <div class="estudio-card-body">
    <span class="estudio-estado en-curso">En curso</span>
    <h3 class="estudio-titulo">Nuevo estudio</h3>
  </div>
</a>
```

Si no agregas la tarjeta ahí, el estudio existirá, pero no aparecerá en el listado principal.

---

## 7. Cómo editar la portada (`index.qmd`)

`index.qmd` es una de las páginas más importantes del sitio. Mezcla HTML y R.

### Qué controla

- video principal;
- sección de destacados;
- noticias recientes;
- líneas de investigación;
- bloque “Acerca del Observatorio”;
- logos de instituciones asociadas;
- footer.

### Cómo funciona la sección Destacados

Hay un bloque en R que:

- revisa las carpetas dentro de `noticias/`;
- lee el YAML de cada `index.qmd`;
- busca las noticias con `destacado: true`;
- construye automáticamente las tarjetas destacadas.

Eso significa que para destacar una noticia no hay que editar la portada: basta con poner `destacado: true` en esa noticia.

### Cómo funciona Noticias recientes

También se arma automáticamente leyendo las noticias desde `noticias/`.

### Qué sí se edita manualmente en `index.qmd`

- el video del hero;
- los textos fijos de la portada;
- los botones;
- los bloques de líneas de investigación;
- logos y enlaces institucionales;
- footer.

### Cuándo editar `index.qmd`

Edita `index.qmd` cuando quieras cambiar:

- el diseño o estructura de la portada;
- los textos visibles de la home;
- los botones principales;
- la lista de instituciones asociadas;
- la forma en que se muestran destacados o noticias.

No hace falta editarlo para sumar una noticia común.

---

## 8. Cómo editar la navegación principal

La navbar no se cambia en `index.qmd`, sino en:

- `_quarto.yml`

Ahí se define:

- `Inicio`
- `Acerca de OLES`
- `Noticias`
- menú `Investigación`
- menú `Repositorio de datos`
- `Equipo`
- `Contacto`

Si quieres cambiar el nombre de una sección, moverla o agregar una nueva, debes editar `_quarto.yml`.

Ejemplo:

```yaml
website:
  navbar:
    left:
      - text: "Inicio"
        href: index.qmd
```

---

## 9. Cómo funciona la página Equipo

La página:

- `equipo/index.qmd`

usa **listings automáticos por categoría**.

Eso significa:

- no tienes que agregar manualmente una tarjeta por persona;
- basta con que el archivo exista y su `categories` coincida con una categoría listada.

Actualmente las secciones del index de equipo se arman con:

- `Dirección`
- `Subdirección`
- `Investigadores`
- `Coordinador`
- `Asistentes`

Si inventas una categoría nueva, no aparecerá a menos que también edites `equipo/index.qmd`.

---

## 10. Cómo funcionan Noticias y Publicaciones index

### `noticias/index.qmd`

Usa un `listing` automático de:

- `*/index.qmd`

dentro de la carpeta `noticias/`.

Por eso, para que una noticia aparezca:

- debe estar en una subcarpeta;
- el archivo debe llamarse `index.qmd`.

### `publicaciones/index.qmd`

Usa un `listing` automático de:

- `*.qmd`

dentro de `publicaciones/`.

Por eso, cualquier publicación nueva que agregues allí aparecerá sola tras renderizar.

---

## 11. Cómo subir archivos e imágenes

### Personas

- fotos del equipo: normalmente en `equipo/image/`

### Noticias

- imágenes dentro de la carpeta de la noticia:
  - `noticias/2026-01-20/featured.jpg`
  - `noticias/2026-01-20/foto1.jpg`

### Repositorio

- PDFs e informes dentro de la carpeta correspondiente, por ejemplo:
  - `repositorio/2025_epsep_informe_w01-w04.pdf`

### Recomendación práctica

Usa nombres simples, sin espacios, por ejemplo:

- `featured.jpg`
- `foto1.jpg`
- `luciano-saez.jpg`
- `2026-informe-epsep.pdf`

---

## 12. Cómo actualizar EPSEP o el repositorio

La página actual está en:

- `repositorio/epsep.qmd`

Si quieres subir una nueva versión del informe:

1. Guarda el PDF nuevo en `repositorio/`.
2. Actualiza el nombre del archivo enlazado en `repositorio/epsep.qmd`.
3. Si cambia el enlace al informe online, actualiza también esa URL.

Si en el futuro hay más repositorios, tendrás que:

1. crear nuevas páginas en `repositorio/`;
2. agregarlas en el menú correspondiente de `_quarto.yml`.

---

## 13. Cómo editar “Acerca de OLES” y “Contacto”

### `somos.qmd`

Edita aquí:

- descripción institucional;
- objetivo;
- apoyos y fondos;
- texto sobre el equipo;
- logos de financiamiento o instituciones.

### `contacto.qmd`

Edita aquí:

- correo de contacto;
- enlaces a LinkedIn, Instagram y X;
- cualquier texto de presentación.

---

## 14. Sobre estilos y botones

Los estilos globales están en:

- `styles.css`

Ahí se controlan:

- colores;
- tipografías;
- cards;
- botones;
- botones “Volver”;
- layouts de estudios, noticias y otras páginas.

Si quieres que un cambio visual afecte muchas páginas a la vez, casi siempre el lugar correcto es `styles.css`.

---

## 15. Errores comunes

### La persona no aparece en Equipo

Revisa:

- que el archivo esté en la carpeta correcta;
- que `categories` tenga una categoría existente;
- que hiciste `quarto render`.

### La publicación no aparece en el perfil

Revisa:

- que `authors` tenga slugs correctos;
- que la publicación esté dentro de `publicaciones/`;
- que el script pre-render haya corrido al hacer `quarto render`.

### La noticia no aparece en Noticias

Revisa:

- que esté en una carpeta tipo `noticias/AAAA-MM-DD/`;
- que el archivo se llame `index.qmd`;
- que tenga YAML válido;
- que hayas renderizado.

### El proyecto existe, pero no se ve en la lista de estudios

Revisa:

- que hayas agregado también su tarjeta en `estudios/index.qmd`.

---

## 16. Resumen rápido: qué archivo tocar según lo que quieras hacer

| Quiero hacer esto | Archivo o carpeta principal |
|---|---|
| Agregar una persona | `equipo/` o subcarpetas, usando `_templates/PERSONA.qmd` |
| Agregar una publicación | `publicaciones/`, usando `_templates/publicacion.qmd` |
| Agregar una noticia | `noticias/AAAA-MM-DD/index.qmd`, usando `_templates/noticia-template.qmd` |
| Agregar un proyecto | `estudios/nuevo-proyecto.qmd` y además `estudios/index.qmd` |
| Cambiar portada | `index.qmd` |
| Cambiar menú superior | `_quarto.yml` |
| Cambiar estilos globales | `styles.css` |
| Cambiar página “Acerca de OLES” | `somos.qmd` |
| Cambiar contacto | `contacto.qmd` |
| Cambiar EPSEP | `repositorio/epsep.qmd` |

---

## 17. Recomendación final de trabajo

Cuando quieras subir contenido nuevo, conviene seguir siempre esta lógica:

1. copiar una plantilla desde `_templates/`;
2. nombrar bien el archivo;
3. revisar el YAML con cuidado;
4. guardar imágenes en la carpeta correcta;
5. renderizar;
6. revisar visualmente la página generada en `docs/`.

Si el cambio es en proyectos o portada, revisa además que los botones y enlaces sigan funcionando.

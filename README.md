# Página Web OLES

Sitio del **Observatorio de Violencia y Legitimidad Social (OLES)**, construido con [Quarto](https://quarto.org). El contenido se compila en la carpeta `docs/`.

---

## Diagrama del sitio y flujos de contenido

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                              oles-page (raíz)                                    │
├─────────────────────────────────────────────────────────────────────────────────┤
│  index.qmd          Portada: video, DESTACADOS (2 noticias fijas),              │
│                     Noticias recientes (3 más recientes por fecha), estudios     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  noticias/                                                                       │
│  ├── index.qmd      Listado automático (listing) de todas las noticias          │
│  └── YYYY-MM-DD/    Una noticia = una carpeta con fecha                          │
│        ├── index.qmd      (title, description, date, image)                      │
│        └── featured.jpg   Imagen principal                                       │
│                                                                                  │
│  → Destacadas: noticias con destacado: true en el YAML; se compilan solas (fecha) │
├─────────────────────────────────────────────────────────────────────────────────┤
│  equipo/                                                                         │
│  ├── index.qmd      Listado por categorías (Dirección, Subdirección,             │
│  │                  Investigadores, Coordinador, Asistentes)                     │
│  ├── image/         Fotos de cada persona (nombre-apellido.jpg)                 │
│  ├── nombre.qmd     Perfil: categories, orden, image, texto + {{< include        │
│  │                  _pub-nombre.md >}} (Últimas publicaciones)                  │
│  └── asistentes-anteriores/   Misma lógica, otros .qmd                          │
│                                                                                  │
│  → _pub-*.md los genera compilar_publicaciones_perfiles.R (no editar a mano)     │
├─────────────────────────────────────────────────────────────────────────────────┤
│  publicaciones/                                                                  │
│  ├── index.qmd      Listado automático (listing) por fecha                       │
│  └── YYYY-slug.qmd  Una publicación: title, date, authors: [slug1, slug2, ...]  │
│                                                                                  │
│  → authors = slugs de equipo/*.qmd → el script R escribe equipo/_pub-*.md        │
│    y así cada perfil muestra sus publicaciones                                   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  estudios/                                                                       │
│  ├── index.qmd      Listado MANUAL (HTML con tarjetas y enlaces a *.html)        │
│  └── slug.qmd       Página de cada proyecto (title, description, estado)        │
│                                                                                  │
│  → Añadir/editar proyecto = crear/editar .qmd + añadir/editar tarjeta en index   │
├─────────────────────────────────────────────────────────────────────────────────┤
│  _quarto.yml       Configuración sitio, navbar, pre-render: R script            │
│  compilar_publicaciones_perfiles.R   Lee publicaciones, escribe _pub-*.md       │
└─────────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                              quarto render
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│  docs/              Sitio compilado (publicar este directorio)                   │
└─────────────────────────────────────────────────────────────────────────────────┘
```

**Resumen de flujos:**

| Contenido        | Dónde se crea/edita                    | Qué se actualiza solo / qué a mano      |
|------------------|----------------------------------------|-----------------------------------------|
| Noticias         | `noticias/YYYY-MM-DD/index.qmd`        | Listado automático por fecha            |
| Destacadas       | YAML de cada noticia: `destacado: true` | Se compilan solas (orden por fecha)    |
| Equipo           | `equipo/*.qmd` + `equipo/image/`      | Cards por categoría automático          |
| Publicaciones    | `publicaciones/*.qmd` con `authors`   | Listado automático; _pub-*.md por script|
| Proyectos        | `estudios/*.qmd` + tarjetas en `estudios/index.qmd` | Listado a mano en index         |

---

## Manual paso a paso

Para instrucciones detalladas de cada tipo de contenido, usa el **[MANUAL.md](MANUAL.md)**:

1. **Noticias y destacadas** – Crear noticia, imagen featured, elegir las 2 destacadas en portada, noticias recientes.
2. **Equipo** – Agregar personas, categorías, fotos, orden, asistentes anteriores.
3. **Publicaciones** – Crear publicación y anidarla a autores (campo `authors` + script R).
4. **Proyectos** – Crear o modificar estudios y su listado en la página de investigación.

---

## Estructura de carpetas (referencia)

```
oles-page/
├── _quarto.yml              # Configuración del sitio y pre-render
├── _templates/              # Plantillas (ej. noticia-template.qmd)
├── compilar_publicaciones_perfiles.R   # Genera _pub-*.md para perfiles
├── index.qmd                # Portada
├── somos.qmd                 # Acerca de OLES
├── contacto.qmd
├── styles.css
├── translations.js           # ES/EN
├── noticias/                 # Noticias por carpeta YYYY-MM-DD
├── equipo/                   # Perfiles + image/ + asistentes-anteriores/
├── publicaciones/           # Publicaciones académicas (.qmd con authors)
├── estudios/                 # Proyectos de investigación (.qmd + listado en index)
├── eventos/
├── MANUAL.md                 # Manual de contenidos (este flujo)
├── README.md                 # Este archivo
└── docs/                     # Salida del sitio (quarto render)
```

---

## Compilar el sitio

```bash
# Todo el sitio (ejecuta antes el script R y luego Quarto)
quarto render

# Solo la portada
quarto render index.qmd

# Solo una sección
quarto render noticias/index.qmd
quarto render equipo/index.qmd
```

Requisito: tener R y el paquete `yaml` para el pre-render (`install.packages("yaml")`).

---

## Publicar

El sitio se sirve desde la carpeta `docs/` (p. ej. Netlify, GitHub Pages con branch `main` y carpeta `docs`). Tras `quarto render`, hacer commit y push de `docs/` (y de los cambios en fuentes).

---

## Notas

- **Destacadas:** Aparecen las noticias que tengan `destacado: true` en el YAML; se ordenan por fecha (más reciente arriba).
- **Publicaciones en perfiles:** Siempre que cambies `publicaciones/*.qmd` o el campo `authors`, ejecuta `quarto render` para regenerar los `_pub-*.md`.
- **Proyectos:** Para que un estudio aparezca en la página “Proyectos de Investigación”, hay que añadir su tarjeta en `estudios/index.qmd` además de crear el `.qmd`.

Para más detalle, ver **[MANUAL.md](MANUAL.md)**.

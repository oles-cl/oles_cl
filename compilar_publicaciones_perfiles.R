# compilar_publicaciones_perfiles.R
# Lee publicaciones/*.qmd (campo authors: y reference:) y escribe
# equipo/_pub-{autor}.md y equipo/asistentes-anteriores/_pub-{autor}.md
# para incluir en cada perfil. Ejecutar antes de quarto render (también como pre-render del proyecto).

root <- "."
pub_dir <- file.path(root, "publicaciones")
equipo_dir <- file.path(root, "equipo")
asistentes_dir <- file.path(equipo_dir, "asistentes-anteriores")

# Slugs cuyo `equipo/_pub-{slug}.md` no debe regenerarse (vacío = todos automáticos).
perfiles_pub_manual <- character(0)

if (!requireNamespace("yaml", quietly = TRUE)) {
  stop("Instala el paquete yaml: install.packages('yaml')")
}

perfil_incluye_bloque_pub <- function(out_dir, slug) {
  qmd <- file.path(out_dir, paste0(slug, ".qmd"))
  if (!file.exists(qmd)) return(FALSE)
  txt <- paste(readLines(qmd, warn = FALSE, encoding = "UTF-8"), collapse = "\n")
  grepl(paste0("_pub-", slug, ".md"), txt, fixed = TRUE)
}

# Archivos de publicación (excluir index.qmd)
pub_files <- list.files(pub_dir, pattern = "\\.qmd$", full.names = TRUE)
pub_files <- pub_files[basename(pub_files) != "index.qmd"]

pubs_by_author <- list()

for (f in pub_files) {
  content <- readLines(f, encoding = "UTF-8")
  delim <- which(content == "---")
  if (length(delim) < 2) next
  y <- yaml::yaml.load(paste(content[(delim[1]+1):(delim[2]-1)], collapse = "\n"))
  if (is.null(y$authors)) next
  slug <- tools::file_path_sans_ext(basename(f))
  href_equipo <- paste0("../publicaciones/", slug, ".html")
  href_asistentes <- paste0("../../publicaciones/", slug, ".html")
  ref <- if (is.null(y$reference)) "" else y$reference
  title <- if (is.null(y$title)) slug else y$title
  dfecha <- if (is.null(y$date) || !nzchar(as.character(y$date)[1])) "1900-01-01" else as.character(y$date)[1]
  dsort <- suppressWarnings(as.numeric(as.Date(dfecha)))
  for (a in y$authors) {
    if (is.null(pubs_by_author[[a]])) pubs_by_author[[a]] <- list()
    pubs_by_author[[a]] <- c(pubs_by_author[[a]], list(list(
      title = title, href_equipo = href_equipo, href_asistentes = href_asistentes,
      reference = ref, date_sort = dsort
    )))
  }
}

# Ordenar por fecha (más reciente primero) en cada perfil
for (nm in names(pubs_by_author)) {
  lst <- pubs_by_author[[nm]]
  ord <- order(vapply(lst, function(z) if (is.null(z$date_sort)) 0 else z$date_sort, numeric(1)), decreasing = TRUE)
  pubs_by_author[[nm]] <- lst[ord]
}

# Quién está en equipo/ vs asistentes-anteriores/
equipo_slugs <- setdiff(
  tools::file_path_sans_ext(list.files(equipo_dir, pattern = "\\.qmd$")),
  "index"
)
asistentes_slugs <- if (!dir.exists(asistentes_dir)) character(0) else
  setdiff(tools::file_path_sans_ext(list.files(asistentes_dir, pattern = "\\.qmd$")), "index")

# Escribir _pub-{slug}.md (con publicaciones o placeholder si no hay)
placeholder <- "- (Aún no hay publicaciones listadas.)"
max_pubs_por_perfil <- 3  # Máximo de publicaciones a mostrar por perfil

for (slug in names(pubs_by_author)) {
  if (slug %in% perfiles_pub_manual) next
  out_dir <- if (slug %in% asistentes_slugs) asistentes_dir else equipo_dir
  if (!perfil_incluye_bloque_pub(out_dir, slug)) next
  pubs <- pubs_by_author[[slug]]
  # Limitar a las primeras max_pubs_por_perfil publicaciones (ya ordenadas por fecha)
  pubs <- head(pubs, max_pubs_por_perfil)
  lines <- character(length(pubs))
  for (i in seq_along(pubs)) {
    p <- pubs[[i]]
    href <- if (slug %in% asistentes_slugs) p$href_asistentes else p$href_equipo
    lines[i] <- sprintf("- [%s](%s) — %s", p$title, href, p$reference)
  }
  out_file <- file.path(out_dir, paste0("_pub-", slug, ".md"))
  writeLines(lines, out_file, useBytes = TRUE)
  message("Escrito: ", out_file)
}

# Quienes están en equipo o asistentes pero no tienen publicaciones: archivo con placeholder
todos_slugs <- c(equipo_slugs, asistentes_slugs)
for (slug in todos_slugs) {
  if (slug %in% perfiles_pub_manual) next
  if (slug %in% names(pubs_by_author)) next
  out_dir <- if (slug %in% asistentes_slugs) asistentes_dir else equipo_dir
  if (!perfil_incluye_bloque_pub(out_dir, slug)) next
  out_file <- file.path(out_dir, paste0("_pub-", slug, ".md"))
  writeLines(placeholder, out_file, useBytes = TRUE)
  message("Escrito (placeholder): ", out_file)
}

message("Listo. Ejecuta 'quarto render' para compilar el sitio.")

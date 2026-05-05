#!/usr/bin/env python3
"""Genera archivos publicaciones/*.qmd (one-shot); edita la lista si hace falta."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUB = ROOT / "publicaciones"

TEMPLATE = '''---
title: "{title}"
description: "{desc}"
venue: "{venue}"
tipo: {tipo}
{doi_line}date: "{date}"
author: "{author}"
authors: [{authors_csv}]
reference: "{reference}"
format:
  html:
    title-block-style: none
    body-classes: publicacion-page
---

# {title}

{para}

**Autores OLES:** {oles_links}

**Fecha:** {fecha_label}.

## Referencia sugerida

{reference_md}

[← Volver a Publicaciones](index.qmd)
'''


def q(s: str) -> str:
    return s.replace('"', '\\"')


def write_entry(
    slug: str,
    title: str,
    desc: str,
    venue: str,
    tipo: str,
    date: str,
    author: str,
    authors: list[str],
    reference: str,
    reference_md: str,
    doi: str | None = None,
):
    doi_line = f'doi: "{doi}"\n' if doi else ""
    authors_csv = ", ".join(authors)
    oles_links = ", ".join(
        f"[{a.replace('-', ' ').title()}](../equipo/{a}.html)" for a in authors
    )
    # enlaces más legibles para slugs conocidos
    nicer = {
        "loreto-quiroz": "Loreto Quiroz",
        "luciano-saez-fuentealba": "Luciano Sáez-Fuentealba",
        "manuela-badilla": "Manuela Badilla Rajevic",
        "ana-figueiredo": "Ana Figueiredo",
        "cristobal-moya": "Cristóbal Moya",
        "monica-gerber": "Mónica Gerber",
        "macarena-orchard": "Macarena Orchard",
        "bruno-rojas": "Bruno Rojas",
        "joaquin-bahamondes": "Joaquín Bahamondes",
        "nicolas-tobar-jorquera": "Nicolás Tobar Jorquera",
        "matias-deneken": "Matías Deneken",
        "ismael-puga": "Ismael Puga",
    }
    parts = []
    for a in authors:
        label = nicer.get(a, a.replace("-", " ").title())
        if a == "nicolas-tobar-jorquera":
            href = f"../equipo/asistentes-anteriores/{a}.html"
        elif a == "bruno-rojas":
            href = f"../equipo/asistentes-anteriores/{a}.html"
        else:
            href = f"../equipo/{a}.html"
        parts.append(f"[{label}]({href})")
    oles_links = ", ".join(parts)
    fecha_label = date[:4] if len(date) >= 4 else date
    para = desc
    body = TEMPLATE.format(
        title=q(title),
        desc=q(desc),
        venue=q(venue),
        tipo=tipo,
        doi_line=doi_line,
        date=date,
        author=q(author),
        authors_csv=authors_csv,
        reference=q(reference),
        reference_md=reference_md,
        oles_links=oles_links,
        fecha_label=fecha_label,
        para=para,
    )
    (PUB / f"{slug}.qmd").write_text(body, encoding="utf-8")
    print("Wrote", slug)


# --- Loreto Quiroz ---
write_entry(
    "2024-delito-sociedad-linchamientos-quiroz",
    "Linchamientos, conciencia jurídica y enajenación legal en Chile: análisis de prensa",
    "Análisis de prensa sobre linchamientos y conciencia jurídica.",
    "Revista Delito y Sociedad, N° 57",
    "articulo",
    "2024-06-01",
    "Cornejo, D., & Quiroz, L.",
    ["loreto-quiroz"],
    "Cornejo, D., & Quiroz, L. (2024). Linchamientos, conciencia jurídica y enajenación legal en Chile: análisis de prensa. *Revista Delito y Sociedad*, N° 57.",
    "Cornejo, D., & Quiroz, L. (2024). Linchamientos, conciencia jurídica y enajenación legal en Chile: análisis de prensa. *Revista Delito y Sociedad*, N° 57.",
)
write_entry(
    "2024-novum-jus-vif-quiroz",
    "Conciencia jurídica y autoridad judicial en procedimientos por VIF en Chile",
    "Riesgo y desigualdades de género en procedimientos por violencia intrafamiliar.",
    "Novum Jus, 18(2)",
    "articulo",
    "2024-09-01",
    "Quiroz, L., & Riquelme, I.",
    ["loreto-quiroz"],
    "Quiroz, L., & Riquelme, I. (2024). Conciencia jurídica y autoridad judicial: riesgo y desigualdades de género en procedimientos por violencia intrafamiliar (VIF) en Chile. *Novum Jus*, 18(2).",
    "Quiroz, L., & Riquelme, I. (2024). Conciencia jurídica y autoridad judicial: riesgo y desigualdades de género en procedimientos por violencia intrafamiliar (VIF) en Chile. *Novum Jus*, 18(2).",
)
write_entry(
    "2023-contemporanea-vigilantism-quiroz",
    "From hard vigilantism to soft vigilantism in Latin America",
    "Vigilantismo en América Latina.",
    "Contemporánea, 13(3)",
    "articulo",
    "2023-12-01",
    "Fuentes, A., González, J., & Quiroz, L.",
    ["loreto-quiroz"],
    "Fuentes, A., González, J., & Quiroz, L. (2023). From hard vigilantism to soft vigilantism in Latin America. *Contemporánea*, 13(3).",
    "Fuentes, A., González, J., & Quiroz, L. (2023). From hard vigilantism to soft vigilantism in Latin America. *Contemporánea*, 13(3).",
)
write_entry(
    "2023-derecho-pucp-protesta-violenta-quiroz",
    "El derecho y la representación de la protesta política violenta en el estallido chileno",
    "Análisis de un expediente judicial del estallido chileno.",
    "Derecho PUCP, (90), 41–77",
    "articulo",
    "2023-05-01",
    "Quiroz, L.",
    ["loreto-quiroz"],
    "Quiroz, L. (2023). El derecho y la representación de la protesta política violenta: análisis de un expediente judicial del estallido chileno. *Derecho PUCP*, (90), 41–77. [DOI](https://doi.org/10.18800/derechopucp.202301.002)",
    "Quiroz, L. (2023). El derecho y la representación de la protesta política violenta: análisis de un expediente judicial del estallido chileno. *Derecho PUCP*, (90), 41–77. [DOI](https://doi.org/10.18800/derechopucp.202301.002)",
    doi="10.18800/derechopucp.202301.002",
)
write_entry(
    "2022-onati-linchamientos-quiroz",
    "Linchamientos en Chile y Argentina: jueces, fiscales y defensores",
    "Aproximación sociojurídica comparada.",
    "Oñati Socio-Legal Series, 12(2), 383–413",
    "articulo",
    "2022-08-01",
    "Quiroz, L.",
    ["loreto-quiroz"],
    "Quiroz, L. (2022). Linchamientos en Chile y Argentina: una aproximación desde el quehacer de jueces, fiscales y defensores. *Oñati Socio-Legal Series*, 12(2), 383–413.",
    "Quiroz, L. (2022). Linchamientos en Chile y Argentina: una aproximación desde el quehacer de jueces, fiscales y defensores. *Oñati Socio-Legal Series*, 12(2), 383–413.",
)
write_entry(
    "2019-direito-cidade-linchamientos-quiroz",
    "Linchamientos y derecho en Chile: ineficacia y poder simbólico",
    "Sociología jurídica y vigilantismo.",
    "Revista de Direito da Cidade, 11(2)",
    "articulo",
    "2019-07-01",
    "Quiroz, L.",
    ["loreto-quiroz"],
    "Quiroz, L. (2019). Linchamientos y derecho en Chile: entre la ineficacia y el poder simbólico. *Revista de Direito da Cidade*, 11(2).",
    "Quiroz, L. (2019). Linchamientos y derecho en Chile: entre la ineficacia y el poder simbólico. *Revista de Direito da Cidade*, 11(2).",
)
write_entry(
    "2017-moebio-teorias-linchamientos-quiroz",
    "Teorías de integración y linchamiento: capacidades explicativas",
    "Análisis de linchamiento desde teorías de integración, dominación e interdependencia.",
    "Cinta de Moebio, 58",
    "articulo",
    "2017-04-01",
    "Quiroz, L.",
    ["loreto-quiroz"],
    "Quiroz, L. (2017). Capacidades explicativas de las teorías de integración, dominación e interdependencia en el análisis de los linchamientos. *Cinta de Moebio*, 58.",
    "Quiroz, L. (2017). Capacidades explicativas de las teorías de integración, dominación e interdependencia en el análisis de los linchamientos. *Cinta de Moebio*, 58.",
)

# --- Manuela Badilla ---
write_entry(
    "2026-social-movement-studies-cross-temporal-monuments-badilla",
    "Cross-temporal protests: the indexical role of monument contestation in times of unrest",
    "Movimientos sociales y disputas monumentales.",
    "Social Movement Studies (early view)",
    "articulo",
    "2026-01-15",
    "Badilla Rajevic, M., & Wagner-Pacifici, R.",
    ["manuela-badilla"],
    "Badilla Rajevic, M., & Wagner-Pacifici, R. (2026). Cross-temporal protests: the indexical role of monument contestation in times of unrest. *Social Movement Studies*, 1–21. [DOI](https://doi.org/10.1080/14742837.2026.2616454)",
    "Badilla Rajevic, M., & Wagner-Pacifici, R. (2026). Cross-temporal protests: the indexical role of monument contestation in times of unrest. *Social Movement Studies*, 1–21. DOI 10.1080/14742837.2026.2616454.",
    doi="10.1080/14742837.2026.2616454",
)
write_entry(
    "2025-memory-studies-memorialicidio-badilla",
    "Memorialicidio: human rights heritage under threat",
    "Patrimonio y memorias represivas.",
    "Memory Studies",
    "articulo",
    "2025-03-01",
    "Badilla Rajevic, M., Infante-Batiste, V., & Abarca Paillicán, G. E.",
    ["manuela-badilla"],
    "Badilla Rajevic, M., Infante-Batiste, V., & Abarca Paillicán, G. E. (2025). Memorialicidio: human rights heritage under threat. *Memory Studies*. [DOI](https://doi.org/10.1177/17506980251388300)",
    "Badilla Rajevic, M., Infante-Batiste, V., & Abarca Paillicán, G. E. (2025). Memorialicidio: human rights heritage under threat. *Memory Studies*. DOI 10.1177/17506980251388300.",
    doi="10.1177/17506980251388300",
)
write_entry(
    "2025-ijhc-conservative-memory-badilla",
    "Between iconophilia and iconoclasm: advances of conservative memory in Chile",
    "Memoria política patrimonio herencia.",
    "International Journal of Heritage Studies",
    "articulo",
    "2025-02-01",
    "Badilla Rajevic, M., & Infante-Batiste, V.",
    ["manuela-badilla"],
    "Badilla Rajevic, M., & Infante-Batiste, V. (2025). Between iconophilia and iconoclasm: advances of conservative memory in Chile. *International Journal of Heritage Studies*. [DOI](https://doi.org/10.1080/13527258.2025.2484678)",
    "Badilla Rajevic, M., & Infante-Batiste, V. (2025). Between iconophilia and iconoclasm: advances of conservative memory in Chile. *International Journal of Heritage Studies*. DOI 10.1080/13527258.2025.2484678.",
    doi="10.1080/13527258.2025.2484678",
)
write_entry(
    "2025-contratexto-imagenes-feminicidio-badilla-figueiredo",
    "Deslegitimación del feminicidio a través de imágenes en Chile",
    "Análisis visual y violencias de género.",
    "Revista Contratexto, 44",
    "articulo",
    "2025-06-01",
    "Badilla Rajevic, M., Figueiredo, A., Cisternas Alarcón, P., & Rivera López, D.",
    ["manuela-badilla", "ana-figueiredo"],
    "Badilla Rajevic, M., Figueiredo, A., Cisternas Alarcón, P., & Rivera López, D. (2025). Deslegitimación del feminicidio a través de imágenes en Chile. *Revista Contratexto*, 44. [DOI](https://doi.org/10.26439/contratexto2025.n44.7889)",
    "Badilla Rajevic, M., Figueiredo, A., Cisternas Alarcón, P., & Rivera López, D. (2025). Deslegitimación del feminicidio a través de imágenes en Chile. *Revista Contratexto*, 44. DOI 10.26439/contratexto2025.n44.7889.",
    doi="10.26439/contratexto2025.n44.7889",
)
write_entry(
    "2024-peace-conflict-neighborhood-uprising-badilla",
    "When my neighborhood woke up: knitting collective action amid the 2019 Chilean uprising",
    "Movilización en barrios postergados durante el estallido.",
    "Peace and Conflict: Journal of Peace Psychology, 30",
    "articulo",
    "2024-11-01",
    "Rajevic, M. B., & Vargas, A. O.",
    ["manuela-badilla"],
    "Rajevic, M. B., & Vargas, A. O. (2024). When my neighborhood woke up: knitting collective action in disadvantaged areas amid the 2019 Chilean uprising. *Peace and Conflict: Journal of Peace Psychology*, 30. [DOI](https://doi.org/10.1037/pac0000706)",
    "Rajevic, M. B., & Vargas, A. O. (2024). When my neighborhood woke up: knitting collective action in disadvantaged areas amid the 2019 Chilean uprising. *Peace and Conflict: Journal of Peace Psychology*, 30. DOI 10.1037/pac0000706.",
    doi="10.1037/pac0000706",
)

# Luciano / otros OLES — evitar duplicar Psyké 2023 y Peace & Conflict 2025 (ya en sitio)

write_entry(
    "2025-working-fear-police-legitimacy-gerber",
    "Fear of the police and the fragility of legitimacy (en revisión)",
    "Insights from Chile y Brasil; manuscrito en evaluación.",
    "Working paper · en revisión",
    "working-paper",
    "2025-11-01",
    "Gerber, M. M., Branco, F. C., Cubas, V., Fuentealba, L. S., Deneken, M., Jackson, J.",
    ["monica-gerber", "luciano-saez-fuentealba", "matias-deneken"],
    "Gerber, M. M., Branco, F. C., Cubas, V., Fuentealba, L. S., de Oliveira, A. R., Deneken, M., & Jackson, J. (en revisión). Fear of the police and the fragility of legitimacy: insights from Chile and Brazil.",
    "Gerber *et al*. (en revisión). Fear of the police and the fragility of legitimacy: insights from Chile and Brazil.",
)
write_entry(
    "2025-working-vignette-games-guide-puga-saez",
    "Orientaciones para aplicación de juegos de clasificación de viñetas (en revisión)",
    "Reflexiones metodológicas desde un estudio empírico.",
    "Working paper · en revisión",
    "working-paper",
    "2025-10-01",
    "Puga, I., & Sáez, F.",
    ["ismael-puga", "luciano-saez-fuentealba"],
    "Puga, I., & Sáez, F. (en revisión). Orientaciones para la aplicación de juegos de clasificación de viñetas: reflexiones y recomendaciones a partir de un estudio empírico.",
    "Puga, I., & Sáez, F. (en revisión). Orientaciones para la aplicación de juegos de clasificación de viñetas.",
)
write_entry(
    "2025-forthcoming-politica-sociedad-ideas-constituyente",
    "Atribuciones de ideas y proceso constituyente en Chile (aceptado)",
    "Estudio cualitativo sobre consensos en tiempos de incertidumbre.",
    "Política y Sociedad (aceptado)",
    "articulo",
    "2025-12-01",
    "Sáez, L., Puga, I., Gerber, M., Figueiredo, A., & Moya, C.",
    ["luciano-saez-fuentealba", "ismael-puga", "monica-gerber", "ana-figueiredo", "cristobal-moya"],
    "Sáez, L., Puga, I., Gerber, M., Figueiredo, A., & Moya, C. (aceptado). Atribuciones de ideas y proceso constituyente en Chile: estudio cualitativo sobre construcción de consensos en tiempos de incertidumbre. *Política y Sociedad*.",
    "Sáez, L., Puga, I., Gerber, M., Figueiredo, A., & Moya, C. (aceptado). Atribuciones de ideas y proceso constituyente en Chile. *Política y Sociedad*.",
)
write_entry(
    "2025-jpola-motivational-postures-qualitative-saez",
    "How do people relate to the police? A qualitative study on motivational postures in Chile",
    "Estudio cualitativo sobre posturas hacia la policía.",
    "Journal of Politics in Latin America, 18(1), 61–85",
    "articulo",
    "2025-04-01",
    "Sáez, L., Gerber, M. M., Orchard, M., Rojas, B., & Figueiredo, A.",
    ["luciano-saez-fuentealba", "monica-gerber", "macarena-orchard", "bruno-rojas", "ana-figueiredo"],
    "Sáez, L., Gerber, M. M., Orchard, M., Rojas, B., & Figueiredo, A. (2025). How do people relate to the police? A qualitative study on motivational postures towards the police in Chile. *Journal of Politics in Latin America*, 18(1), 61–85. [DOI](https://doi.org/10.1177/1866802X251397948)",
    "Sáez, L., *et al*. (2025). *Journal of Politics in Latin America*, 18(1). DOI 10.1177/1866802X251397948.",
    doi="10.1177/1866802X251397948",
)
write_entry(
    "2025-castalia-actor-red-psicofarmacos-saez",
    "¿Pueden hablar los psicofármacos? Teoría del actor-red e infancia",
    "Uso de psicofármacos en infancias y adolescencias.",
    "Castalia – Revista de Psicología de la Academia (44)",
    "articulo",
    "2025-05-01",
    "Pinto Venegas, J., & Sáez-Fuentealba, L.",
    ["luciano-saez-fuentealba"],
    "Pinto Venegas, J., & Sáez-Fuentealba, L. (2025). ¿Pueden hablar los psicofármacos? Aproximaciones desde la teoría del actor-red sobre el uso de psicofármacos en infancias y adolescencias. *Castalia*, (44), 51–69. [DOI](https://doi.org/10.25074/07198051.44.2889)",
    "Pinto Venegas, J., & Sáez-Fuentealba, L. (2025). *Castalia*, (44). DOI 10.25074/07198051.44.2889.",
    doi="10.25074/07198051.44.2889",
)
write_entry(
    "2024-castalia-infomes-ddhh-estallido-saez",
    "\"Ensamblajes y performatividad de la verdad\": informes de DDHH y estallido",
    "Agencia de informes durante el estallido social.",
    "Castalia. Revista de Psicología de la Academia",
    "articulo",
    "2024-07-01",
    "Sáez Fuentealba, L.",
    ["luciano-saez-fuentealba"],
    "Sáez Fuentealba, L. (2024). «Ensamblajes y performatividad de la verdad»: la agencia de los informes sobre violaciones a los derechos humanos durante el estallido social chileno. *Castalia*. [DOI](https://doi.org/10.25074/07198051.43.2842)",
    "Sáez Fuentealba, L. (2024). *Castalia*. DOI 10.25074/07198051.43.2842.",
    doi="10.25074/07198051.43.2842",
)
write_entry(
    "2024-colombia-int-violencia-pobladores-dictadura-saez",
    "Violencia hacia pobladores en dictadura: disputas sobre narrativas oficiales (1973–2023)",
    "Historiografía y violencia política.",
    "Colombia Internacional, 119, 37–64",
    "articulo",
    "2024-03-01",
    "Sáez Fuentealba, L.",
    ["luciano-saez-fuentealba"],
    "Sáez Fuentealba, L. (2024). El lugar de la violencia hacia los pobladores durante la dictadura cívico-militar en Chile: disputas y silenciamientos en la construcción de narrativas oficiales (1973–2023). *Colombia Internacional*, 119, 37–64. [DOI](https://doi.org/10.7440/colombiaint119.2024.02)",
    "Sáez Fuentealba, L. (2024). *Colombia Internacional*, 119. DOI 10.7440/colombiaint119.2024.02.",
    doi="10.7440/colombiaint119.2024.02",
)
write_entry(
    "2024-pensamiento-educativo-observatorio-investigacion-saez",
    "Significados de la investigación en estudiantes de pregrado vía observatorio universitario",
    "Participación estudiantil en observatorio.",
    "Pensamiento Educativo, 61(1)",
    "articulo",
    "2024-09-01",
    "Sáez, L., Gerber, M. M., Orchard, M., & Figueiredo, A.",
    ["luciano-saez-fuentealba", "monica-gerber", "macarena-orchard", "ana-figueiredo"],
    "Sáez, L., Gerber, M. M., Orchard, M., & Figueiredo, A. (2024). Significados atribuidos a la investigación en estudiantes de pregrado: la experiencia de participación en un observatorio de investigación universitario. *Pensamiento Educativo*, 61(1). [DOI](https://doi.org/10.7764/PEL.61.1.2024.8)",
    "Sáez, L., *et al*. (2024). *Pensamiento Educativo*, 61(1). DOI 10.7764/PEL.61.1.2024.8.",
    doi="10.7764/PEL.61.1.2024.8",
)
write_entry(
    "2020-disenso-regimenes-veridiccion-saez",
    "Pactos vigentes, peligros latentes: regímenes de veridicción y octubre chileno",
    "Análisis del largo octubre chileno.",
    "Disenso, 1(2), 91–102",
    "articulo",
    "2020-12-01",
    "Sáez, L.",
    ["luciano-saez-fuentealba"],
    "Sáez, L. (2020). Pactos vigentes, peligros latentes. Regímenes de veridicción frente al largo octubre chileno. *Disenso*, 1(2), 91–102.",
    "Sáez, L. (2020). *Disenso*, 1(2), 91–102.",
)
write_entry(
    "2020-castalia-economia-moral-victimas-saez",
    "Re-pensar la economía moral de las víctimas (1990–2020)",
    "Gestión gubernamental y resistencia en historia reciente chilena.",
    "Castalia, 34, 73–89",
    "articulo",
    "2020-08-01",
    "Sáez, L.",
    ["luciano-saez-fuentealba"],
    "Sáez, L. (2020). Re-pensar la economía moral de las víctimas: entre la gestión gubernamental y la resistencia en la historia reciente chilena. *Castalia*, 34, 73–89. [DOI](https://doi.org/10.25074/07198051.34.1686)",
    "Sáez, L. (2020). *Castalia*, 34. DOI 10.25074/07198051.34.1686.",
    doi="10.25074/07198051.34.1686",
)
write_entry(
    "2018-divergencia-campana-antichilena-saez",
    "Chile vs el mundo: la revista Qué Pasa y la campaña antichilena",
    "Análisis de medios y diplomacia cultural.",
    "Divergencia, 11, 127–146",
    "articulo",
    "2018-06-01",
    "Santoni, A., & Sáez, L.",
    ["luciano-saez-fuentealba"],
    "Santoni, A., & Sáez, L. (2018). Chile vs El Mundo. El caso de la revista Qué Pasa y la campaña antichilena. *Divergencia*, 11, 127–146.",
    "Santoni, A., & Sáez, L. (2018). *Divergencia*, 11, 127–146.",
)
write_entry(
    "2018-tiempo-historico-lobbying-embajada-saez",
    "Lobbying y difusión de la Embajada de Chile en España (1983–1988)",
    "Historia política y diplomacia.",
    "Tiempo Histórico, 17, 87–107",
    "articulo",
    "2018-11-01",
    "Santoni, A., Elgueta, R., & Sáez, L.",
    ["luciano-saez-fuentealba"],
    "Santoni, A., Elgueta, R., & Sáez, L. (2018). En direcciones opuestas: la acción de lobbying y de difusión de la Embajada de Chile en la España de Felipe González (1983–1988). *Tiempo Histórico*, 17, 87–107.",
    "Santoni, A., Elgueta, R., & Sáez, L. (2018). *Tiempo Histórico*, 17, 87–107.",
)
write_entry(
    "2017-divergencia-masacre-apoquindo-saez",
    "Los caminos de la inmunización democrática: la masacre de Apoquindo (1993)",
    "Memoria y violencia política.",
    "Divergencia, 7, 71–101",
    "articulo",
    "2017-05-01",
    "Sáez, L.",
    ["luciano-saez-fuentealba"],
    "Sáez, L. (2017). Los caminos de la inmunización democrática. Ecos y significados de La Masacre de Apoquindo, 21 octubre de 1993. *Divergencia*, 7, 71–101.",
    "Sáez, L. (2017). *Divergencia*, 7, 71–101.",
)

print("Done.")

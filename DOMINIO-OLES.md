# Publicar en www.oles.cl (GitHub Pages)

El sitio compilado va a `docs/`. GitHub Pages puede servir esa carpeta con dominio propio **www.oles.cl**.

## 1. Repositorio en GitHub

1. Sube este proyecto a un repositorio (por ejemplo `tu-org/oles-page`).
2. En el repo: **Settings → Pages**.
3. **Build and deployment → Source:** *Deploy from a branch*.
4. **Branch:** `main` (o la rama que uses) y carpeta **`/docs`**.
5. Guarda.

## 2. Dominio personalizado en GitHub

En la misma página **Pages**:

1. En **Custom domain** escribe: `www.oles.cl`
2. Guarda. GitHub comprobará el DNS (puede tardar minutos u horas).
3. Cuando esté verde, activa **Enforce HTTPS**.

Opcional: en el mismo campo o en DNS, configura también **oles.cl** (sin www) para que redirija a `www.oles.cl` (ver paso 3).

El archivo **`CNAME`** en la raíz del proyecto (se copia a `docs/` al hacer `quarto render`) debe contener solo:

```text
www.oles.cl
```

## 3. DNS en NIC Chile (nic.cl)

Si **oles.cl** está en [NIC Chile](https://www.nic.cl), configura la zona DNS ahí (no hace falta otro proveedor salvo que hayas delegado los nameservers a Cloudflare u otro).

### 3.1 Entrar al panel

1. Inicia sesión en **https://www.nic.cl**
2. **Mis dominios** → elige **oles.cl**
3. Abre **Configuración técnica** / **Administración DNS** / **Zona DNS** (el nombre exacto puede variar según la vista de NIC)
4. Asegúrate de usar la **zona DNS de NIC** (servidores tipo `ns1.nic.cl`, `ns2.nic.cl`). Si el dominio apunta a nameservers externos, los registros se editan en ese otro panel, no en NIC.

### 3.2 Registros a crear

Sustituye `USUARIO` por tu usuario u organización de GitHub (ej. si el repo es `matdknu/oles-page`, el destino del CNAME es **`matdknu.github.io`**).

| Tipo | Host / nombre | Valor | TTL (si preguntan) |
|------|----------------|--------|---------------------|
| **CNAME** | `www` | `USUARIO.github.io` | 3600 o por defecto |
| **A** | `@` o vacío (raíz **oles.cl**) | `185.199.108.153` | por defecto |
| **A** | `@` | `185.199.109.153` | por defecto |
| **A** | `@` | `185.199.110.153` | por defecto |
| **A** | `@` | `185.199.111.153` | por defecto |

**Importante para el CNAME:**

- El valor debe ser solo `USUARIO.github.io` **sin** `https://` y **sin** barra final.
- En algunos paneles NIC el host del CNAME es `www` y en otros `www.oles.cl`; usa lo que el formulario indique (suele bastar `www`).

**Registros A (raíz):** las cuatro IPs son las oficiales de GitHub Pages para el dominio apex (`oles.cl`). Así tanto `www.oles.cl` como `oles.cl` llegan a GitHub; en **Settings → Pages** puedes dejar como dominio preferido `www.oles.cl`.

### 3.3 Qué no hace falta (o conviene revisar)

- No pongas CNAME en la raíz `@` (NIC/GitHub no lo permiten bien para apex); usa las **A** de arriba.
- Si ya existen registros **A** o **CNAME** de un hosting antiguo para `www` o `@`, **cámbialos** o bórralos para que no compitan con GitHub.
- Registros **MX** (correo): déjalos como estén si usáis email con `@oles.cl`; no interfieren con la web si el correo sigue en sus propios registros MX.

### 3.4 Propagación

En `.cl` los cambios suelen verse entre **15 minutos y 24–48 horas**. GitHub en **Pages** mostrará el dominio como verificado cuando el DNS responda bien.

Comprobar desde tu Mac:

```bash
dig www.oles.cl CNAME +short
dig oles.cl A +short
```

Deberías ver el CNAME hacia `….github.io` y las cuatro IPs de GitHub en la raíz.

Documentación GitHub: [dominio personalizado en Pages](https://docs.github.com/es/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site).

## 4. Flujo de actualización del sitio

Cada vez que cambies contenido:

```bash
quarto render
git add .
git commit -m "Actualizar sitio"
git push
```

No hace falta build en la nube si compilas en local y subes `docs/` ya generado.

## 5. Comprobar

- `https://www.oles.cl` — sitio principal  
- `https://oles.cl` — debería redirigir a www (si configuraste apex + GitHub)  
- Certificado HTTPS: lo emite GitHub tras validar el dominio  

## Notas

- **`_quarto.yml`** incluye `site-url: https://www.oles.cl` para enlaces canónicos al publicar.
- Si el repo es **privado**, GitHub Pages en plan gratuito de cuenta personal puede tener límites; en organizaciones revisa el plan.
- Tamaño actual de `docs/`: ~200 MB; compatible con GitHub Pages (límite orientativo ~1 GB por sitio).

# Como armar el cv

El CV ahora se construye como parte del sitio estático.

## Con mise

```bash
mise run build
```

Esto genera:
- `dist/cv/en.html`
- `dist/cv/es.html`

PDFs:

```bash
mise run cv:pdf
```

Esto genera:
- `out/cv-en.pdf`
- `out/cv-es.pdf`

Preview local:

```bash
mise run serve
```

Y luego:
- `http://localhost:8000/cv/en.html`
- `http://localhost:8000/cv/es.html`

## Dependencias

- `pandoc` (gestionado por `mise`)
- `python`
- `uv` / `uvx` para PDFs

---
title: Cómo contribuir
description: El sitio es open source. Corrige, agrega, traduce o manda tu historia.
---

Este sitio es **open source**: todo el contenido está en un repositorio público en GitHub, y cualquiera puede sugerir cambios. ¿Encontraste algo mal, desactualizado, o tienes un tip mejor? Contribuye.

## Forma fácil (sin saber Git)

### Sugerir una corrección o algo nuevo en una página

1. Crea una cuenta en [GitHub](https://github.com) (es gratis).
2. Al final de cualquier página de este sitio, haz clic en **"Editar página"**.
3. GitHub va a abrir el archivo del texto. Haz clic en el lápiz y haz tu cambio.
4. Haz clic en **"Commit changes…"** y luego en **"Propose changes"**, escribe rapidito qué cambiaste y por qué.
5. Listo, eso crea un *pull request*. Alguien lo revisa y, si está todo bien, entra al sitio.

### Mandar una historia o sugerir una empresa

En el repositorio de GitHub (el ícono de arriba, en la esquina), ve a **Issues → New issue** y elige el formulario:

- **Novo relato** (nueva historia) — cuenta cómo lograste trabajar para afuera.
- **Sugerir empresa** — una empresa, consultora o agencia que contrata latinos.
- **Correção** (corrección) — algo mal o desactualizado que no quieres editar tú mismo.

## Forma a la antigua (sabes Git)

```bash
git clone <url-do-repositório>
cd devemdolar
npm install
npm run dev
```

El sitio corre en `http://localhost:4321`. Los textos están en `src/content/docs/<idioma>/`. Haz un fork, crea una branch y manda el pull request.

## Traducciones

El sitio existe en **portugués, español e inglés**. El portugués es la versión original. Si cambiaste algo en español y sabes portugués o inglés, actualiza las otras versiones también (o avisa en el pull request que hay que actualizarlas).

El mismo archivo existe en cada idioma, con el mismo nombre:

```
src/content/docs/pt/resume.md
src/content/docs/es/resume.md
src/content/docs/en/resume.md
```

## Reglas de la casa

- **Mantén el tono.** El sitio es informal y medio grosero a propósito. No hace falta convertirlo en artículo de LinkedIn.
- **Nada de ventas.** Sin links de afiliado, cursos, mentorías, ni "escríbeme por DM". Un PR así se cierra al instante.
- **Fuente cuando sea un hecho.** Leyes, impuestos, estudios, números: pon el link.
- **Libros solo en inglés.**
- **No expongas a nadie.** Nada de nombres de compañeros, jefes, ni datos confidenciales de empresas.

## Licencia

El contenido está bajo [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.es): puedes copiarlo y adaptarlo, siempre que des crédito y mantengas la misma licencia. El código del sitio está bajo licencia MIT.

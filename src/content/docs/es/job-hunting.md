---
title: Buscar vacantes
description: "Búsqueda booleana, LinkedIn Posts, Google con site: y HiringCafe. Dónde están las vacantes buenas."
---

Para ligar con chavas (o chavos), nunca te debes autorrechazar, sino dejar que la otra persona decida si te rechaza o no. Lo mismo aplica para las vacantes.

> "El no ya lo tengo, voy por la humillación."

Aquí es donde empieza la verdadera batalla. Probablemente te vas a postular a decenas de vacantes antes de que te llamen a una entrevista, y está bien. Eres uno más en un mar de gente, pero tarde o temprano también vas a picar. Yo en lo personal solo busco de tres formas: **LinkedIn, Google y HiringCafe**.

## Búsqueda booleana

Tanto para LinkedIn como para Google, vas a usar **búsqueda booleana** (*boolean search*). Nomás es armar la búsqueda con operadores lógicos para decir exactamente qué quieres y qué no:

| Operador | Qué hace | Ejemplo |
|---|---|---|
| `"comillas"` | Busca la expresión exacta | `"Power BI"` (y no "power" y "BI" sueltos) |
| `OR` | Cualquiera de los términos | `"Power BI" OR Tableau` |
| `AND` | Todos los términos tienen que aparecer | `"Power BI" AND remote` |
| `NOT` (LinkedIn) o `-` (Google) | Excluye el término | `NOT India` / `-India` |
| `( )` | Agrupa las cosas, igual que en matemáticas | `("Power BI" OR Tableau) AND remote` |

Reglas que todo el mundo la riega:

- En LinkedIn, `AND`, `OR` y `NOT` tienen que ir en **MAYÚSCULAS**. En minúsculas los ignora.
- En Google, `AND` no existe (todos los términos ya son obligatorios por defecto), y para excluir es el signo de menos pegado a la palabra: `-India`.
- En LinkedIn, siempre usa paréntesis cuando mezcles `OR` con `AND`, si no el resultado se vuelve un desmadre.
- Google ignora los paréntesis, pero no pasa nada: ahí el `OR` ya se "pega" a los términos vecinos, así que `"Power BI" OR Tableau remote` funciona como `("Power BI" OR Tableau) remote`.

La estructura que funciona es: **(tus puestos/stack) AND (remoto) AND (dónde puedes trabajar) NOT (lo que no quieres)**. Ejemplo para mi stack:

```
("Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer") AND (remote OR "work from anywhere") AND (LATAM OR "Latin America" OR Brazil OR "South America") NOT (hybrid OR onsite OR "on-site")
```

Cambia los términos del primer paréntesis por tu stack y listo (y si no eres de Brasil, cambia `Brazil` por tu país). Vale la pena guardar unas 3 o 4 variaciones (una más amplia, una solo con tu puesto exacto, una con "contractor" en lugar de "remote") e ir alternando.

## LinkedIn

Ahora que ya le sabes, nomás copia y pega tu búsqueda booleana en la barra de búsqueda de LinkedIn. Y luego le das clic a *Empleos*, ¿verdad?

**¡FALSO!**

En la pestaña de empleos la mayoría son vacantes fantasma, te vas a postular a una montaña de vacantes para que nunca te llamen, solo una que otra es legítima. Solo vale la pena postularte por ahí si son esas de *Easy Apply* en las que ni pierdes tiempo. Hoy en día seguro hay alguna forma de usar IA para hacerlo en masa, pero nunca lo he buscado.

Vas a buscar solo en **Posts** (en LinkedIn en español aparece como *Publicaciones*). Siempre que un reclutador publica una vacante legítima, también la comparte, así que es una forma de filtrar. Ordena por **Más recientes**.

En los posts también va a haber mucha basura, sobre todo porque hay muchos indios publicando vacantes scam o vacantes solo para India. Vas a darle clic a los posts, leer el nombre de quien publicó, si es indio ya lo puedes ignorar, y así te vas. ¿Es aburrido? Un montón, pero es donde están las mejores vacantes. Busca nombres claramente anglosajones, latinos, o tal vez hasta de Europa del Este. Ahí sí lees el texto.

Hoy en día esos también tienen buena probabilidad de ser scam. Señales de que es estafa:

- Texto extremadamente genérico ("We are hiring! Multiple positions! DM me!").
- Contacto por e-mail `@gmail.com`, `@zohomail.com`, `@outlook.com`, o peor, Telegram/WhatsApp.
- Salario demasiado bueno para tan pocos requisitos.
- Empresa que no tiene sitio web, o cuyo sitio se creó el mes pasado.
- Te piden pagar algo (capacitación, equipo, "cuota de procesamiento"). Una vacante legítima **nunca** te cobra.

Las vacantes legítimas te van a mandar o al propio LinkedIn, o a la plataforma de reclutamiento de la empresa, lo que nos lleva a la siguiente forma de buscar:

## Google

Aquí vas a mantener la búsqueda booleana de LinkedIn (adaptada a Google: sin `AND`, sin paréntesis y con `-` en lugar de `NOT`), solo que al principio de la búsqueda vas a poner las plataformas de reclutamiento (ATS) más comunes. Tu búsqueda va a quedar así:

```
site:greenhouse.io "Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer" remote OR "work from anywhere" LATAM OR "Latin America" OR Brazil OR "South America" -hybrid -onsite
```

Luego cambias el `site:` por las otras plataformas:

| Plataforma | Qué poner en el `site:` |
|---|---|
| Greenhouse | `site:greenhouse.io` (agarra `boards.` y `job-boards.`) |
| Lever | `site:jobs.lever.co` |
| Ashby | `site:jobs.ashbyhq.com` |
| Workable | `site:apply.workable.com` |
| SmartRecruiters | `site:jobs.smartrecruiters.com` |
| Recruitee | `site:recruitee.com` |
| BambooHR | `site:bamboohr.com` |
| Breezy HR | `site:breezy.hr` |
| Workday | `site:myworkdayjobs.com` |
| Rippling | `site:ats.rippling.com` |
| Wellfound (startups) | `site:wellfound.com` |

Filtra en Google por la **última semana** (o últimas 24 horas): *Herramientas → Cualquier fecha → Última semana*.

Y ve dándole clic a los sitios y viendo las vacantes. Cuando termines todas las que salieron, pasa al siguiente sitio.

Este proceso en LinkedIn y en Google lo vas a hacer **todos los días**. En LinkedIn, dos veces al día, en la mañana y en la noche. ¡No te rindas! Si ves una vacante fresca, la probabilidad de que te llamen es mucho más alta que en una vacante que publicaron hace unos días.

## HiringCafe

[HiringCafe](https://hiringcafe.com) es una plataforma hecha por un usuario de reddit, y es por mucho la mejor plataforma de vacantes que he visto. Agregan directamente de los sitios que buscaste en Google, pero puede que una que otra cosa no aparezca ahí.

Ahí vas a dejar tu búsqueda guardada y la vas a revisar todos los días. Cuando veas una vacante que encaje con tu perfil, no solo te vas a postular: ve a LinkedIn, busca empleados de la empresa y agrégalos. **Sobre todo a los reclutadores.**

## Empresas que contratan latinos

Más adelante voy a agregar a este sitio empresas que contratan brasileños o latinos de forma remota, ya sean consultoras, agencias de reclutamiento o la propia empresa. Nomás tengo que hacerle scrape a mis e-mails para sacar la lista completa.

Mientras tanto, hay una página de [empresas y plataformas](/es/companies/) que la comunidad va llenando. Si trabajas o trabajaste en una empresa que contrata latinos remotos, manda un pull request.

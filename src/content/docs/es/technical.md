---
title: Técnico
description: Domina tu stack. Lo que un dev necesita saber en la era de la IA, y los libros que valen la pena.
---

El conocimiento técnico es mucho más subjetivo que el inglés y va a depender de tu bagaje profesional. Yo mismo soy analista de datos, especialista en Power BI. Mi stack incluye el propio Power BI, SQL, Python, modelado de datos, data warehousing (Snowflake y Databricks), etc. No es precisamente el stack con más vacantes, pero como vieron antes, las conseguí de todos modos.

Lo más importante es que seas **bueno en lo que haces**, sobre todo si aspiras a hacer OE (*overemployment*, tener más de un trabajo al mismo tiempo). Hay quien dice que Power BI es fácil, pero es porque no tienen idea del tamaño del desmadre que arma un cuate que hizo un curso de 20 horas y se cree la última Coca-Cola del desierto.

**Domina tu stack.**

## Teclear código ya no vale nada

Hoy en día, solo saber teclear código importa poco. Claude escribe más código en una hora del que tú escribirías en 10 años. Lo que la IA no tiene es la **subjetividad**. Tienes que dominar las reglas de negocio, saber cómo se integran los sistemas, interactuar con los stakeholders, entender la arquitectura, comprender cómo debe funcionar el sistema en sí. Ahí sí, le delegas las tasks a la IA para que codee, cree tests, etc.

La era de los cursitos de "Aprende a programar y vuélvete Dev" se acabó. El estudio tiene que ser más profundo, y para eso hay dos caminos: **lectura e implementación**. Obviamente lectura aquí también pueden ser videos, pero ya entendieron.

## Lo que necesitas dominar

Lo básico que nunca cambia:

- **Algoritmos y estructuras de datos** — complejidad, cuándo usar hash map, árbol, cola. No es para memorizarte LeetCode, es para saber por qué esa query o ese loop está lento.
- **Reglas de negocio** — entender *por qué* existe el sistema y quién gana dinero con él.
- **Modelado de datos** — normalización, modelado dimensional, cuándo desnormalizar.
- **Deployment** — cómo tu código sale de tu máquina y llega a producción.

Y lo que separa al dev de la era de la IA del tecleador de código:

- **System design** — cómo armar un sistema que aguante carga: cache, colas, load balancer, réplicas de base de datos, consistencia vs. disponibilidad. Es lo que te preguntan en entrevista de senior y es justo lo que la IA no decide sola.
- **Bases de datos por dentro** — índices, transacciones, locks, plan de ejecución. La IA escribe la query, tú tienes que saber por qué tarda 40 segundos.
- **Diseño de APIs e integraciones** — REST, eventos, webhooks, idempotencia, versionado, contratos entre sistemas.
- **Cloud** — por lo menos una de las grandes (AWS, Azure o GCP) al nivel de saber qué hace cada pieza y cuánto cuesta.
- **Containers, CI/CD e Infra as Code** — Docker, pipelines de deploy, Terraform. Ya nadie sube cosas a producción arrastrando archivos.
- **Observabilidad** — logs, métricas, traces y alertas. Saber descubrir *por qué* se rompió a las 3 de la mañana.
- **Seguridad** — lo básico de OWASP, manejo de secretos, autenticación y autorización. Al código generado por IA le encanta filtrar API keys.
- **Tests** — saber qué vale la pena testear y cómo. La IA escribe tests rapidísimo, pero un test malo solo da una falsa sensación de seguridad.
- **Costos** — FinOps. Afuera, la pregunta "¿cuánto cuesta esto al mes?" sale muchísimo más que aquí.
- **Revisar código de IA** — leer código que no escribiste, encontrar el bug sutil, y saber decir "no, hazlo de otra forma". Esa es la skill más subestimada de 2026.
- **Trabajar con LLMs** — ingeniería de contexto, evaluación (evals), RAG, agentes. Aunque no seas de IA, todo producto le está metiendo IA por algún lado.

## Implementa

Mientras vas estudiando la base, también es importante implementar. Hoy es más fácil que nunca, nomás pagas un plan de 20 dólares de Claude y puedes implementar lo que sea.

Mientras vas implementando, lo más importante es que **entiendas las decisiones técnicas que está tomando la IA**. Recuerda, estás aprendiendo. Lee el código, trata de entenderlo, PREGUNTA. Haz de cuenta que Claude es un senior medio autista pero que es una bestia programando, y cualquier duda que tengas, se la puedes preguntar. Pídele que explore otra solución que se te ocurrió, que implemente una feature nueva, y ve haciendo crecer tu proyectito.

## Proyectos personales

Ten siempre la mente abierta a posibles proyectos personales. Algunos ejemplos de proyectos que hice hace poco:

1. Extraer datos públicos de la alcaldía de mi ciudad para tratar de identificar patrones de fraude. Descubrí que la administración actual contrata MUCHÍSIMO MÁS personal tercerizado.
2. Extraer datos de la API de Path of Exile 2 para saber qué mods de tablet vender. GGG, regresen los scarabs, ¡nadie aguanta andar dándole reforge a 500 tablets de expedition!
3. Agarré los datos de la tabla FIPE (la referencia de precios de autos usados en Brasil) que otro usuario de reddit compartió para armar un dashboard que ayude a decidir qué carro comprar.
4. El ERP de Olist tiene unas gráficas medio de mierda, así que armé una extracción de los datos de ahí, e hice un dashboard de ventas e inventario para la tienda de mi esposa.
5. Este mismo sitio, al que le estoy metiendo un montón de firuletes. Escribí la mayor parte del texto a mano, pero le dije a Claude que usara Higgsfield y se luciera con el diseño para que quedara bonito.

La IA ha democratizado el desarrollo, así que hoy hay posibilidades infinitas de lo que se puede hacer. Casi ninguna va a ser rentable, pero muchas pueden ser proyectos interesantes, y todas se vuelven tema de conversación en la entrevista. ¡Suéltale rienda a tu creatividad!

## Libros

Algunos libros indispensables, dependiendo del stack. Otros usuarios, siéntanse libres de agregar libros a esta lista (nomás manden un pull request). Ah, y recuerden: **solo libros en inglés**.

### Computación en general (todo el mundo debería leerlos)

| Libro | Autor | Por qué |
|---|---|---|
| [The Pragmatic Programmer (20th Anniversary)](https://www.amazon.com/dp/0135957052) | David Thomas, Andrew Hunt | El manual de cómo ser un profesional decente |
| [A Philosophy of Software Design](https://www.amazon.com/dp/173210221X) | John Ousterhout | Corto y directo: cómo reducir la complejidad |
| [Code: The Hidden Language of Computer Hardware and Software](https://www.amazon.com/dp/0137909101) | Charles Petzold | Entiende cómo funciona una computadora de verdad |
| [Computer Systems: A Programmer's Perspective](https://www.amazon.com/dp/013409266X) | Randal Bryant, David O'Hallaron | El libro de texto de sistemas para los que no estudiaron computación |
| [Software Engineering at Google](https://www.amazon.com/dp/1492082791) | Titus Winters et al. | Cómo funciona la ingeniería a escala |

### Algoritmos y entrevistas

| Libro | Autor | Por qué |
|---|---|---|
| [Grokking Algorithms (2nd Edition)](https://www.amazon.com/dp/1633438538) | Aditya Bhargava | Algoritmos con dibujitos, para los traumados |
| [Introduction to Algorithms (CLRS)](https://www.amazon.com/dp/026204630X) | Cormen, Leiserson, Rivest, Stein | La biblia. No es para leerlo completo, es para consultarlo |
| [Cracking the Coding Interview](https://www.amazon.com/dp/0984782850) | Gayle Laakmann McDowell | Sigue siendo el estándar para entrevistas de live coding |
| [System Design Interview, Vol. 1](https://www.amazon.com/s?k=System+Design+Interview+Alex+Xu) | Alex Xu | La entrevista de system design masticadita |

### Backend y arquitectura

| Libro | Autor | Por qué |
|---|---|---|
| [Designing Data-Intensive Applications (2nd Edition)](https://www.amazon.com/dp/1098119061) | Martin Kleppmann, Chris Riccomini | El mejor libro técnico de la última década. Punto. La 2ª edición salió en 2026 |
| [Database Internals](https://www.amazon.com/dp/1492040347) | Alex Petrov | Cómo funciona una base de datos por dentro |
| [Clean Architecture](https://www.amazon.com/dp/0134494164) | Robert C. Martin | Léelo con sentido crítico, pero léelo |
| [Domain-Driven Design](https://www.amazon.com/dp/0321125215) | Eric Evans | Cómo traducir reglas de negocio a código |
| [Refactoring (2nd Edition)](https://www.amazon.com/dp/0134757599) | Martin Fowler | Cómo meterle mano a código legacy sin romper todo |

### Datos y analytics

| Libro | Autor | Por qué |
|---|---|---|
| [The Data Warehouse Toolkit](https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802) | Ralph Kimball, Margy Ross | Modelado dimensional, la base de todo BI |
| [Fundamentals of Data Engineering](https://www.amazon.com/dp/1098108302) | Joe Reis, Matt Housley | El mapa completo de la ingeniería de datos |
| [Analytics Engineering with SQL and dbt](https://www.amazon.com/dp/1098142381) | Rui Machado, Hélder Russa | dbt y la capa de transformación |
| [Spark: The Definitive Guide](https://www.amazon.com/dp/1491912219) | Bill Chambers, Matei Zaharia | Si le mueves a Databricks, es obligatorio |
| [SQL Performance Explained](https://www.amazon.com/dp/3950307826) | Markus Winand | Índices y planes de ejecución, bien explicados |
| [Practical Statistics for Data Scientists](https://www.amazon.com/dp/149207294X) | Peter Bruce, Andrew Bruce, Peter Gedeck | La estadística que de verdad usas |

### Power BI

| Libro | Autor | Por qué |
|---|---|---|
| [The Definitive Guide to DAX](https://www.amazon.com/Definitive-Guide-DAX-Alberto-Ferrari/dp/0138244723) | Alberto Ferrari, Marco Russo | Si no lo leíste, no sabes DAX. Este link es de la 3ª edición |

### Machine learning e IA

| Libro | Autor | Por qué |
|---|---|---|
| [Hands-On Machine Learning (3rd Edition)](https://www.amazon.com/dp/1098125975) | Aurélien Géron | El mejor libro práctico de ML |
| [Designing Machine Learning Systems](https://www.amazon.com/dp/1098107969) | Chip Huyen | ML en producción, no en un notebook |
| [AI Engineering](https://www.amazon.com/dp/1098166302) | Chip Huyen | Cómo construir producto encima de un LLM |

### DevOps, SRE y cloud

| Libro | Autor | Por qué |
|---|---|---|
| [Site Reliability Engineering](https://www.amazon.com/dp/149192912X) | Google | Cómo mantiene Google las cosas en el aire |
| [Accelerate](https://www.amazon.com/dp/1942788339) | Nicole Forsgren, Jez Humble, Gene Kim | Lo que de verdad hace que un equipo entregue rápido |
| [The DevOps Handbook (2nd Edition)](https://www.amazon.com/dp/1950508404) | Gene Kim et al. | El manual práctico de DevOps |
| [Terraform: Up & Running (3rd Edition)](https://www.amazon.com/dp/1098116747) | Yevgeniy Brikman | Infra as Code como debe ser |

### Lenguajes y frontend

| Libro | Autor | Por qué |
|---|---|---|
| [Fluent Python (2nd Edition)](https://www.amazon.com/dp/1492056359) | Luciano Ramalho | Escrito por un brasileño, por cierto |
| [Effective Java (3rd Edition)](https://www.amazon.com/dp/0134685997) | Joshua Bloch | Obligatorio si eres de Java |
| [Eloquent JavaScript (4th Edition)](https://www.amazon.com/dp/1718504101) | Marijn Haverbeke | JavaScript bien hecho (y gratis en línea) |
| [Don't Make Me Think, Revisited](https://www.amazon.com/dp/0321965515) | Steve Krug | Usabilidad, para dejar de hacer pantallas feas |

### Negocios y carrera

| Libro | Autor | Por qué |
|---|---|---|
| [Storytelling with Data](https://www.amazon.com/dp/1119002257) | Cole Nussbaumer Knaflic | Cómo mostrarle datos a quien decide |
| [The Staff Engineer's Path](https://www.amazon.com/dp/1098118731) | Tanya Reilly | Cómo crecer sin volverte gerente |
| [Never Split the Difference](https://www.amazon.com/dp/0062407805) | Chris Voss | Negociación. Léelo antes de hablar de salario |
| [The Mom Test](https://www.amazon.com/dp/1492180742) | Rob Fitzpatrick | Cómo hablar con stakeholders sin que te mientan |

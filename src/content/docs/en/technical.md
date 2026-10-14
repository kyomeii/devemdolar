---
title: Technical
description: Master your stack. What a dev needs to know in the AI era, and the books worth reading.
---

Technical knowledge is way more subjective than English and depends on your professional background. Me, I'm a data analyst, a Power BI specialist. My stack includes Power BI itself, SQL, Python, data modeling, data warehousing (Snowflake and Databricks), etc. It's not exactly the stack with the most job openings out there, but as you saw earlier, I landed them anyway.

The most important thing is to be **good at what you do**, especially if you're aiming for OE (*overemployment*, holding more than one job at the same time). Some people say Power BI is easy, but that's because you have no idea how big a mess a guy who took a 20-hour course and thinks he's hot shit can make.

**Master your stack.**

## Typing code isn't worth shit anymore

These days, just knowing how to type code barely matters. Claude types more code in one hour than you would in 10 years. What AI doesn't have is **judgment**. You have to master the business rules, know how the systems integrate, deal with the stakeholders, understand the architecture, understand how the system itself is supposed to work. Then, sure, you delegate the tasks to the AI to code, write tests, etc.

The era of "Learn to code and become a Dev" bootcamps is over. Your studying needs to go deeper, and there are two ways to do that: **reading and building**. Obviously "reading" here can include videos, but you get the idea.

## What you need to master

The basics that never change:

- **Algorithms and data structures** — complexity, when to use a hash map, a tree, a queue. Not to memorize LeetCode, but to know why that query or that loop is slow.
- **Business rules** — understand *why* the system exists and who makes money from it.
- **Data modeling** — normalization, dimensional modeling, when to denormalize.
- **Deployment** — how your code gets from your machine to production.

And what separates the AI-era dev from a code typist:

- **System design** — how to build a system that handles load: caching, queues, load balancers, database replicas, consistency vs. availability. It's what shows up in senior interviews, and it's exactly what AI doesn't decide on its own.
- **Database internals** — indexes, transactions, locks, execution plans. The AI writes the query, you have to know why it takes 40 seconds.
- **API and integration design** — REST, events, webhooks, idempotency, versioning, contracts between systems.
- **Cloud** — at least one of the big ones (AWS, Azure, or GCP), at the level of knowing what each piece does and how much it costs.
- **Containers, CI/CD, and Infra as Code** — Docker, deploy pipelines, Terraform. Nobody pushes stuff to production by dragging files around anymore.
- **Observability** — logs, metrics, traces, and alerts. Knowing how to figure out *why* it broke at 3 a.m.
- **Security** — OWASP basics, secrets management, authentication and authorization. AI-generated code loves leaking API keys.
- **Testing** — knowing what's worth testing and how. AI writes tests in no time, but bad tests just give you a false sense of security.
- **Cost** — FinOps. Abroad, the question "how much does this cost per month?" comes up way more than it does here.
- **Reviewing AI code** — reading code you didn't write, finding the subtle bug, and knowing how to say "no, do it another way." This is the most underrated skill of 2026.
- **Working with LLMs** — context engineering, evals, RAG, agents. Even if you're not in AI, every product is shoving AI in somewhere.

## Build stuff

While you're studying the fundamentals, it's important to build things too. Nowadays it's easier than ever: just pay for a 100-reais Claude plan and you can build anything.

As you build, the most important thing is that you **understand the technical decisions the AI is making**. Remember, you're learning. Read the code, try to understand it, ASK. Pretend Claude is a kinda-autistic senior dev who's fucking amazing at code, and anything you're unsure about, you can ask. Ask it to explore some other solution you thought of, to implement a new feature, and keep evolving your little project.

## Personal projects

Always keep your mind open to personal project ideas. Some examples of projects I did recently:

1. Pulled public data from my city hall to try to spot fraudulent patterns. Found out the current administration hires WAY MORE contractors.
2. Pulled data from the Path of Exile 2 API to figure out which tablet mods to sell. GGG, bring the scarabs back, nobody can stand rerolling 500 expedition tablets!
3. Took the FIPE data (Brazil's official used-car price table) that another reddit user shared and built a dashboard to help decide on buying a car.
4. Olist's ERP has some shitty charts, so I set up a data extraction from it and built a sales and inventory dashboard for my wife's store.
5. This very site, which I'm going way overboard on. I wrote most of the text by hand, but I had Claude use Higgsfield and go all out on the design to make it look pretty.

AI has democratized development, so today there are endless possibilities for what you can build. Almost none of them will make money, but a lot of them can be interesting projects, and all of them become interview material. Let your creativity run wild!

## Books

Some essential books, depending on your stack. Other folks, feel free to add books to this list (just send a pull request). Oh, and remember: **English books only**.

### General computing (everyone should read these)

| Book | Author | Why |
|---|---|---|
| [The Pragmatic Programmer (20th Anniversary)](https://www.amazon.com/dp/0135957052) | David Thomas, Andrew Hunt | The manual on how to be a decent professional |
| [A Philosophy of Software Design](https://www.amazon.com/dp/173210221X) | John Ousterhout | Short and to the point: how to reduce complexity |
| [Code: The Hidden Language of Computer Hardware and Software](https://www.amazon.com/dp/0137909101) | Charles Petzold | Understand how a computer actually works |
| [Computer Systems: A Programmer's Perspective](https://www.amazon.com/dp/013409266X) | Randal Bryant, David O'Hallaron | The systems textbook for people who didn't study CS |
| [Software Engineering at Google](https://www.amazon.com/dp/1492082791) | Titus Winters et al. | How engineering works at scale |

### Algorithms and interviews

| Book | Author | Why |
|---|---|---|
| [Grokking Algorithms (2nd Edition)](https://www.amazon.com/dp/1633438538) | Aditya Bhargava | Algorithms with little drawings, for the traumatized |
| [Introduction to Algorithms (CLRS)](https://www.amazon.com/dp/026204630X) | Cormen, Leiserson, Rivest, Stein | The bible. Not meant to be read cover to cover, it's for reference |
| [Cracking the Coding Interview](https://www.amazon.com/dp/0984782850) | Gayle Laakmann McDowell | Still the standard for live coding interviews |
| [System Design Interview, Vol. 1](https://www.amazon.com/s?k=System+Design+Interview+Alex+Xu) | Alex Xu | System design interviews, spoon-fed |

### Backend and architecture

| Book | Author | Why |
|---|---|---|
| [Designing Data-Intensive Applications (2nd Edition)](https://www.amazon.com/dp/1098119061) | Martin Kleppmann, Chris Riccomini | The best technical book of the last decade. Period. The 2nd edition came out in 2026 |
| [Database Internals](https://www.amazon.com/dp/1492040347) | Alex Petrov | How databases work under the hood |
| [Clean Architecture](https://www.amazon.com/dp/0134494164) | Robert C. Martin | Read it with a critical eye, but read it |
| [Domain-Driven Design](https://www.amazon.com/dp/0321125215) | Eric Evans | How to translate business rules into code |
| [Refactoring (2nd Edition)](https://www.amazon.com/dp/0134757599) | Martin Fowler | How to touch legacy code without breaking everything |

### Data and analytics

| Book | Author | Why |
|---|---|---|
| [The Data Warehouse Toolkit](https://www.amazon.com/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802) | Ralph Kimball, Margy Ross | Dimensional modeling, the foundation of all BI |
| [Fundamentals of Data Engineering](https://www.amazon.com/dp/1098108302) | Joe Reis, Matt Housley | The complete map of data engineering |
| [Analytics Engineering with SQL and dbt](https://www.amazon.com/dp/1098142381) | Rui Machado, Hélder Russa | dbt and the transformation layer |
| [Spark: The Definitive Guide](https://www.amazon.com/dp/1491912219) | Bill Chambers, Matei Zaharia | If you work with Databricks, it's mandatory |
| [SQL Performance Explained](https://www.amazon.com/dp/3950307826) | Markus Winand | Indexes and execution plans, explained properly |
| [Practical Statistics for Data Scientists](https://www.amazon.com/dp/149207294X) | Peter Bruce, Andrew Bruce, Peter Gedeck | The statistics you actually use |

### Power BI

| Book | Author | Why |
|---|---|---|
| [The Definitive Guide to DAX](https://www.amazon.com/Definitive-Guide-DAX-Alberto-Ferrari/dp/0138244723) | Alberto Ferrari, Marco Russo | If you haven't read it, you don't know DAX. This link is for the 3rd edition |

### Machine learning and AI

| Book | Author | Why |
|---|---|---|
| [Hands-On Machine Learning (3rd Edition)](https://www.amazon.com/dp/1098125975) | Aurélien Géron | The best hands-on ML book |
| [Designing Machine Learning Systems](https://www.amazon.com/dp/1098107969) | Chip Huyen | ML in production, not in a notebook |
| [AI Engineering](https://www.amazon.com/dp/1098166302) | Chip Huyen | How to build products on top of LLMs |

### DevOps, SRE, and cloud

| Book | Author | Why |
|---|---|---|
| [Site Reliability Engineering](https://www.amazon.com/dp/149192912X) | Google | How Google keeps things up |
| [Accelerate](https://www.amazon.com/dp/1942788339) | Nicole Forsgren, Jez Humble, Gene Kim | What actually makes a team ship fast |
| [The DevOps Handbook (2nd Edition)](https://www.amazon.com/dp/1950508404) | Gene Kim et al. | The practical DevOps manual |
| [Terraform: Up & Running (3rd Edition)](https://www.amazon.com/dp/1098116747) | Yevgeniy Brikman | Infra as Code done right |

### Languages and frontend

| Book | Author | Why |
|---|---|---|
| [Fluent Python (2nd Edition)](https://www.amazon.com/dp/1492056359) | Luciano Ramalho | Written by a Brazilian, by the way |
| [Effective Java (3rd Edition)](https://www.amazon.com/dp/0134685997) | Joshua Bloch | Mandatory if you're a Java person |
| [Eloquent JavaScript (4th Edition)](https://www.amazon.com/dp/1718504101) | Marijn Haverbeke | JavaScript done right (and free online) |
| [Don't Make Me Think, Revisited](https://www.amazon.com/dp/0321965515) | Steve Krug | Usability, so you stop building shitty screens |

### Business and career

| Book | Author | Why |
|---|---|---|
| [Storytelling with Data](https://www.amazon.com/dp/1119002257) | Cole Nussbaumer Knaflic | How to show data to the people who make decisions |
| [The Staff Engineer's Path](https://www.amazon.com/dp/1098118731) | Tanya Reilly | How to grow without becoming a manager |
| [Never Split the Difference](https://www.amazon.com/dp/0062407805) | Chris Voss | Negotiation. Read it before you talk salary |
| [The Mom Test](https://www.amazon.com/dp/1492180742) | Rob Fitzpatrick | How to talk to stakeholders without getting lied to |

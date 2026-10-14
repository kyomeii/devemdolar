---
title: Técnica
description: Domine sua stack. O que um dev precisa saber na era da IA, e os livros que valem a pena.
---

Conhecimento técnico é muito mais subjetivo do que o inglês e vai depender da sua bagagem profissional. Eu mesmo sou analista de dados, especialista em Power BI. Minha stack envolve o próprio Power BI, SQL, Python, modelagem de dados, data warehousing (Snowflake e Databricks), etc. Não é exatamente a stack com mais fartura de vagas, mas como vocês viram anteriormente, eu as consegui mesmo assim.

O mais importante é você ser **bom naquilo que faz**, principalmente se você almeja fazer OE (*overemployment*, ter mais de um emprego ao mesmo tempo). Há quem diga que Power BI é fácil, mas é porque vocês não têm noção do tamanho da merda que faz um cara que fez um curso de 20 horas e se acha o pica.

**Domine a sua stack.**

## Digitar código não vale mais nada

Na era de hoje, só saber digitar código de pouco importa. O Claude digita mais código em uma hora do que você digitaria em 10 anos. O que a IA não tem é a **subjetividade**. Você tem que dominar as regras de negócio, saber como os sistemas se integram, interagir com os stakeholders, entender a arquitetura, compreender como o sistema em si deve funcionar. Aí sim, você delega as tasks pra IA codar, criar testes, etc.

A era dos cursinhos de "Aprenda a programar e vire Dev" acabou. O estudo precisa ser mais profundo, e pra isso tem dois jeitos: **leitura e implementação**. Obviamente leitura nesse caso podem ser vídeos, mas vocês entenderam.

## O que você precisa dominar

O básico que não muda nunca:

- **Algoritmos e estruturas de dados** — complexidade, quando usar hash map, árvore, fila. Não é pra decorar LeetCode, é pra saber por que aquela query ou aquele loop tá lento.
- **Regras de negócio** — entender *por que* o sistema existe e quem ganha dinheiro com ele.
- **Modelagem de dados** — normalização, modelagem dimensional, quando desnormalizar.
- **Deployment** — como seu código sai da sua máquina e chega em produção.

E o que separa o dev da era da IA do digitador de código:

- **System design** — como montar um sistema que aguenta carga: cache, filas, load balancer, réplica de banco, consistência vs. disponibilidade. É o que cai em entrevista de sênior e é exatamente o que a IA não decide sozinha.
- **Bancos de dados por dentro** — índices, transações, locks, plano de execução. A IA escreve a query, você tem que saber por que ela demora 40 segundos.
- **Design de APIs e integrações** — REST, eventos, webhooks, idempotência, versionamento, contrato entre sistemas.
- **Cloud** — pelo menos uma das grandes (AWS, Azure ou GCP) no nível de saber o que cada peça faz e quanto custa.
- **Containers, CI/CD e Infra as Code** — Docker, pipelines de deploy, Terraform. Ninguém mais sobe coisa em produção arrastando arquivo.
- **Observabilidade** — logs, métricas, traces e alertas. Saber descobrir *por que* quebrou às 3 da manhã.
- **Segurança** — o básico do OWASP, gestão de segredos, autenticação e autorização. Código gerado por IA adora vazar API key.
- **Testes** — saber o que vale testar e como. A IA escreve teste rapidinho, mas teste ruim só dá falsa sensação de segurança.
- **Custo** — FinOps. Na gringa, a pergunta "quanto isso custa por mês?" aparece muito mais do que aqui.
- **Revisar código de IA** — ler código que você não escreveu, achar o bug sutil, e saber dizer "não, faz de outro jeito". Essa é a skill mais subestimada de 2026.
- **Trabalhar com LLMs** — engenharia de contexto, avaliação (evals), RAG, agentes. Mesmo que você não seja de IA, todo produto tá enfiando IA em algum lugar.

## Implemente

Enquanto já vão estudando a base, é importante também implementar. Hoje em dia é mais fácil do que nunca, é só pagar um plano de 100 reais do Claude que você consegue implementar qualquer coisa.

Enquanto você vai implementando, o mais importante é você **compreender as decisões técnicas que a IA está tomando**. Lembre-se, você está aprendendo. Leia o código, tente compreender, PERGUNTE. Finge que o Claude é um profissional sênior meio autista mas que é foda pra caralho no código, e tudo que você tiver dúvida, você pode perguntar. Peça para explorar alguma outra solução que você pensou, pra implementar uma nova feature, vá evoluindo o seu projetinho.

## Projetos pessoais

Esteja sempre com a mente aberta a possibilidades de projetos pessoais. Alguns exemplos de projetos que eu fiz recentemente:

1. Extrair dados públicos da prefeitura da minha cidade pra tentar identificar tendências fraudulentas. Descobri que a prefeitura atual contrata MUITO MAIS terceirizado.
2. Extrair dados da API do Path of Exile 2 pra saber quais mods de tablet vender. GGG, traga os scarabs de volta, ninguém aguenta ficar dando reforge em 500 tablets de expedition!
3. Peguei os dados da FIPE que um outro usuário do reddit compartilhou pra montar um dashboard que ajude na decisão de comprar um carro.
4. O ERP da Olist tem uns gráficos meio bosta, então eu montei uma extração dos dados de lá, e fiz um dashboard de vendas e estoque para a loja da minha esposa.
5. Esse site aqui, que eu tô fazendo um monte de firula. Escrevi a maior parte do texto na mão, mas mandei o Claude usar o Higgsfield e caprichar no design pra deixar bonitinho.

A IA tem democratizado o desenvolvimento, então hoje tem possibilidades infinitas do que se pode fazer. Quase nenhuma vai ser rentável, mas muitas podem ser projetos interessantes, e todas viram assunto pra entrevista. Deixe sua criatividade rolar!

## Livros

Alguns livros indispensáveis, dependendo da stack. Outros usuários, sintam-se à vontade para adicionar livros a essa lista (só manda um pull request). Ah, lembrem-se: **só livros em inglês**.

### Computação em geral (todo mundo deveria ler)

| Livro | Autor | Por quê |
|---|---|---|
| [The Pragmatic Programmer (20th Anniversary)](https://www.amazon.com.br/dp/0135957052) | David Thomas, Andrew Hunt | O manual de como ser um profissional decente |
| [A Philosophy of Software Design](https://www.amazon.com.br/dp/173210221X) | John Ousterhout | Curto e direto: como reduzir complexidade |
| [Code: The Hidden Language of Computer Hardware and Software](https://www.amazon.com.br/dp/0137909101) | Charles Petzold | Entenda como um computador funciona de verdade |
| [Computer Systems: A Programmer's Perspective](https://www.amazon.com.br/dp/013409266X) | Randal Bryant, David O'Hallaron | O livro-texto de sistemas pra quem não fez computação |
| [Software Engineering at Google](https://www.amazon.com.br/dp/1492082791) | Titus Winters et al. | Como engenharia funciona em escala |

### Algoritmos e entrevistas

| Livro | Autor | Por quê |
|---|---|---|
| [Grokking Algorithms (2nd Edition)](https://www.amazon.com.br/dp/1633438538) | Aditya Bhargava | Algoritmos com desenhinho, pra quem tem trauma |
| [Introduction to Algorithms (CLRS)](https://www.amazon.com.br/dp/026204630X) | Cormen, Leiserson, Rivest, Stein | A bíblia. Não é pra ler inteiro, é pra consultar |
| [Cracking the Coding Interview](https://www.amazon.com.br/dp/0984782850) | Gayle Laakmann McDowell | Ainda é o padrão pra entrevista de live coding |
| [System Design Interview, Vol. 1](https://www.amazon.com.br/s?k=System+Design+Interview+Alex+Xu) | Alex Xu | Entrevista de system design mastigada |

### Backend e arquitetura

| Livro | Autor | Por quê |
|---|---|---|
| [Designing Data-Intensive Applications (2nd Edition)](https://www.amazon.com.br/dp/1098119061) | Martin Kleppmann, Chris Riccomini | O melhor livro técnico da última década. Ponto. A 2ª edição saiu em 2026 |
| [Database Internals](https://www.amazon.com.br/dp/1492040347) | Alex Petrov | Como banco de dados funciona por dentro |
| [Clean Architecture](https://www.amazon.com.br/dp/0134494164) | Robert C. Martin | Leia com senso crítico, mas leia |
| [Domain-Driven Design](https://www.amazon.com.br/dp/0321125215) | Eric Evans | Como traduzir regra de negócio em código |
| [Refactoring (2nd Edition)](https://www.amazon.com.br/dp/0134757599) | Martin Fowler | Como mexer em código legado sem quebrar tudo |

### Dados e analytics

| Livro | Autor | Por quê |
|---|---|---|
| [The Data Warehouse Toolkit](https://www.amazon.com.br/Data-Warehouse-Toolkit-Definitive-Dimensional/dp/1118530802) | Ralph Kimball, Margy Ross | Modelagem dimensional, a base de todo BI |
| [Fundamentals of Data Engineering](https://www.amazon.com.br/dp/1098108302) | Joe Reis, Matt Housley | O mapa completo da engenharia de dados |
| [Analytics Engineering with SQL and dbt](https://www.amazon.com.br/dp/1098142381) | Rui Machado, Hélder Russa | dbt e a camada de transformação |
| [Spark: The Definitive Guide](https://www.amazon.com.br/dp/1491912219) | Bill Chambers, Matei Zaharia | Se você mexe com Databricks, é obrigatório |
| [SQL Performance Explained](https://www.amazon.com.br/dp/3950307826) | Markus Winand | Índice e plano de execução, explicados direito |
| [Practical Statistics for Data Scientists](https://www.amazon.com.br/dp/149207294X) | Peter Bruce, Andrew Bruce, Peter Gedeck | A estatística que você realmente usa |

### Power BI

| Livro | Autor | Por quê |
|---|---|---|
| [The Definitive Guide to DAX](https://www.amazon.com.br/Definitive-Guide-DAX-Alberto-Ferrari/dp/0138244723) | Alberto Ferrari, Marco Russo | Se você não leu, você não sabe DAX. Esse link é da 3ª edição |

### Machine learning e IA

| Livro | Autor | Por quê |
|---|---|---|
| [Hands-On Machine Learning (3rd Edition)](https://www.amazon.com.br/dp/1098125975) | Aurélien Géron | O melhor livro prático de ML |
| [Designing Machine Learning Systems](https://www.amazon.com.br/dp/1098107969) | Chip Huyen | ML em produção, não em notebook |
| [AI Engineering](https://www.amazon.com.br/dp/1098166302) | Chip Huyen | Como construir produto em cima de LLM |

### DevOps, SRE e cloud

| Livro | Autor | Por quê |
|---|---|---|
| [Site Reliability Engineering](https://www.amazon.com.br/dp/149192912X) | Google | Como o Google mantém as coisas no ar |
| [Accelerate](https://www.amazon.com.br/dp/1942788339) | Nicole Forsgren, Jez Humble, Gene Kim | O que realmente faz um time entregar rápido |
| [The DevOps Handbook (2nd Edition)](https://www.amazon.com.br/dp/1950508404) | Gene Kim et al. | O manual prático de DevOps |
| [Terraform: Up & Running (3rd Edition)](https://www.amazon.com.br/dp/1098116747) | Yevgeniy Brikman | Infra as Code do jeito certo |

### Linguagens e frontend

| Livro | Autor | Por quê |
|---|---|---|
| [Fluent Python (2nd Edition)](https://www.amazon.com.br/dp/1492056359) | Luciano Ramalho | Escrito por um brasileiro, inclusive |
| [Effective Java (3rd Edition)](https://www.amazon.com.br/dp/0134685997) | Joshua Bloch | Obrigatório pra quem é de Java |
| [Eloquent JavaScript (4th Edition)](https://www.amazon.com.br/dp/1718504101) | Marijn Haverbeke | JavaScript direito (e de graça online) |
| [Don't Make Me Think, Revisited](https://www.amazon.com.br/dp/0321965515) | Steve Krug | Usabilidade, pra parar de fazer tela ruim |

### Negócios e carreira

| Livro | Autor | Por quê |
|---|---|---|
| [Storytelling with Data](https://www.amazon.com.br/dp/1119002257) | Cole Nussbaumer Knaflic | Como mostrar dado pra quem decide |
| [The Staff Engineer's Path](https://www.amazon.com.br/dp/1098118731) | Tanya Reilly | Como crescer sem virar gerente |
| [Never Split the Difference](https://www.amazon.com.br/dp/0062407805) | Chris Voss | Negociação. Lê antes de falar de salário |
| [The Mom Test](https://www.amazon.com.br/dp/1492180742) | Rob Fitzpatrick | Como conversar com stakeholder sem ouvir mentira |

---
title: Procurar vagas
description: "Pesquisa booleana, LinkedIn Posts, Google com site: e HiringCafe. Onde estão as vagas boas."
---

Pra flertar com moças (ou rapazes), você nunca deve se autorrejeitar, e sim deixar o terceiro decidir se te rejeita ou não. O mesmo serve pra vagas.

> "O não eu já tenho, vou em busca da humilhação."

Aqui é onde começa a verdadeira batalha. Você provavelmente vai se candidatar a dezenas de vagas até ser chamado pra uma entrevista, e tá tudo bem. Você é só mais um no mar de um monte de gente, mas mais cedo ou mais tarde vai ser fisgado também. Eu pessoalmente só procuro de três maneiras: **LinkedIn, Google e HiringCafe**.

## Pesquisa booleana

Tanto pro LinkedIn quanto pro Google, você vai usar **pesquisa booleana** (*boolean search*). É só montar a pesquisa usando operadores lógicos pra dizer exatamente o que você quer e o que não quer:

| Operador | O que faz | Exemplo |
|---|---|---|
| `"aspas"` | Busca a expressão exata | `"Power BI"` (e não "power" e "BI" soltos) |
| `OR` | Qualquer um dos termos | `"Power BI" OR Tableau` |
| `AND` | Todos os termos precisam aparecer | `"Power BI" AND remote` |
| `NOT` (LinkedIn) ou `-` (Google) | Exclui o termo | `NOT India` / `-India` |
| `( )` | Agrupa as coisas, igual matemática | `("Power BI" OR Tableau) AND remote` |

Regras que todo mundo erra:

- No LinkedIn, `AND`, `OR` e `NOT` têm que ser em **MAIÚSCULA**. Em minúscula ele ignora.
- No Google, `AND` não existe (todos os termos já são obrigatórios por padrão), e pra excluir é o sinal de menos colado na palavra: `-India`.
- No LinkedIn, sempre use parênteses quando misturar `OR` com `AND`, senão o resultado vira bagunça.
- O Google ignora parênteses, mas não tem problema: lá o `OR` já "gruda" nos termos vizinhos, então `"Power BI" OR Tableau remote` funciona como `("Power BI" OR Tableau) remote`.

A estrutura que funciona é: **(seus cargos/stack) AND (remoto) AND (onde você pode trabalhar) NOT (o que você não quer)**. Exemplo pra minha stack:

```
("Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer") AND (remote OR "work from anywhere") AND (LATAM OR "Latin America" OR Brazil OR "South America") NOT (hybrid OR onsite OR "on-site")
```

Troca os termos do primeiro parêntese pela sua stack e pronto. Vale salvar umas 3 ou 4 variações (uma mais ampla, uma só com o seu cargo exato, uma com "contractor" no lugar de "remote") e ir alternando.

## LinkedIn

Agora que você já manja, é só copiar e colar sua pesquisa booleana na barra de pesquisa do LinkedIn. Aí você vai e clica em *Vagas*, correto?

**ERRADO!**

Na aba de vagas a maioria é vaga fantasma, tu vai se aplicar em uma porrada de vaga pra nunca ser chamado, só uma ou outra são legítimas. Só vale a pena se aplicar por lá se for aqueles *Easy Apply* que você nem perde tempo. Hoje em dia deve ter alguma forma de usar IA pra fazer isso em massa, mas nunca procurei.

Você vai pesquisar em **Posts** apenas. Sempre que um recrutador posta uma vaga legítima, ele também vai compartilhar, então é um jeito de filtrar. Ordene por **mais recentes**.

Nos posts também vai ter muito lixo, principalmente porque tem muito indiano postando vaga de scam ou só vagas pra Índia mesmo. Você vai clicar em posts, ler o nome da pessoa que fez a postagem, se for indiano já pode ignorar, e assim vai. É entediante? Muito, mas é onde estão as melhores vagas. Procure por nomes claramente anglo-saxões, latinos, ou talvez até do leste europeu. Aí sim você lê o texto.

Hoje em dia esses também têm uma boa chance de ser scam. Sinais de que é golpe:

- Texto extremamente genérico ("We are hiring! Multiple positions! DM me!").
- Contato por e-mail `@gmail.com`, `@zohomail.com`, `@outlook.com`, ou pior, Telegram/WhatsApp.
- Salário bom demais pra pouca exigência.
- Empresa que não tem site, ou cujo site foi criado mês passado.
- Pedem pra você pagar alguma coisa (treinamento, equipamento, "taxa de processamento"). Vaga legítima **nunca** te cobra.

Vagas legítimas vão apontar ou pro próprio LinkedIn, ou pra plataforma de recrutamento da empresa, o que nos leva para a próxima opção de procura:

## Google

Aqui você vai manter a pesquisa booleana do LinkedIn (adaptada pro Google: sem `AND`, sem parênteses e com `-` no lugar de `NOT`), só que no começo da pesquisa você vai colocar as plataformas de recrutamento (ATS) mais comuns. Sua pesquisa vai ser:

```
site:greenhouse.io "Power BI" OR "Analytics Engineer" OR "BI Developer" OR "BI Engineer" remote OR "work from anywhere" LATAM OR "Latin America" OR Brazil OR "South America" -hybrid -onsite
```

Aí você troca o `site:` pelas outras plataformas:

| Plataforma | O que colocar no `site:` |
|---|---|
| Greenhouse | `site:greenhouse.io` (pega `boards.` e `job-boards.`) |
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

Filtre no Google pela **última semana** (ou últimas 24 horas): *Ferramentas → Qualquer horário → Na última semana*.

E vai clicando nos sites e vendo as vagas. Quando terminar todas as que apareceram, vai pro próximo site.

Esse processo no LinkedIn e no Google você vai fazer **todo dia**. No LinkedIn, duas vezes por dia, de manhã e de noite. Não desista! Se você vir uma vaga fresca, a chance de ser chamado é muito maior do que numa vaga que foi postada uns dias atrás.

## HiringCafe

[HiringCafe](https://hiringcafe.com) é uma plataforma feita por um usuário no reddit, e é de longe a melhor plataforma de vagas que eu já vi. Eles agregam diretamente dos sites que você pesquisou no Google, mas pode ser que uma ou outra coisa não apareça lá.

Lá você vai deixar sua pesquisa salva e olhar todo dia. Quando vir uma vaga que se encaixa no seu perfil, você não vai só se inscrever: vai no LinkedIn, pesquisar funcionários da empresa e adicioná-los. **Principalmente os recrutadores.**

## Empresas que contratam brasileiros

Futuramente vou adicionar nesse site empresas que contratam brasileiros ou latinos remotamente, sejam elas consultorias, agências de recrutamento ou a própria empresa. Só tenho que fazer um scrape nos meus e-mails pra achar a lista extensiva.

Enquanto isso, tem uma página de [empresas e plataformas](/pt/companies/) que a comunidade vai preenchendo. Se você trabalha ou trabalhou numa empresa que contrata brasileiro remoto, manda um pull request.

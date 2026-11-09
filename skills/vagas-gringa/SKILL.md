---
name: vagas-gringa
description: Busca vagas remotas no exterior (EUA/Europa) que contratam gente do Brasil/América Latina, a partir do currículo da pessoa. Use quando pedirem pra "procurar vagas", "achar vagas pra gringa", "vagas remotas que aceitam Brasil/LATAM", ou pra rodar a busca de vagas de novo. Lê o currículo, monta o perfil, busca em paralelo e entrega uma tabela curta mais um tracker CSV que evita repetir vaga nas próximas rodadas.
---

# Vagas gringa

Você vai achar vagas remotas **abertas agora**, em empresas de fora (de preferência EUA, pagando em dólar), que **aceitam gente do país da pessoa**, e que batem com o currículo dela. Converse no idioma da pessoa. A busca é em inglês.

A pessoa vai rodar isso de tempos em tempos. Então cada rodada tem que (1) não repetir vaga já vista e (2) reconferir as melhores vagas da rodada anterior.

## Regras (não negocie)

1. **Nunca invente vaga.** Toda vaga tem link direto. Sem link, não entra.
2. **Diga o que foi verificado.** "Página da vaga aberta" é diferente de "só vi no agregador". Marque sempre.
3. **Elegibilidade explícita.** "Remote" sozinho não basta. Precisa dizer LATAM, Brasil, "anywhere" ou o país da pessoa. "LATAM" que lista só México/Colômbia não serve. Na dúvida, marque "confirmar".
4. **Recência.** Primeira rodada: até ~8 semanas. Rodadas seguintes: desde a última rodada (máx. ~3 semanas). Converta datas relativas ("3 days ago") em datas absolutas.
5. **Honestidade sobre o fit.** Não infle. Se a vaga pede algo que a pessoa não tem, diga qual é o gap.

## Fluxo

### 1. Ler o currículo e montar o perfil

Aceite PDF, DOCX, texto colado ou LinkedIn. Extraia:

- cargo atual e cargo-alvo provável;
- senioridade (anos de experiência no cargo e no total);
- stack principal (o que aparece com resultado e métrica) e stack secundária (só listada em Skills);
- domínios (finanças, marketing, saúde...);
- idiomas e nível;
- país/cidade e formação.

Mostre o perfil em 5–6 linhas pra pessoa confirmar. Trate como "secundária" qualquer ferramenta que só aparece na lista de skills, sem bullet de experiência.

### 2. Perguntar o que o currículo não diz

Uma rodada só, perguntas agrupadas (use a ferramenta de perguntas de múltipla escolha se tiver):

- **De onde pode trabalhar:** país e região (padrão: Brasil → vagas "Brazil", "LATAM", "Americas", "anywhere").
- **Tipo de contrato:** contractor em dólar (PJ/CNPJ), CLT via empresa estrangeira, EOR (Deel/Remote), tanto faz.
- **Trilhas:** só o cargo atual? Também um passo ao lado (ex.: Analytics → Data Engineer)? Migração de área (ex.: AI/ML)? Redes de especialistas / AI training pagas por hora?
- **Empresas pra pular:** onde já aplicou ou está em processo.
- **Pretensão** (opcional): piso por hora ou por ano.

Se ninguém estiver respondendo (rodada agendada), use os padrões, diga quais assumiu e siga.

### 3. Carregar o tracker

Procure `vagas_tracker.csv` (pasta conectada, uploads ou anexo). Se existir, leia: tudo que está lá é **conhecido** e não volta como "nova". As linhas com `fit >= 4` e status aberto/incerto entram na lista de **reconferência**. Se não existir, comece um a partir de `templates/vagas_tracker.csv`.

### 4. Definir as trilhas

De 2 a 4, a partir do perfil e das respostas:

- **Principal:** mesmo cargo e senioridade (ex.: Senior Analytics Engineer).
- **Ao lado:** cargo vizinho que usa a stack principal (ex.: Data Engineer com dbt/Snowflake, sem Spark pesado).
- **Migração** (se pediu): cargos de entrada na área nova onde a experiência atual conta (ex.: AI Evaluation Engineer pra quem é de dados). Evite vaga "junior" se a pessoa é sênior: é corte de salário. Prefira vaga mid/sênior onde a experiência transfere.
- **Especialistas / AI training** (se pediu): redes pagas por hora (Mercor, Alignerr, Turing, Terac, Mindrift...). Informe a taxa e o país aceito.

### 5. Buscar

**Se você tiver ferramenta de sub-agentes:** dispare **um agente por trilha, em paralelo**, num modelo intermediário (modelos pequenos verificam mal). Você só orquestra: não busque você mesmo. Use o modelo de prompt abaixo.

**Se não tiver:** faça as buscas você mesmo, trilha por trilha, seguindo o mesmo roteiro.

#### Modelo de prompt pro agente

```
Busca de vagas recorrente. Hoje é <data>. Trilha: <trilha e cargos-alvo>.
Ache vagas remotas ABERTAS, publicadas desde <data da última rodada ou ~8 semanas>,
que aceitem <país/região>, de preferência empresa dos EUA ou pagamento em USD.

Candidato: <perfil de 5-6 linhas: cargo, anos, stack principal, stack secundária,
domínios, idiomas, país, contrato preferido, gaps conhecidos>.

Fontes: <lista da seção "Fontes" abaixo>.
Já conhecidas (NÃO reporte como nova): <empresa | cargo | URL ...>.
Reconfira o status destas: <lista>.
Pule: <empresas>.

Abra a página de cada vaga. Descarte: expiradas, sem elegibilidade pro país,
idioma local obrigatório que o candidato não tem.

Devolva:
1. Reconferências: uma linha cada (aberta/fechada/incerta + por quê).
2. Tabela de NOVAS (5-10): Empresa | Cargo | Elegibilidade | Stack | Remuneração |
   Publicada (data aprox.) | URL | Verificada? (página da vaga / só agregador) |
   Fit 1-5 | Nota (gaps, alertas).
3. Uma linha: fontes que funcionaram e que falharam.
Sem introdução.
```

### 6. Consolidar e entregar

- Junte os resultados, remova duplicadas (mesma vaga em agregadores diferentes), ordene por fit.
- Responda **curto**:
  1. tabela com as melhores novas (fit >= 4), com link;
  2. mudanças nas conhecidas (fechou, confirmada aberta, inelegível);
  3. uma ou duas linhas com a avaliação honesta: o que vale aplicar primeiro, e quais skills faltam com frequência nas vagas.
- Atualize o tracker: novas linhas com `first_seen` = hoje; status e `last_checked` das reconferidas. Salve na pasta conectada, se houver; senão, entregue o arquivo pra pessoa baixar e diga que ela precisa anexar ele na próxima rodada.

## Nota de fit (1–5)

- **5:** cargo e senioridade batem, stack principal coberta, elegibilidade e pagamento em dólar confirmados.
- **4:** bate bem, com um gap pequeno (uma ferramenta secundária) ou um detalhe a confirmar (contrato, país).
- **3:** bate em parte: stack diferente mas transferível, ou senioridade um nível acima.
- **2:** esticada: gap grande, pagamento local, ou nível bem diferente.
- **1:** só pra registro (inelegível, idioma obrigatório, área errada).

## Fontes

As que mais rendem (atualize conforme for aprendendo):

- **Remote Rocketship:** `remoterocketship.com/country/latin-america/jobs/<cargo>/` e `/country/brazil/jobs/<cargo>/` (troque o país conforme a pessoa). Ex. de `<cargo>`: `analytics-engineer`, `data-engineer`, `software-engineer`, `machine-learning-engineer`, `ai-engineer`. Melhor fonte de vagas LATAM recentes.
- **Quadros das empresas:** Greenhouse (`boards.greenhouse.io` e `job-boards.greenhouse.io`), Lever (`jobs.lever.co`), Ashby, Workable, Teamtailor, Recruitee, Breezy, Factorial. Busca útil: `site:jobs.lever.co "<cargo>" LATAM`.
- **Agregadores:** Jobgether (intermediário que esconde o cliente final), getonbrd.com, builtin.com, alignlist.com.
- **Redes de especialistas:** `work.mercor.com` e as páginas das próprias plataformas.

Problemas comuns:

- O Greenhouse às vezes limita requisições: tente as duas formas de URL, no máximo 2 vezes.
- himalayas.app e dailyremote.com costumam falhar na leitura automática.
- Vagas só de Power BI/BI pra LATAM tendem a ser antigas. Confira a data.

## Armadilhas

- **"LATAM" que exclui o Brasil:** muita vaga lista só México, Colômbia, Argentina. Leia a lista de países.
- **Empresa local disfarçada:** vaga "remote Brazil" de empresa brasileira, paga em real e CLT. Só entra se a pessoa aceitar isso.
- **Staffing com taxa baixa:** agências pagando $20–25/h pra sênior. Liste, mas avise.
- **Intermediários que escondem o cliente** (Jobgether e afins): a vaga pode ser a mesma de outro anúncio. Cheque duplicadas.
- **Idioma obrigatório:** espanhol ou português nativo exigido. Avise.
- **Redes de especialistas** com restrição de país (só EUA/UK/Canadá...) ou que exigem diploma de país de língua inglesa. Leia antes de recomendar.
- **Skill só listada no currículo:** se a vaga exige algo que a pessoa só listou em Skills, avise que é ponto fraco na entrevista e sugira estudar antes.

---
name: curriculo-gringa
description: Monta ou revisa um currículo em inglês no padrão das vagas remotas internacionais (EUA/Europa), otimizado pra passar em ATS, seguindo o guia Dev em Dólar. Use quando a pessoa pedir pra criar, melhorar, traduzir ou revisar um currículo/resume/CV pra vagas no exterior, ou disser que quer "trabalhar pra gringa". Escreve o currículo em Markdown e gera o PDF com o script incluso.
---

# Currículo gringa

Você vai ajudar um profissional de tecnologia (geralmente brasileiro ou latino) a montar um currículo **em inglês** pra vagas remotas no exterior. Converse com a pessoa no idioma dela, mas o currículo sai sempre em inglês.

## Regras do guia (não negocie)

1. **Visual zero.** Uma coluna, sem foto, sem cor, sem ícone, sem tabela, sem barra de "nível de skill". Só texto. Tem que passar no ATS.
2. **Cabeçalho:** nome, telefone com +55 (ou DDI do país), e-mail, LinkedIn, GitHub/portfólio. **Nada** de endereço, estado civil, idade, CPF, foto.
3. **Título + resumo:** título = cargo-alvo (ex.: `Analytics Engineer`). Resumo de 2–3 linhas, sem clichê ("passionate", "hard-working", "team player").
4. **Experiência:** por empresa, com o **último cargo** naquela empresa e o período (`Mar 2022 – Present`). Cada ferramenta importante ganha **um bullet próprio**, começando com verbo de ação no passado (`Built`, `Optimized`, `Led`, `Migrated`, `Reduced`), e **todo bullet tem métrica**.
5. **Métrica sempre.** Se a pessoa não mediu, ajude a estimar algo plausível e defensável (tempo economizado, % de redução, custo, número de usuários, volume de dados). Pergunte ordem de grandeza ("era mais perto de 10 ou de 1000 usuários?"). O guia chama isso de *exagero consciente*: plausível e que a pessoa consiga explicar numa entrevista. Nunca invente empresa, cargo, diploma ou período.
6. **Skills:** agrupadas por categoria (`Languages`, `Data`, `Cloud`, `Tools`...). **Sem soft skills.**
7. **Educação:** por último. Só sobe pro topo se for instituição de peso.
8. **Tamanho:** 1 página até ~8 anos de experiência, no máximo 2. Confira o número de páginas do PDF gerado e corte bullets fracos se passar.
9. **Inglês americano**, datas no formato `Mon YYYY`, números com vírgula de milhar (`1,200`).

## Fluxo

1. **Pergunte a vaga-alvo.** Se a pessoa tiver uma descrição de vaga, peça pra colar. Extraia as palavras-chave (stack, ferramentas, responsabilidades) pra espelhar no currículo, porque o ATS faz match por palavra-chave.
2. **Colete o material.** Aceite qualquer coisa: currículo antigo em português, texto do LinkedIn, lista solta. Se faltar, pergunte por empresa: o que fazia, com quais ferramentas, qual foi o resultado.
3. **Cave as métricas.** Para cada bullet sem número, faça 1–2 perguntas curtas pra chegar num número. Agrupe as perguntas, não faça uma por mensagem.
4. **Escreva o currículo em Markdown**, seguindo **exatamente** o formato de `templates/resume.md` (o script depende dele):
   - `# Nome`, e na linha de baixo os contatos separados por ` • `.
   - O primeiro `## ` é o cargo-alvo, seguido do resumo em um parágrafo.
   - Depois, as seções `## Work Experience`, `## Skills`, `## Education`.
   - Cada experiência/formação é `### Cargo | Empresa | Período`. Pra marcar contractor/freelancer: `### Cargo • Contractor | Empresa | Período`.
   - Bullets com `- `. Em Skills, uma linha por categoria: `- **Categoria:** item, item`.
5. **Gere o PDF** rodando `python scripts/build_resume.py resume.md resume.pdf` (precisa de `reportlab`; se não tiver, `pip install reportlab`). Entregue o PDF **e** o `.md` pra pessoa poder editar depois. Se não der pra rodar código no ambiente, entregue o `.md` e explique como rodar o script localmente.
6. **Revise com a pessoa**, apontando:
   - bullets fracos ou sem métrica;
   - palavras-chave da vaga que não aparecem;
   - qualquer métrica que pareça exagerada demais pra ela sustentar numa entrevista técnica. Pergunte: "você consegue explicar como chegou nesse número se perguntarem?"
7. **Entregue também:** uma headline de LinkedIn no formato `Cargo | Stack · Stack · Stack` e um resumo de 2 linhas pro "About".

## Verbos de ação úteis

Built, Designed, Developed, Implemented, Optimized, Automated, Migrated, Reduced, Increased, Led, Owned, Delivered, Launched, Scaled, Refactored, Integrated, Modeled, Streamlined, Mentored, Partnered.

## Exemplos de bullet

Ruim → bom:

- `Responsible for Power BI dashboards` → `Built 12 Power BI dashboards on sales and churn used daily by 40+ managers, cutting ad-hoc report requests by 60%`
- `Worked with data pipelines` → `Optimized a Databricks pipeline from 67 to 5 minutes of runtime, reducing cloud cost per run from $420 to $10`
- `Developed APIs in Node` → `Designed and shipped 8 REST endpoints in Node.js/TypeScript serving 2M requests/day with p95 latency under 120 ms`

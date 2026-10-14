---
title: Currículo
description: Como montar um currículo que passa no ATS e vende seu peixe. E como mentir com consciência.
---

Agora você já é um profissional que domina sua stack e fala inglês. Hora de começar a se vender. Eu entendo "se vender" como os próximos 4 tópicos, que são:

1. **Montar seu currículo:** vai abrir as portas dos processos seletivos. Tem que exaltar suas forças e passar pelo ATS, só isso.
2. **LinkedIn:** é outra porta pra processos seletivos. O mais importante é configurar seu perfil e criar conexões. Participar ativamente da rede social é secundário, mas ainda tem sua relevância.
3. **Procurar vagas:** procurar vagas é saber se vender sim, é igual vendedor de porta em porta, só que é você quem preenche os mesmos dados 3000 vezes.
4. **Entrevista:** será o ápice de tudo que fizemos até aqui, então esteja preparado.

Aqui vamos focar só no currículo.

## Visual: não tem

Esqueça todos aqueles currículos com cores, foto, elementos visuais, etc. Currículo pra área tech é **só conteúdo**, e tem que passar no ATS (*Applicant Tracking System*, o robô que lê seu currículo antes de qualquer humano).

Eu usava o resumake.io, que era só uma interface que compilava o currículo em LaTeX com uns visuais pré-definidos. Hoje eu recomendo escrever em **Markdown** e gerar o PDF a partir dele. Pro ATS tanto faz se veio de LaTeX, Markdown ou Word: o que importa é o PDF final ter **texto de verdade** (dá pra selecionar e copiar), **uma coluna só** e fonte padrão. Markdown só é muito mais fácil de editar, e a Skill lá embaixo já gera o PDF pra você.

O resultado fica assim (tudo inventado, óbvio, a Joana não existe):

![Exemplo completo de currículo no padrão gringo](../../../assets/resume/cv-full.png)

Agora vamos por partes.

## Estrutura

### Cabeçalho

Nome, número de telefone (com +55), e-mail e portfólio/GitHub se você tiver. Mais nada. Sem endereço, sem estado civil, sem foto, sem data de nascimento, nada.

![Exemplo de cabeçalho: nome, telefone, e-mail, LinkedIn e GitHub](../../../assets/resume/cv-header.png)

### Título e resumo

O título é o seu cargo. No caso do meu atual, eu uso *Analytics Engineer*. Depois, um breve resumo profissional do que você faz, em poucas linhas, já enfiando as palavras-chave da sua stack.

![Exemplo de título e resumo](../../../assets/resume/cv-summary.png)

### Experiência

Separado por empresas, sempre com o seu **último título** dentro daquela empresa. Coloque o período que ficou também.

![Exemplo de uma experiência: cargo, empresa, período e bullets com métrica](../../../assets/resume/cv-experience.png)

Cada ferramenta que você quer ressaltar deve ter um bullet point próprio, e se possível uma **métrica** atrelada a esse bullet point. **MESMO QUE VOCÊ NÃO TENHA MEDIDO, TIRA DA BUNDA, MAS COLOCA UMA MÉTRICA.**

Por exemplo:

> Built a Power BI report on customer churn that helped the board make decisions that reduced churn by 12%.

"Ah, mas a diretoria só queria olhar o número." Aí é problema deles. No seu currículo eles foram competentes, agiram e melhoraram o número, sim.

Outro exemplo:

> Optimized a data pipeline from 67 minutes to 5 minutes of runtime, cutting cloud processing costs from $420 to $10 per run.

Esse segundo é bem mais fácil de medir, mas vale a pena dar uma exagerada também, só que uma **exagerada consciente**.

### Skills

Após as experiências, coloque suas skills separadas em tópicos (linguagens, ferramentas, cloud, etc.). Nada de soft skills, tipo liderança, proatividade, etc. Essas baboseiras só quem gosta é gestor brasileiro. Idiomas podem entrar aqui também.

![Exemplo da seção de skills, separada por categoria](../../../assets/resume/cv-skills.png)

### Educação

Por último, sua educação. Dependendo do peso da sua educação, pode colocar antes. Se eu tivesse me formado no MIT, essa informação vinha logo depois do resumo.

![Exemplo da seção de educação](../../../assets/resume/cv-education.png)

## Como criar o currículo

Deixei no repositório uma **Skill do Claude** pra ajudar vocês nisso ([pasta `skills/curriculo-gringa`](https://github.com/kyomeii/devemdolar/tree/main/skills/curriculo-gringa)). Ela segue tudo que está nessa página: faz as perguntas certas, transforma suas experiências em bullet points com métrica, escreve o currículo em Markdown e cospe o PDF pronto, igualzinho ao exemplo aí de cima. O próprio Claude ajuda vocês direitinho a configurar.

## Sobre mentir no currículo

Mintam, mas **mintam com consciência**. "Eu sei fazer? Não, mas eu aprendo." E o recrutador não precisa saber que você não sabe. Óbvio que você precisa ter uma base pra não falar merda, passar pelo recrutador do RH, e ter tempo o suficiente pra se aprofundar pra passar na entrevista técnica também.

Eu já fiz algum projeto profissional com dbt? Ainda não, mas fiz alguns pessoais, e já sei bastante. No meu currículo tem uma *fanfic* de que eu peguei e otimizei a camada de transformação usando dbt. Hoje eu domino a ferramenta, e sei o suficiente sobre essa camada de transformação específica pra conseguir entender como a ferramenta encaixaria no processo. Isso é mentir com consciência.

Conte não só a sua história, mas a estória daquilo que você quer se tornar.

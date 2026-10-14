---
title: Como contribuir
description: O site é open source. Corrija, acrescente, traduza ou mande seu relato.
---

Esse site é **open source**: todo o conteúdo fica num repositório público no GitHub, e qualquer um pode sugerir mudança. Achou algo errado, desatualizado, ou tem uma dica melhor? Contribua.

## Jeito fácil (sem saber Git)

### Sugerir uma correção ou acréscimo numa página

1. Crie uma conta no [GitHub](https://github.com) (é de graça).
2. No fim de qualquer página desse site, clique em **"Editar página"**.
3. O GitHub vai abrir o arquivo do texto. Clique no lápis, faça sua alteração.
4. Clique em **"Commit changes…"** e depois em **"Propose changes"**, escreva rapidinho o que você mudou e por quê.
5. Pronto, isso cria um *pull request*. Alguém revisa e, se estiver de boa, entra no site.

### Mandar um relato ou sugerir uma empresa

No repositório do GitHub (ícone lá em cima, no canto), vá em **Issues → New issue** e escolha o formulário:

- **Novo relato** — conte sua história de como conseguiu trabalhar pra fora.
- **Sugerir empresa** — uma empresa, consultoria ou agência que contrata brasileiros.
- **Correção** — algo errado ou desatualizado que você não quer editar você mesmo.

## Jeito raiz (sabe Git)

```bash
git clone <url-do-repositório>
cd gringa
npm install
npm run dev
```

O site roda em `http://localhost:4321`. Os textos ficam em `src/content/docs/<idioma>/`. Faça um fork, crie uma branch, e mande o pull request.

## Traduções

O site existe em **português, espanhol e inglês**. O português é a versão original. Se você mudou algo em português e sabe espanhol ou inglês, atualize as outras versões também (ou avise no pull request que elas precisam ser atualizadas).

O mesmo arquivo existe em cada idioma, com o mesmo nome:

```
src/content/docs/pt/resume.md
src/content/docs/es/resume.md
src/content/docs/en/resume.md
```

## Regras da casa

- **Mantenha o tom.** O site é informal e meio grosso de propósito. Não precisa transformar em artigo do LinkedIn.
- **Nada de venda.** Sem link de afiliado, curso, mentoria, ou "me chama na DM". PR assim é fechado na hora.
- **Fonte quando for fato.** Lei, imposto, estudo, número: coloque o link.
- **Livros só em inglês.**
- **Não exponha ninguém.** Nada de nome de colega, gestor, ou dado confidencial de empresa.

## Licença

O conteúdo está sob [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.pt-br): pode copiar e adaptar, desde que dê crédito e mantenha a mesma licença. O código do site está sob licença MIT.

# Dev em Dólar

**Pare de ganhar em shitcoin.** Guia gratuito, open source e sem papo de coach pra profissional de tecnologia brasileiro trabalhar remoto pra fora, ganhando em dólar ou euro.

🇧🇷 Português · 🇪🇸 Español · 🇺🇸 English

> *A free, open-source, no-bullshit guide for Latin American tech professionals to land remote jobs paid in USD/EUR. Available in Portuguese, Spanish and English.*

## O que tem aqui

| Capítulo | Arquivo |
|---|---|
| 0. Manifesto | [`src/content/docs/pt/manifesto.md`](src/content/docs/pt/manifesto.md) |
| 1. Inglês | [`src/content/docs/pt/english.md`](src/content/docs/pt/english.md) |
| 2. Técnica | [`src/content/docs/pt/technical.md`](src/content/docs/pt/technical.md) |
| 3. Currículo | [`src/content/docs/pt/resume.md`](src/content/docs/pt/resume.md) |
| 4. LinkedIn | [`src/content/docs/pt/linkedin.md`](src/content/docs/pt/linkedin.md) |
| 5. Procurar vagas | [`src/content/docs/pt/job-hunting.md`](src/content/docs/pt/job-hunting.md) |
| 6. Entrevista | [`src/content/docs/pt/interview.md`](src/content/docs/pt/interview.md) |
| 7. No trabalho | [`src/content/docs/pt/on-the-job.md`](src/content/docs/pt/on-the-job.md) |

As versões em espanhol e inglês ficam em `src/content/docs/es/` e `src/content/docs/en/`, com os mesmos nomes de arquivo.

Tem também uma **Skill do Claude** pra montar currículo no padrão gringo em [`skills/curriculo-gringa`](skills/curriculo-gringa).

## Contribuir

Leia o [CONTRIBUTING.md](CONTRIBUTING.md). Resumo:

- **Sem saber Git:** clique em "Editar página" no fim de qualquer página do site, ou abra uma [issue](../../issues/new/choose) (tem formulário pra relato, empresa e correção).
- **Sabendo Git:** fork, branch, pull request.

## Rodar localmente

Precisa de [Node.js](https://nodejs.org) 22 ou mais novo.

```bash
npm install
npm run dev      # http://localhost:4321
npm run build    # gera o site estático em dist/
```

Feito com [Astro](https://astro.build) + [Starlight](https://starlight.astro.build). Configurações do site (URL, repositório, carteiras de doação, e-mail de contato) ficam em [`src/config.mjs`](src/config.mjs).

## Licença

- **Conteúdo** (textos em `src/content/` e ilustrações): [CC BY-SA 4.0](LICENSE-CONTENT.md)
- **Código**: [MIT](LICENSE)

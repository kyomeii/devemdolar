# Como contribuir

Valeu por querer ajudar. Esse site só melhora com gente que já passou pelo processo contando o que funcionou.

> 🇪🇸 Las contribuciones en español son bienvenidas. 🇺🇸 Contributions in English are welcome too.

## Jeitos de contribuir

### 1. Sem saber Git

- **Corrigir ou acrescentar algo numa página:** no site, clique em **"Editar página"** no rodapé. O GitHub abre o arquivo, você edita no navegador e clica em **Propose changes**. Isso vira um pull request.
- **Mandar um relato, sugerir empresa ou apontar erro:** abra uma [issue](../../issues/new/choose) e escolha o formulário. Só preencher.

### 2. Sabendo Git

```bash
git clone https://github.com/<seu-usuario>/devemdolar.git
cd devemdolar
npm install
npm run dev
```

1. Faça um fork e crie uma branch (`git checkout -b minha-mudanca`).
2. Os textos ficam em `src/content/docs/<idioma>/`. O mesmo arquivo existe em `pt`, `es` e `en`.
3. Rode `npm run build` antes de mandar, pra garantir que nada quebrou.
4. Abra o pull request explicando o que mudou e por quê.

## Regras da casa

1. **Mantenha o tom.** Informal, direto, meio grosso. Não é artigo de LinkedIn.
2. **Nada de venda.** Sem link de afiliado, curso, mentoria, "me chama na DM". PR assim é fechado sem discussão.
3. **Fonte quando for fato.** Lei, imposto, estudo, número, limite de plataforma: coloque o link.
4. **Livros só em inglês.**
5. **Não exponha ninguém.** Nada de nome de colega, gestor, ou informação confidencial de empresa.
6. **Traduções:** o português é a versão original. Se mudar algo em `pt`, atualize `es` e `en` se souber, ou avise no PR que as traduções precisam ser atualizadas.

## Relatos

Relatos novos vão em `src/content/docs/pt/stories/<um-nome-curto>.md`. O modelo está na página [Relatos](src/content/docs/pt/stories.md). Pode ser anônimo.

## Licença

Ao contribuir, você concorda que seu conteúdo será publicado sob [CC BY-SA 4.0](LICENSE-CONTENT.md) e seu código sob [MIT](LICENSE).

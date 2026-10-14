# Skill: currículo gringa

Uma [Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) pro Claude que monta seu currículo em inglês no padrão do guia: sem firula visual, passando no ATS, com métrica em todo bullet.

## Como instalar

**No Claude.ai (site ou app):**

1. Baixe essa pasta (`curriculo-gringa`) e compacte em `.zip`.
2. Vá em *Settings → Capabilities → Skills* e faça upload do zip.
3. Numa conversa nova, diga: "monta meu currículo pra gringa" e cole seu currículo atual ou LinkedIn.

**No Claude Code:**

Copie a pasta pra `~/.claude/skills/curriculo-gringa/` (ou pra `.claude/skills/` dentro de um projeto).

## O que ela faz

1. Pergunta a vaga-alvo e puxa as palavras-chave.
2. Lê seu material (currículo antigo, LinkedIn, texto solto, em qualquer idioma).
3. Te faz perguntas pra transformar "eu fazia relatório" em bullet com número.
4. Escreve o currículo em Markdown e gera o PDF (com o script `scripts/build_resume.py`), no mesmo formato do exemplo do site.
5. Revisa com você o que tá fraco ou exagerado demais pra sustentar na entrevista.

O modelo fica em [`templates/resume.md`](templates/resume.md).

### Gerar o PDF na mão

Se você editar o `.md` depois, dá pra gerar o PDF de novo sem o Claude:

```bash
pip install reportlab
python scripts/build_resume.py resume.md resume.pdf
```

Por que Markdown e não LaTeX? Pro ATS tanto faz: o que ele precisa é de um PDF com texto selecionável, uma coluna e fonte padrão, e os dois entregam isso. Markdown só é bem mais fácil de editar.

# Skill: vagas gringa

Uma [Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) pro Claude que lê seu currículo e procura vagas remotas no exterior que aceitam gente do Brasil/América Latina, de preferência pagando em dólar.

## Como instalar

**No Claude.ai (site ou app):**

1. Baixe essa pasta (`vagas-gringa`) e compacte em `.zip`.
2. Vá em *Settings → Capabilities → Skills* e faça upload do zip.
3. Numa conversa nova, anexe seu currículo e diga: "procura vagas remotas pra mim na gringa".

**No Claude Code:**

Copie a pasta pra `~/.claude/skills/vagas-gringa/` (ou pra `.claude/skills/` dentro de um projeto).

## O que ela faz

1. Lê seu currículo e resume seu perfil (cargo, senioridade, stack, idiomas).
2. Pergunta o que o currículo não diz: de onde você pode trabalhar, tipo de contrato, se quer só seu cargo atual ou também um passo ao lado ou migração de área.
3. Busca em paralelo, por trilha, em quadros de vagas e páginas das empresas.
4. Entrega uma tabela curta com as melhores vagas, link direto, nota de fit e o que foi verificado de verdade.
5. Mantém um tracker (`vagas_tracker.csv`) pra não repetir vaga nas próximas rodadas.

## Rodando de novo

Rode a cada poucos dias. Anexe o `vagas_tracker.csv` da última rodada (ou deixe ele numa pasta conectada) que a skill só traz vagas novas e reconfere as melhores antigas.

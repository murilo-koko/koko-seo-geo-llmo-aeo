# =========================================================
# KOKO SKILL SERIES
# por Murilo Souza · koko.ag
# Inteligência aplicada, empacotada para uso real.
# =========================================================

# Koko SEO GEO LLMO AEO

Skill pública para auditar landing pages, posts de blog e rascunhos de conteúdo com foco em quatro pilares:

- SEO
- GEO
- AEO
- LLMO

A proposta é simples: você cola uma URL ou um conteúdo e recebe uma leitura clara do que está forte, do que está vazando e do que vale corrigir primeiro.

![Preview da auditoria](./assets/readme-audit-preview.svg)

## Visão Geral

`koko-seo-geo-llmo-aeo` foi criada para transformar uma auditoria que normalmente seria difusa, técnica demais ou difícil de compartilhar em um pacote utilizável.

Em vez de só listar problemas, a skill organiza a análise como entrega de operação:

- scorecard
- diagnóstico
- prioridades
- versão pública para screenshot ou conteúdo social

Ela funciona bem sem integrações externas e foi pensada para uso real, não só para demonstração.

## O Que a Skill Faz

Esta skill pode:

- auditar uma URL ao vivo
- revisar um post antes de publicar
- revisar a copy de uma landing page
- comparar 2 a 5 URLs para detectar sobreposição e risco de canibalização
- rodar uma auditoria `sitewide-lite` a partir de uma homepage
- gerar um `Audit Snapshot`
- gerar um `Public Scorecard`
- gerar um resumo em formato de carrossel para Instagram
- verificar sinais leves de AI search readiness, como `llms.txt`, blocos citáveis, FAQ e estrutura de listas

![Preview do compare mode](./assets/readme-compare-preview.svg)

## Para Quem Ela Foi Feita

Essa skill foi feita para:

- pessoas de marketing que precisam de direção prática
- founders e operadores que querem entender o estado de uma página rapidamente
- criadores de conteúdo que querem revisar um artigo antes de publicar
- times que querem avaliar uma página sem depender de Search Console ou GA
- pessoas que precisam de uma entrega fácil de compartilhar

## Entradas Aceitas

Você pode usar a skill com:

- uma URL
- um rascunho colado no chat
- a copy de uma landing page
- 2 a 5 URLs para comparação
- uma homepage para rodar `sitewide-lite`

## Saídas Esperadas

Por padrão, a skill devolve:

- `Audit Snapshot`
- notas para SEO, GEO, AEO e LLMO
- leitura do que está forte
- leitura do que está vazando
- prioridades de correção

Dependendo do pedido, ela também pode devolver:

- `Public Scorecard`
- `Carousel Summary`
- comparação entre páginas
- risco de canibalização-lite
- leitura de AI citation readiness
- resumo `sitewide-lite`

## Como Instalar Localmente

Clone o repositório:

```bash
git clone https://github.com/murilo-koko/koko-seo-geo-llmo-aeo.git
cd koko-seo-geo-llmo-aeo
```

Depois escolha um dos caminhos abaixo.

Instalação manual:

```bash
ln -s /caminho/absoluto/para/koko-seo-geo-llmo-aeo ~/.codex/skills/koko-seo-geo-llmo-aeo
```

Instalação com script:

```bash
bash install.sh
```

Depois disso, reinicie o Codex para a skill ser carregada.

Para remover o link:

```bash
bash uninstall.sh
```

## Como Usar

Depois de reiniciar o Codex, abra uma nova thread e invoque a skill com:

```text
$koko-seo-geo-llmo-aeo
```

Ou use a skill diretamente dentro do prompt.

Exemplo:

```text
Use $koko-seo-geo-llmo-aeo to audit https://example.com for SEO, GEO, AEO, and LLMO.
```

## Prompts Recomendados

Auditar uma URL:

```text
Use $koko-seo-geo-llmo-aeo to audit https://example.com for SEO, GEO, AEO, and LLMO. Return the Audit Snapshot, top leaks, priority roadmap, and Public Scorecard.
```

Revisar uma landing page:

```text
Use $koko-seo-geo-llmo-aeo to score this landing page and tell me what is leaking first.
```

Revisar um rascunho:

```text
Use $koko-seo-geo-llmo-aeo to review this draft before publication. Score SEO, GEO, AEO, and LLMO, then give me the top fixes.
```

Comparar páginas:

```text
Use $koko-seo-geo-llmo-aeo to compare these URLs and tell me whether they overlap too much. I want overlap score, risk label, and what each page should own.
```

Rodar `sitewide-lite`:

```text
Use $koko-seo-geo-llmo-aeo to run a sitewide-lite audit from this homepage. Crawl a small set of internal pages and tell me the biggest structural issues first.
```

Gerar saída para Instagram:

```text
Use $koko-seo-geo-llmo-aeo to audit this page and also generate a Public Scorecard plus a carousel-ready summary.
```

## Tutorial Rápido

### 1. Teste simples por URL

Cole este prompt:

```text
Use $koko-seo-geo-llmo-aeo to audit https://koko.ag/ for SEO, GEO, AEO, and LLMO.
```

### 2. Teste de comparação

Cole este prompt:

```text
Use $koko-seo-geo-llmo-aeo to compare https://koko.ag/ and https://koko.ag/servicos and tell me whether they overlap too much.
```

### 3. Teste de auditoria leve de site

Cole este prompt:

```text
Use $koko-seo-geo-llmo-aeo to run a sitewide-lite audit from https://koko.ag/.
```

## Exemplos

### Teste técnico por terminal

Se quiser validar a base técnica da skill fora do app:

```bash
uv run python scripts/smoke_test_url.py https://koko.ag/blog/grafico-de-retencao-reels-instagram
```

Comparação por terminal:

```bash
python3 scripts/compare_pages.py https://example.com/page-a https://example.com/page-b
```

Auditoria `sitewide-lite` por terminal:

```bash
python3 scripts/sitewide_lite_audit.py https://example.com --max-pages 5
```

Regenerar previews do README a partir dos demos:

```bash
python3 scripts/render_readme_previews.py \
  --audit-json references/demo-koko-blog.json \
  --compare-json references/demo-compare.json \
  --audit-output assets/readme-audit-preview.svg \
  --compare-output assets/readme-compare-preview.svg
```

## Diferenciais

Os principais diferenciais desta skill hoje são:

- funciona bem sem API externa
- já nasce com saída compartilhável
- trata SEO, GEO, AEO e LLMO como pacote único
- já inclui `compare mode`
- já inclui `sitewide-lite`
- já inclui sinais de `AI citation readiness`
- foi embalada para uso real, não só para benchmarking técnico

## Limites e Guardrails

Essa skill não deve:

- fingir precisão quando faltam insumos
- inventar métricas de Search Console, GA ou SERP
- depender de integrações para ser útil
- vender score como verdade absoluta

Ela foi desenhada para:

- orientar decisão
- apontar vazamentos
- priorizar correções

Não foi desenhada para substituir por completo uma operação avançada com dados proprietários.

## Sobre o Autor

Criado por [Murilo Souza](https://www.linkedin.com/in/murilo-koko/).

- Instagram: [@murilo.sn](https://www.instagram.com/murilo.sn/)
- LinkedIn: [murilo-koko](https://www.linkedin.com/in/murilo-koko/)
- Koko: [koko.ag](https://koko.ag/)

## Licença

Este repositório usa licença [MIT](./LICENSE).

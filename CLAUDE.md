# amigos-dieta-posts

Artes e material dos posts do Instagram @amigos.dieta (Vinicius). Tudo em português do Brasil.

## O que tem aqui

- `posts/AAAA-MM-DD/` — artes (JPEG 1080x1350) de cada dia, servidas em
  `https://raw.githubusercontent.com/viniloren/amigos-dieta-posts/main/posts/AAAA-MM-DD/<arquivo>.jpg`.
  O Instagram (via Windsor.ai) só aceita imagens por link público, por isso elas ficam aqui.
- `gerador/artes.py` — gera slides no visual da marca: `page(corpo_html, selo, contador=None, foot="")`,
  `render(nome, html)` → JPEG em `$ARTES_OUT` (padrão `/tmp/artes-out`), `img(caminho)`, `foot_swipe()`.
  Classes prontas: `.wrap`, `.kicker`, `h1`/`h2` com `<em>` em laranja, `.sub`, `.pills/.pill`, `.photo`,
  `.card` + `.label`, `ul.list`, `ol.steps`, `.price`, `.cta`. Precisa de `google-chrome` (headless).
- `gerador/exemplo_dia_2411.py` — exemplo completo de um dia (4 posts, 14 slides). Copie o padrão.
- `biblioteca/fotos/<ebook>/pNNN-K.jpg` — fotos tiradas dos PDFs dos e-books. `biblioteca/indice-fotos.json`
  diz a página e o texto do topo da página de cada foto, para achar a foto de uma receita
  (procure o nome da receita em `texto_da_pagina`; no PDF de carne há 2 receitas por página, então
  abra a imagem para conferir antes de usar). As fotos de salada são pequenas: use em tamanho moderado.
- `biblioteca/fontes/` — Baloo 2 e DM Sans (as fontes do site).

## Regras de conteúdo

- Só o e-book "Sobremesas de Domingo" pode ser chamado de "zero açúcar" e "sem glúten". Os outros
  (36 Receitas de Salada, Carne Moída: 90 Receitas, 100 Receitas Natalinas) nunca.
- Não inventar depoimentos, números de vendas ou resultados. Nada de promessa de emagrecimento ou
  afirmação médica.
- O ManyChat ("Comente QUERO") só funciona no post das 5 sobremesas grátis; não use "Comente QUERO"
  em outros posts, a menos que o Vinicius diga que ampliou a automação.

## Publicação

Publicar SEMPRE só depois do "aprovado" do Vinicius na conversa, para os posts daquele dia.
Windsor.ai for Social Media: connector `instagram`, account `17841472503944181`;
`create_carousel_post` (image_urls, 2 a 10) ou `create_image_post` (image_url), com `caption`.
Depois de publicar, marcar "Postado" na coluna K da planilha "Calendário de posts – @amigos.dieta"
(Sheet `1930ff0d-8080-442c-a4f6-47c64246a006`, aba "Calendário", 1 linha por post, a partir da linha 2).

Commits: autor `viniloren <viniloren@users.noreply.github.com>`, direto na `main`.

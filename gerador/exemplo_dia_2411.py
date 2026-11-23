import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artes import *

S = FOTOS + '/exemplo-2411'
out = {}

# ---------- 11:00 SALADA: Salada Caesar (carrossel receita) ----------
sal = []
sal.append(render("2411-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">Almoço que sustenta</div>
  <h1 style="font-size:150px">Salada<br><em>Caesar</em></h1>
  <div class="sub">Frango, croutons crocantes e molho cremoso de parmesão.</div>
  <div style="display:flex;gap:34px;align-items:flex-end;margin-top:auto">
    <div class="photo" style="width:430px;height:520px"><img src="{img(S+'/caesar-up.jpg')}"></div>
    <div class="pills" style="flex-direction:column;align-items:flex-start;margin:0 0 20px">
      <span class="pill">Fácil</span><span class="pill">Com proteína</span><span class="pill">Ingredientes de mercado</span>
    </div>
  </div>
</div>""", "RECEITA", foot=foot_swipe())))
sal.append(render("2411-salada-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Para o molho</div><ul class="list" style="gap:10px">
    <li>6 colheres (sopa) de maionese</li><li>40 g de parmesão ralado grosso</li>
    <li>3 colheres (sopa) de suco de limão</li><li>2 colheres (sopa) de azeite</li>
    <li>1 a 2 filés de anchova</li><li>1 dente de alho picado</li><li>Sal e pimenta-do-reino</li></ul></div>
  <div class="card"><div class="label">Para a salada</div><ul class="list">
    <li>1 pé de alface-americana</li><li>1 a 2 filés de peito de frango</li><li>½ xícara de croutons</li></ul></div>
</div>""", None, contador="2/4")))
sal.append(render("2411-salada-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps">
    <li>Tempere o frango com sal e pimenta, grelhe na frigideira e corte em tiras.</li>
    <li>Misture maionese, parmesão, limão, azeite, anchova e alho até virar um molho cremoso.</li>
    <li>Distribua a alface numa travessa e coloque o frango e os croutons por cima.</li>
    <li>Jogue bastante molho e finalize com mais parmesão. Agora é só servir!</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Sem croutons? Toste cubinhos de pão na frigideira com um fio de azeite por 5 minutos.</div></div>
</div>""", None, contador="3/4")))
sal.append(render("2411-salada-4", page("""
<div class="wrap" style="justify-content:center">
  <div class="kicker">Gostou?</div>
  <h1 style="font-size:104px">Mais <em>35 saladas</em><br>que matam a fome</h1>
  <div class="sub">Pratos completos, com proteína, grãos e molhos especiais, no e-book <b>36 Receitas de Salada</b>.</div>
  <div class="price" style="margin-top:46px"><small>R$</small>9,90</div>
  <div class="sub" style="font-size:30px;margin-top:10px">Pix ou cartão · chega no seu e-mail na hora</div>
</div>
<div class="foot" style="bottom:64px;display:block"><div class="cta"><span>Link na bio</span><small>Salve este post<br>pra fazer depois 💚</small></div></div>
""", "OFERTA")))
out["salada"] = sal

# ---------- 17:30 CARNE: qual corte pedir moído (carrossel dica) ----------
car = []
car.append(render("2411-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Dica de açougue</div>
  <h1 style="font-size:116px">Qual corte pedir<br><em>moído?</em></h1>
  <div class="sub">A escolha certa muda o resultado da receita.</div>
  <div class="photo" style="width:100%;height:560px;margin-top:auto"><img src="{img(S+'/carne-foto.jpg')}"></div>
</div>""", "DICA", foot=foot_swipe())))
car.append(render("2411-carne-2", page("""
<div class="wrap">
  <h2>Patinho: <em>o curinga</em></h2>
  <div class="sub" style="margin:0 0 36px">Magro e saboroso. Vai bem em quase tudo.</div>
  <div class="card"><div class="label">Use em</div><ul class="list">
    <li>Molho à bolonhesa e lasanha</li><li>Escondidinho e torta</li><li>Recheio de panqueca e tapioca</li></ul></div>
  <div class="card" style="margin-top:28px"><div class="label">Atenção</div>
    <div style="font-size:38px;line-height:1.32">Por ter pouca gordura, pode ressecar. Não cozinhe demais.</div></div>
</div>""", None, contador="2/5")))
car.append(render("2411-carne-3", page("""
<div class="wrap">
  <h2>Acém ou fraldinha: <em>suculência</em></h2>
  <div class="sub" style="margin:0 0 36px">Um pouco mais de gordura, mais sabor e mais suco.</div>
  <div class="card"><div class="label">Use em</div><ul class="list">
    <li>Hambúrguer artesanal</li><li>Almôndega e polpetone</li><li>Rocambole e kafta</li></ul></div>
  <div class="card" style="margin-top:28px"><div class="label">Combinação</div>
    <div style="font-size:38px;line-height:1.32">Patinho + fraldinha meio a meio: magro e suculento ao mesmo tempo.</div></div>
</div>""", None, contador="3/5")))
car.append(render("2411-carne-4", page("""
<div class="wrap">
  <h2>3 dicas no <em>balcão</em></h2>
  <ol class="steps">
    <li>Escolha a peça e peça para moer na hora, na sua frente.</li>
    <li>Para almôndega, quibe e hambúrguer, peça para moer duas vezes: a massa fica mais lisa.</li>
    <li>Leve só o que vai usar em até 2 dias. O resto, congele em porções.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Bônus</div>
    <div style="font-size:38px;line-height:1.32">Congele achatada, em saquinhos de 500 g: ocupa menos espaço e descongela bem mais rápido na geladeira.</div></div>
</div>""", None, contador="4/5")))
car.append(render("2411-carne-5", page("""
<div class="wrap" style="justify-content:center">
  <div class="kicker">E agora, o que fazer?</div>
  <h1 style="font-size:104px"><em>90 receitas</em><br>com carne moída</h1>
  <div class="sub">Rocamboles, quibes, almôndegas, escondidinhos, tortas, lanches e muito mais no e-book <b>Carne Moída: 90 Receitas</b>.</div>
  <div class="price" style="margin-top:46px"><small>R$</small>19,90</div>
  <div class="sub" style="font-size:30px;margin-top:10px">Pix ou cartão · chega no seu e-mail na hora</div>
</div>
<div class="foot" style="bottom:64px;display:block"><div class="cta"><span>Link na bio</span><small>Salve e mande pra<br>quem cozinha aí 💚</small></div></div>
""", "OFERTA")))
out["carne"] = car

# ---------- 19:30 NATAL: venda (carrossel 4 slides) ----------
nat = []
nat.append(render("2411-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Faltam 31 dias</div>
  <h1 style="font-size:124px">Ainda não sabe<br>o que fazer<br>na <em>ceia?</em></h1>
  <div class="photo" style="width:100%;height:520px;margin-top:auto"><img src="{img(S+'/nat31-000.jpg')}"></div>
</div>""", "NATAL", foot=foot_swipe())))
nat.append(render("2411-natal-2", page("""
<div class="wrap">
  <h2>A ceia <em>completa</em>, da entrada à sobremesa</h2>
  <div class="card"><ul class="list">
    <li>Entradas e petiscos</li><li>Saladas e acompanhamentos</li><li>Aves e carnes</li>
    <li>Peixes e frutos do mar</li><li>Arroz, farofas e purês</li><li>Pães, rabanadas e panetones</li>
    <li>Sobremesas geladas</li><li>Doces e bolos de Natal</li><li>Bebidas natalinas</li></ul></div>
</div>""", None, contador="2/4")))
nat.append(render("2411-natal-3", page(f"""
<div class="wrap">
  <h2>Cada receita com <em>tempo, rendimento</em> e passo a passo</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto">
    <div class="photo" style="grid-column:1/3;height:400px"><img src="{img(S+'/nat36-000.jpg')}"></div>
    <div class="photo" style="height:250px"><img src="{img(S+'/nat37-000.jpg')}"></div>
    <div class="photo" style="height:250px"><img src="{img(S+'/nat68-000.jpg')}"></div>
  </div>
  <div class="sub" style="font-size:28px;margin-top:18px">Tender com mel e mostarda · Pernil na cerveja · Rabanada</div>
</div>""", None, contador="3/4")))
nat.append(render("2411-natal-4", page("""
<div class="wrap" style="justify-content:center">
  <div class="kicker">E-book em PDF</div>
  <h1 style="font-size:116px"><em>100 Receitas</em><br>Natalinas</h1>
  <div class="sub">Planeje a ceia inteira hoje e chegue no dia 24 sem estresse.</div>
  <div class="price" style="margin-top:46px"><small>R$</small>19,90</div>
  <div class="sub" style="font-size:30px;margin-top:10px">Pix ou cartão · chega no e-mail na hora · garantia de 7 dias</div>
</div>
<div class="foot" style="bottom:64px;display:block"><div class="cta"><span>Link na bio</span><small>Marque quem faz<br>a ceia aí 💚</small></div></div>
""", "OFERTA")))
out["natal"] = nat

# ---------- 21:00 SOBREMESAS: isso ou aquilo (post único) ----------
sob = [render("2411-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Isso ou aquilo?</div>
  <h1 style="font-size:132px"><em>Pudim</em> ou<br><em>brigadeiro?</em></h1>
  <div class="sub">As duas versões são zero açúcar e sem glúten. Qual você faria hoje?</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:auto">
    <div><div class="photo" style="height:430px"><img src="{img(S+'/sob145-001.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:18px">1 · Pudim</div></div>
    <div><div class="photo" style="height:430px"><img src="{img(S+'/sob52-001.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:18px">2 · Brigadeiro</div></div>
  </div>
</div>
<div class="foot" style="bottom:52px"><span></span><span>Comente 1 ou 2 👇</span></div>
""", "ZERO AÇÚCAR"))]
out["sobremesas"] = sob

import json
json.dump(out, open(f"{OUT}/2411.json", "w"), indent=1)
print(json.dumps(out, indent=1))

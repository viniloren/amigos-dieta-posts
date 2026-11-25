import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artes import *

F = FOTOS + '/fotos'
out = {}


def oferta(kicker, titulo, sub, preco, extra, cta_small, selo="OFERTA"):
    return page(f"""
<div class="wrap" style="justify-content:center">
  <div class="kicker">{kicker}</div>
  <h1 style="font-size:104px">{titulo}</h1>
  <div class="sub">{sub}</div>
  <div class="price" style="margin-top:46px"><small>R$</small>{preco}</div>
  <div class="sub" style="font-size:30px;margin-top:10px">{extra}</div>
</div>
<div class="foot" style="bottom:64px;display:block"><div class="cta"><span>Link na bio</span><small>{cta_small}</small></div></div>
""", selo)


# ---------- 11:00 SALADA: Frango e Abacate (Reels -> carrossel 4) ----------
sal = []
sal.append(render("2511-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">Salada que mata a fome de verdade</div>
  <h1 style="font-size:140px">Frango<br>e <em>abacate</em></h1>
  <div class="sub">Proteína, gordura boa e crocância.</div>
  <div style="display:flex;gap:34px;align-items:flex-end;margin-top:auto">
    <div class="photo" style="width:440px;height:540px"><img src="{img(F+'/salada/p018-0.jpg')}"></div>
    <div class="pills" style="flex-direction:column;align-items:flex-start;margin:0 0 20px">
      <span class="pill">Pronta em 20 min</span><span class="pill">Com proteína</span><span class="pill">2 porções</span>
    </div>
  </div>
</div>""", "RECEITA", foot=foot_swipe())))
sal.append(render("2511-salada-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Para a salada</div><ul class="list" style="gap:12px">
    <li>2 filés de peito de frango (300 g)</li><li>1 abacate maduro pequeno</li>
    <li>2 xícaras de folhas (alface e rúcula)</li><li>10 tomates-cereja</li>
    <li>½ cebola-roxa em fatias finas</li><li>½ xícara de milho cozido</li></ul></div>
  <div class="card"><div class="label">Para o molho</div><ul class="list" style="gap:12px">
    <li>3 colheres (sopa) de azeite</li><li>Suco de 1 limão</li>
    <li>1 colher (chá) de mostarda</li><li>Sal e pimenta-do-reino</li></ul></div>
</div>""", None, contador="2/4")))
sal.append(render("2511-salada-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps">
    <li>Tempere o frango com sal, pimenta e limão. Grelhe 5 a 6 minutos de cada lado, descanse e fatie.</li>
    <li>Corte o abacate em cubos e regue com um pouco de limão para não escurecer.</li>
    <li>Monte as folhas, o tomate, a cebola, o milho e o abacate. Coloque o frango por cima.</li>
    <li>Chacoalhe os ingredientes do molho num pote fechado e regue só na hora de servir.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Vai levar de marmita? Leve o molho num potinho separado e as folhas ficam crocantes.</div></div>
</div>""", None, contador="3/4")))
sal.append(render("2511-salada-4", oferta(
    "Gostou?", "Mais <em>35 saladas</em><br>que matam a fome",
    "Pratos completos, com proteína, grãos e molhos especiais, no e-book <b>36 Receitas de Salada</b>.",
    "9,90", "Pix ou cartão · chega no seu e-mail na hora", "Salve este post<br>pra fazer depois 💚")))
out["salada"] = sal

# ---------- 17:30 CARNE: Escondidinho com purê de mandioca (carrossel receita) ----------
car = []
car.append(render("2511-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Passo a passo</div>
  <h1 style="font-size:112px">Escondidinho<br>de carne com<br><em>purê de mandioca</em></h1>
  <div class="photo" style="width:100%;height:540px;margin-top:auto"><img src="{img(F+'/carne/p021-1.jpg')}"></div>
</div>""", "RECEITA", foot=foot_swipe())))
car.append(render("2511-carne-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:22px"><div class="label">Purê</div><ul class="list" style="gap:10px">
    <li>1 kg de mandioca descascada</li><li>1 colher (sopa) de manteiga</li><li>1 xícara de leite quente</li><li>Sal a gosto</li></ul></div>
  <div class="card" style="margin-bottom:22px"><div class="label">Recheio</div><ul class="list" style="gap:10px">
    <li>500 g de carne moída</li><li>1 cebola e 2 dentes de alho picados</li><li>2 tomates picados</li><li>Cheiro-verde, sal e pimenta</li></ul></div>
  <div class="card"><div class="label">Cobertura</div><ul class="list">
    <li>150 g de muçarela ralada</li></ul></div>
</div>""", None, contador="2/4")))
car.append(render("2511-carne-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Cozinhe a mandioca em água com sal até ficar bem macia (cerca de 15 min na pressão). Tire o fio do meio.</li>
    <li>Amasse ainda quente com a manteiga e o leite até virar um purê liso. Acerte o sal.</li>
    <li>Refogue cebola e alho, junte a carne e frite até soltar. Entre com o tomate, sal e pimenta e cozinhe 10 min. Finalize com cheiro-verde.</li>
    <li>Na travessa: metade do purê, a carne, o resto do purê e a muçarela. Forno a 200 °C por 20 min, até gratinar.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Quer adiantar? Monte na véspera, cubra e guarde na geladeira. No dia, forno por cerca de 30 min.</div></div>
</div>""", None, contador="3/4")))
car.append(render("2511-carne-4", oferta(
    "E amanhã?", "<em>90 receitas</em><br>com carne moída",
    "Escondidinhos, rocamboles, quibes, almôndegas, tortas e lanches no e-book <b>Carne Moída: 90 Receitas</b>.",
    "19,90", "Pix ou cartão · chega no seu e-mail na hora", "Salve e mande pra<br>quem cozinha aí 💚")))
out["carne"] = car

# ---------- 19:30 NATAL: Tender com mel e mostarda (Reels -> carrossel 5) ----------
nat = []
nat.append(render("2511-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Faltam 29 dias</div>
  <h1 style="font-size:84px">Esse vai ser o prato<br>mais elogiado da ceia:</h1>
  <h1 style="font-size:116px;margin-top:14px"><em>Tender com mel<br>e mostarda</em></h1>
  <div class="photo" style="width:100%;height:470px;margin-top:auto"><img src="{img(F+'/natal/p036-0.jpg')}"></div>
</div>""", "NATAL", foot=foot_swipe())))
nat.append(render("2511-natal-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>1 tender (cerca de 1,5 kg)</li>
    <li>4 colheres (sopa) de mel</li>
    <li>3 colheres (sopa) de mostarda (amarela ou dijon)</li>
    <li>3 colheres (sopa) de suco de laranja</li>
    <li>Cravos-da-índia para espetar</li>
    <li>Rodelas de abacaxi para decorar (opcional)</li></ul></div>
  <div class="pills" style="margin-top:auto"><span class="pill">Serve 8 a 10 pessoas</span><span class="pill">Cerca de 1 hora</span></div>
</div>""", None, contador="2/5")))
nat.append(render("2511-natal-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Preaqueça o forno a 180 °C. Tire a embalagem e a rede do tender.</li>
    <li>Faça cortes em losango na superfície (cerca de 1 cm de fundo) e espete um cravo em cada cruzamento.</li>
    <li>Misture mel, mostarda e suco de laranja. Pincele metade, cubra com papel-alumínio e asse por 40 min.</li>
    <li>Tire o papel, pincele o resto do molho, ponha o abacaxi e asse mais 20 min, regando com o caldo, até dourar.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Bom saber</div>
    <div style="font-size:38px;line-height:1.32">O tender já vem cozido: o forno serve para aquecer e caramelizar o molho.</div></div>
</div>""", None, contador="3/5")))
nat.append(render("2511-natal-4", page("""
<div class="wrap">
  <h2>Truques pra <em>ceia sem correria</em></h2>
  <div class="card" style="margin-bottom:26px"><div class="label">Na véspera</div>
    <div style="font-size:40px;line-height:1.32">Faça os cortes, espete os cravos e deixe o molho pronto na geladeira. No dia 24 é só pincelar e assar.</div></div>
  <div class="card" style="margin-bottom:26px"><div class="label">Brilho de vitrine</div>
    <div style="font-size:40px;line-height:1.32">Nos últimos 10 minutos, regue de novo com o caldo da assadeira. É isso que deixa o tender brilhante.</div></div>
  <div class="card"><div class="label">Sobrou?</div>
    <div style="font-size:40px;line-height:1.32">Fatie fino e use no sanduíche do dia 25.</div></div>
</div>""", None, contador="4/5")))
nat.append(render("2511-natal-5", oferta(
    "E-book em PDF", "<em>100 Receitas</em><br>Natalinas",
    "Da entrada à sobremesa: planeje a ceia inteira hoje e chegue no dia 24 sem estresse.",
    "19,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Marque quem faz<br>a ceia aí 💚")))
out["natal"] = nat

# ---------- 21:00 SOBREMESAS: Brigadeiro de colher fit (carrossel receita) ----------
sob = []
sob.append(render("2511-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Passo a passo</div>
  <h1 style="font-size:124px">Brigadeiro<br>de colher <em>fit</em></h1>
  <div class="pills"><span class="pill">Zero açúcar</span><span class="pill">Sem glúten</span><span class="pill">6 ingredientes</span></div>
  <div class="photo" style="width:620px;height:620px;margin:auto auto 0"><img src="{img(F+'/sobremesas/p052-0.jpg')}"></div>
</div>""", "ZERO AÇÚCAR", foot=foot_swipe())))
sob.append(render("2511-sobremesas-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>1 xícara (240 ml) de leite</li>
    <li>1 xícara de leite em pó</li>
    <li>3 colheres (sopa) de cacau em pó 100%</li>
    <li>4 colheres (sopa) de xilitol ou eritritol</li>
    <li>1 colher (sopa) de manteiga ou óleo de coco</li>
    <li>Cacau ou nibs para finalizar</li></ul></div>
  <div class="card" style="margin-top:auto"><div class="label">Atenção</div>
    <div style="font-size:36px;line-height:1.32">Confira no rótulo do leite em pó e do cacau o aviso “não contém glúten”.</div></div>
</div>""", None, contador="2/4")))
sob.append(render("2511-sobremesas-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps">
    <li>Na panela, ainda fora do fogo, misture tudo até não sobrar nenhum grumo.</li>
    <li>Leve ao fogo baixo, mexendo sem parar, por 8 a 10 minutos, até engrossar e começar a soltar do fundo.</li>
    <li>Passe para potinhos e cubra com filme encostando no creme, pra não formar película.</li>
    <li>Deixe esfriar e leve à geladeira por 1 hora. Finalize com cacau ou nibs.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Quer de enrolar? Cozinhe mais uns 5 minutos, até a massa desgrudar inteira do fundo da panela.</div></div>
</div>""", None, contador="3/4")))
sob.append(render("2511-sobremesas-4", oferta(
    "Gostou?", "<em>200 sobremesas</em><br>zero açúcar",
    "Todas sem glúten, no e-book <b>Sobremesas de Domingo – Versão Zero</b>.",
    "24,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e marque quem<br>ama um docinho 💚")))
out["sobremesas"] = sob

import json
json.dump(out, open(f"{OUT}/2511.json", "w"), indent=1)
print(json.dumps(out, indent=1))

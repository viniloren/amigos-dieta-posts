import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artes import *

F = FOTOS + "/fotos"
out = {}


def cta_final(kicker, titulo, texto, preco, extra, selo_cta):
    return page(f"""
<div class="wrap" style="justify-content:center">
  <div class="kicker">{kicker}</div>
  <h1 style="font-size:104px">{titulo}</h1>
  <div class="sub">{texto}</div>
  <div class="price" style="margin-top:46px"><small>R$</small>{preco}</div>
  <div class="sub" style="font-size:30px;margin-top:10px">Pix ou cartão · chega no seu e-mail na hora</div>
</div>
<div class="foot" style="bottom:64px;display:block"><div class="cta"><span>Link na bio</span><small>{extra}</small></div></div>
""", selo_cta)


# ---------- SALADA: Salada Primavera ----------
s = []
s.append(render("2311-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">Pronta em 10 minutos</div>
  <h1 style="font-size:140px">Salada<br><em>Primavera</em></h1>
  <div class="sub">Alface, tomate-cereja, palmito e manga. Fresca, colorida e sem fogão.</div>
  <div style="display:flex;gap:34px;align-items:flex-end;margin-top:auto">
    <div class="photo" style="width:440px;height:530px"><img src="{img(F+'/salada/p034-0.jpg')}"></div>
    <div class="pills" style="flex-direction:column;align-items:flex-start;margin:0 0 20px">
      <span class="pill">Sem fogão</span><span class="pill">6 ingredientes</span><span class="pill">Refrescante</span>
    </div>
  </div>
</div>""", "RECEITA", foot=foot_swipe())))
s.append(render("2311-salada-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>1 maço de alface-americana</li><li>1 maço de alface crespa</li>
    <li>1 xícara de tomate-cereja cortado ao meio</li><li>1 xícara de palmito pupunha cortado</li>
    <li>1 manga picada</li><li>Sal, azeite e orégano a gosto</li></ul></div>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Quer transformar em almoço completo? Junte frango desfiado ou grão-de-bico.</div></div>
</div>""", None, contador="2/4")))
s.append(render("2311-salada-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps">
    <li>Lave bem as folhas, seque e rasgue com as mãos numa saladeira.</li>
    <li>Junte os tomates-cereja cortados ao meio.</li>
    <li>Acrescente o palmito pupunha e a manga picada.</li>
    <li>Tempere com sal, azeite e orégano na hora de servir.</li>
  </ol>
</div>""", None, contador="3/4")))
s.append(render("2311-salada-4", cta_final("Gostou?", "Mais <em>35 saladas</em><br>que matam a fome",
    "Pratos completos, com proteína, grãos e molhos especiais, no e-book <b>36 Receitas de Salada</b>.",
    "9,90", "Salve este post<br>pra fazer depois 💚", "OFERTA")))
out["salada"] = s

# ---------- CARNE: Batata Recheada ----------
c = []
c.append(render("2311-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Janta que todo mundo ama</div>
  <h1 style="font-size:118px">Batata <em>recheada</em><br>com carne moída</h1>
  <div class="sub">Gratinada com mussarela. Serve 4 pessoas.</div>
  <div class="photo" style="width:100%;height:560px;margin-top:auto"><img src="{img(F+'/carne/p040-1.jpg')}"></div>
</div>""", "RECEITA", foot=foot_swipe())))
c.append(render("2311-carne-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>4 batatas grandes</li><li>400 g de carne moída</li><li>1 cebola e 2 dentes de alho</li>
    <li>Sal, pimenta e salsinha</li><li>100 g de creme de leite</li><li>100 g de mussarela ralada</li><li>Azeite a gosto</li></ul></div>
  <div class="card" style="margin-top:auto"><div class="label">Tempo</div>
    <div style="font-size:38px;line-height:1.32">20 min de preparo + 60 min de forno</div></div>
</div>""", None, contador="2/4")))
c.append(render("2311-carne-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:26px">
    <li>Lave as batatas e asse inteiras a 200 °C por 50 a 60 minutos.</li>
    <li>Corte ao meio e retire a polpa com cuidado.</li>
    <li>Refogue a carne com cebola, alho e temperos.</li>
    <li>Misture a polpa com o creme de leite e junte a carne.</li>
    <li>Recheie as cascas, cubra com mussarela e gratine por 10 minutos.</li>
  </ol>
</div>""", None, contador="3/4")))
c.append(render("2311-carne-4", cta_final("Gostou?", "<em>90 receitas</em><br>com carne moída",
    "Rocamboles, quibes, almôndegas, escondidinhos, tortas, lanches e muito mais no e-book <b>Carne Moída: 90 Receitas</b>.",
    "19,90", "Salve e mande pra<br>quem cozinha aí 💚", "OFERTA")))
out["carne"] = c

# ---------- NATAL: Salmão com crosta de ervas ----------
n = []
n.append(render("2311-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Ceia leve e elegante</div>
  <h1 style="font-size:116px">Salmão com<br><em>crosta de ervas</em></h1>
  <div class="sub">Cara de restaurante, 20 minutos de forno. Serve 6 pessoas.</div>
  <div class="photo" style="width:100%;height:540px;margin-top:auto"><img src="{img(F+'/natal/p049-0.jpg')}"></div>
</div>""", "NATAL", foot=foot_swipe())))
n.append(render("2311-natal-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>1 filé de salmão de 1,2 kg com pele</li><li>4 colheres (sopa) de farinha panko</li>
    <li>3 colheres (sopa) de manteiga derretida</li><li>4 colheres (sopa) de ervas picadas (dill, salsinha, cebolinha)</li>
    <li>Raspas e suco de 1 limão</li><li>2 dentes de alho socados</li><li>2 colheres (sopa) de mostarda Dijon</li><li>Sal e pimenta-do-reino</li></ul></div>
</div>""", None, contador="2/4")))
n.append(render("2311-natal-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:24px">
    <li>Tire o salmão da geladeira 20 minutos antes.</li>
    <li>Seque, tempere com sal, pimenta e limão e coloque na assadeira forrada.</li>
    <li>Espalhe a mostarda por cima: é a "cola" da crosta.</li>
    <li>Misture panko, manteiga, ervas, alho e raspas de limão e aperte sobre o peixe.</li>
    <li>Asse a 200 °C por 18 a 22 minutos, até o centro ficar rosado.</li>
  </ol>
</div>""", None, contador="3/4")))
n.append(render("2311-natal-4", cta_final("E tem mais 99", "<em>100 Receitas</em><br>Natalinas",
    "A ceia completa, da entrada à sobremesa, com tempo, rendimento e passo a passo em cada receita.",
    "19,90", "Marque quem faz<br>a ceia aí 💚", "OFERTA")))
out["natal"] = n

# ---------- SOBREMESAS: Mousse de Chocolate Fit ----------
d = []
d.append(render("2311-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Zero açúcar · sem glúten</div>
  <h1 style="font-size:130px">Mousse de<br><em>chocolate</em></h1>
  <div class="sub">Cremoso, com cacau e leite de coco. Só 5 ingredientes.</div>
  <div style="display:flex;gap:34px;align-items:flex-end;margin-top:auto">
    <div class="photo" style="width:500px;height:500px"><img src="{img(F+'/sobremesas/p111-0.jpg')}"></div>
    <div class="pills" style="flex-direction:column;align-items:flex-start;margin:0 0 20px">
      <span class="pill">Zero açúcar</span><span class="pill">Sem glúten</span><span class="pill">Sem lactose</span>
    </div>
  </div>
</div>""", "RECEITA", foot=foot_swipe())))
d.append(render("2311-sobremesas-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card"><ul class="list">
    <li>½ xícara de cacau em pó</li><li>½ xícara de leite de coco</li>
    <li>¼ xícara de adoçante (eritritol, xilitol ou açúcar de coco)</li>
    <li>1 envelope de gelatina incolor sem sabor</li><li>½ xícara de claras</li></ul></div>
  <div class="card" style="margin-top:auto"><div class="label">Tempo</div>
    <div style="font-size:38px;line-height:1.32">15 min de preparo + 2 horas de geladeira</div></div>
</div>""", None, contador="2/4")))
d.append(render("2311-sobremesas-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:26px">
    <li>Hidrate a gelatina como indica a embalagem.</li>
    <li>Misture o cacau com o leite de coco e o adoçante até ficar liso.</li>
    <li>Aqueça a gelatina até dissolver e junte ao creme de chocolate.</li>
    <li>Bata as claras em neve e incorpore com delicadeza.</li>
    <li>Divida em taças e leve à geladeira por pelo menos 2 horas.</li>
  </ol>
</div>""", None, contador="3/4")))
d.append(render("2311-sobremesas-4", cta_final("Tem mais 199", "<em>200 sobremesas</em><br>zero açúcar",
    "Pudim, quindim, brownie, cheesecake e muito mais, sem açúcar e sem glúten, no e-book <b>Sobremesas de Domingo</b>.",
    "24,90", "Marque quem não<br>vive sem doce 💚", "OFERTA")))
out["sobremesas"] = d

json.dump(out, open(f"{OUT}/2311.json", "w"), indent=1)
print("ok", sum(len(v) for v in out.values()))

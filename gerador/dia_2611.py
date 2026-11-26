import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artes import *
from PIL import Image

F = FOTOS + '/fotos'
out = {}

# Foto do pudim de coco sem as faixas pretas e sem a marca d'água do canto
PUDIM = f"{OUT}/pudim-coco-crop.jpg"
Image.open(F + '/sobremesas/p150-0.jpg').crop((0, 48, 260, 290)).save(PUDIM, quality=95)


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


def dica(nome, n, total, titulo, sub, label, itens, label2, texto2):
    lis = "".join(f"<li>{i}</li>" for i in itens)
    return render(nome, page(f"""
<div class="wrap">
  <h2>{titulo}</h2>
  <div class="sub" style="margin:0 0 36px">{sub}</div>
  <div class="card"><div class="label">{label}</div><ul class="list">{lis}</ul></div>
  <div class="card" style="margin-top:auto"><div class="label">{label2}</div>
    <div style="font-size:38px;line-height:1.32">{texto2}</div></div>
</div>""", None, contador=f"{n}/{total}"))


# ---------- 11:00 SALADA: a fórmula da salada que sustenta (carrossel dica, 6) ----------
sal = []
sal.append(render("2611-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">A fórmula da salada que sustenta</div>
  <h1 style="font-size:96px">Folha + <em>proteína</em><br>+ grão + <em>crocante</em><br>+ molho</h1>
  <div class="sub">5 partes. Monte assim e a salada vira refeição.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:auto">
    <div class="photo" style="height:500px"><img src="{img(F+'/salada/p030-0.jpg')}"></div>
    <div class="photo" style="height:500px"><img src="{img(F+'/salada/p020-0.jpg')}"></div>
  </div>
</div>""", "DICA", foot=foot_swipe())))
sal.append(dica("2611-salada-2", 2, 6, "1. Folha + <em>2. Proteína</em>",
                "A folha dá volume. A proteína faz a salada virar prato principal.",
                "Proteína: escolha 1", ["Frango grelhado desfiado ou em tiras", "2 ovos cozidos",
                                       "1 lata de atum ou sardinha", "Queijo branco em cubos", "Grão-de-bico ou lentilha"],
                "Folhas", "Misture 2 tipos: uma macia (alface) e uma com sabor (rúcula, agrião ou repolho roxo)."))
sal.append(dica("2611-salada-3", 3, 6, "3. <em>Grão</em>",
                "É o que dá corpo e deixa a salada mais completa.",
                "Opções", ["Quinoa ou arroz integral", "Lentilha ou grão-de-bico",
                           "Feijão-preto ou feijão-fradinho", "Milho cozido", "Batata ou batata-doce em cubos"],
                "Adiante", "Cozinhe uma porção no domingo e guarde num pote fechado na geladeira por até 4 dias."))
sal.append(dica("2611-salada-4", 4, 6, "4. <em>Crocante</em>",
                "Uma colherada já muda a textura da salada inteira.",
                "Opções", ["Castanhas, amêndoas ou nozes picadas", "Sementes de girassol ou abóbora",
                           "Croutons de frigideira", "Chips de batata-doce", "Cebola-roxa em fatias finas"],
                "Truque", "Toste as sementes por 2 a 3 minutos na frigideira seca, mexendo. O sabor fica outro."))
sal.append(render("2611-salada-5", page("""
<div class="wrap">
  <h2>5. <em>Molho</em></h2>
  <div class="sub" style="margin:0 0 34px">Regra de ouro: 3 partes de azeite para 1 de ácido.</div>
  <div class="card" style="margin-bottom:24px"><div class="label">Limão</div>
    <div style="font-size:38px;line-height:1.32">3 col. de azeite + 1 col. de suco de limão + sal e pimenta</div></div>
  <div class="card" style="margin-bottom:24px"><div class="label">Mostarda</div>
    <div style="font-size:38px;line-height:1.32">3 col. de azeite + 1 col. de vinagre + 1 col. (chá) de mostarda</div></div>
  <div class="card"><div class="label">Iogurte</div>
    <div style="font-size:38px;line-height:1.32">3 col. de iogurte natural + 1 col. de limão + ervas e sal</div></div>
  <div class="sub" style="font-size:30px;margin-top:auto">Regue só na hora de comer, pra folha não murchar.</div>
</div>""", None, contador="5/6")))
sal.append(render("2611-salada-6", oferta(
    "Quer pronta?", "<em>36 saladas</em><br>que matam a fome",
    "Já montadas nessa fórmula, com proteína, grãos e molhos, no e-book <b>36 Receitas de Salada</b>.",
    "9,90", "Pix ou cartão · chega no seu e-mail na hora · garantia de 7 dias", "Salve este post<br>pra montar a sua 💚")))
out["salada"] = sal

# ---------- 17:30 CARNE: venda (4 slides) ----------
car = []
car.append(render("2611-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Carne moída de novo?</div>
  <h1 style="font-size:116px">Calma, dá pra<br>variar <em>90 vezes</em></h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto">
    <div class="photo" style="height:340px"><img src="{img(F+'/carne/p021-1.jpg')}"></div>
    <div class="photo" style="height:340px"><img src="{img(F+'/carne/p016-2.jpg')}"></div>
    <div class="photo" style="height:340px"><img src="{img(F+'/carne/p035-1.jpg')}"></div>
    <div class="photo" style="height:340px"><img src="{img(F+'/carne/p004-1.jpg')}"></div>
  </div>
</div>""", "OFERTA", foot=foot_swipe())))
car.append(render("2611-carne-2", page("""
<div class="wrap">
  <h2>10 capítulos <em>+ bônus</em></h2>
  <div class="card"><ul class="list" style="gap:22px">
    <li>Rocamboles e rolinhos</li><li>Quibes e kaftas</li><li>Polpetones e almôndegas</li>
    <li>Escondidinhos e gratinados</li><li>Tortas e empadões</li><li>Salgadinhos e fritos</li>
    <li>Recheados e assados</li><li>Arroz, feijão e caldos</li><li>Massas e lasanhas</li>
    <li>Lanches e tapiocas</li></ul></div>
  <div class="sub" style="font-size:32px;margin-top:auto">Do almoço de domingo ao lanche da noite.</div>
</div>""", None, contador="2/4")))
car.append(render("2611-carne-3", page(f"""
<div class="wrap">
  <h2>Cada receita com <em>tempo</em> e passo a passo</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto">
    <div><div class="photo" style="height:330px"><img src="{img(F+'/carne/p010-1.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:14px">Quibe frito</div></div>
    <div><div class="photo" style="height:330px"><img src="{img(F+'/carne/p027-2.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:14px">Torta de carne</div></div>
    <div><div class="photo" style="height:330px"><img src="{img(F+'/carne/p049-2.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:14px">Panqueca</div></div>
    <div><div class="photo" style="height:330px"><img src="{img(F+'/carne/p043-1.jpg')}"></div><div class="pill" style="display:inline-block;margin-top:14px">Arroz carreteiro</div></div>
  </div>
</div>""", None, contador="3/4")))
car.append(render("2611-carne-4", oferta(
    "E-book em PDF", "<em>Carne Moída:</em><br>90 Receitas",
    "Pra variar o cardápio da semana sem gastar mais no mercado.",
    "19,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e mande pra<br>quem cozinha aí 💚")))
out["carne"] = car

# ---------- 19:30 NATAL: peru, chester ou pernil (post único) ----------
def opc(n, nome, foto):
    return f'<div><div class="photo" style="height:520px"><img src="{img(F+foto)}"></div><div class="pill" style="display:inline-block;margin-top:16px">{n} · {nome}</div></div>'

nat = [render("2611-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Faltam 28 dias</div>
  <h1 style="font-size:112px">Peru, chester<br>ou <em>pernil?</em></h1>
  <div class="sub">Qual desses não pode faltar na sua ceia?</div>
  <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px;margin-top:auto;margin-bottom:50px">
    {opc(1, "Peru", "/natal/p031-0.jpg")}{opc(2, "Chester", "/natal/p032-0.jpg")}{opc(3, "Pernil", "/natal/p037-0.jpg")}
  </div>
</div>
<div class="foot" style="bottom:52px"><span></span><span>Comenta 1, 2 ou 3 👇</span></div>
""", "NATAL"))]
out["natal"] = nat

# ---------- 21:00 SOBREMESAS: Pudim de coco (Reels -> carrossel 5) ----------
sob = []
sob.append(render("2611-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Doce sem açúcar que parece de padaria?</div>
  <h1 style="font-size:84px">Olha só:</h1>
  <h1 style="font-size:128px;margin-top:6px;white-space:nowrap"><em>Pudim de coco</em></h1>
  <div class="pills"><span class="pill">Zero açúcar</span><span class="pill">Sem glúten</span><span class="pill">De liquidificador</span></div>
  <div class="photo" style="width:720px;height:690px;margin:auto auto 0"><img src="{img(PUDIM)}"></div>
</div>""", "ZERO AÇÚCAR", foot=foot_swipe())))
sob.append(render("2611-sobremesas-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Calda</div><ul class="list" style="gap:12px">
    <li>½ xícara de xilitol</li><li>¼ de xícara de água</li></ul></div>
  <div class="card"><div class="label">Pudim</div><ul class="list" style="gap:12px">
    <li>4 ovos</li><li>1 vidro de leite de coco (200 ml)</li><li>1 xícara (240 ml) de leite</li>
    <li>½ xícara de leite em pó</li><li>½ xícara de xilitol ou eritritol</li>
    <li>50 g de coco ralado sem açúcar</li></ul></div>
  <div class="pills" style="margin-top:auto"><span class="pill">Forma de 20 cm com furo</span><span class="pill">8 fatias</span></div>
</div>""", None, contador="2/5")))
sob.append(render("2611-sobremesas-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Calda: leve o xilitol e a água ao fogo baixo, sem mexer, até dourar. Espalhe na forma.</li>
    <li>Bata no liquidificador os ovos, os leites, o leite em pó e o adoçante por 1 minuto. Junte o coco e só misture.</li>
    <li>Despeje na forma, cubra com papel-alumínio e asse em banho-maria a 180 °C por 50 a 60 min.</li>
    <li>Espere esfriar, leve à geladeira por 4 horas e desenforme.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Pra servir</div>
    <div style="font-size:38px;line-height:1.32">Finalize com coco ralado sem açúcar levemente tostado por cima. Fica com cara de vitrine.</div></div>
</div>""", None, contador="3/5")))
sob.append(render("2611-sobremesas-4", page("""
<div class="wrap">
  <h2>Truques de <em>padaria</em></h2>
  <div class="card" style="margin-bottom:26px"><div class="label">Sem furinhos</div>
    <div style="font-size:38px;line-height:1.32">Bata pouco e deixe a mistura descansar 5 min antes de assar. Tire a espuma de cima.</div></div>
  <div class="card" style="margin-bottom:26px"><div class="label">Ponto certo</div>
    <div style="font-size:38px;line-height:1.32">Espete um palito perto da borda: se sair limpo, está pronto. O centro firma na geladeira.</div></div>
  <div class="card"><div class="label">Atenção</div>
    <div style="font-size:38px;line-height:1.32">Confira no rótulo do leite em pó e do coco ralado o aviso “não contém glúten”.</div></div>
</div>""", None, contador="4/5")))
sob.append(render("2611-sobremesas-5", oferta(
    "Gostou?", "<em>200 sobremesas</em><br>zero açúcar",
    "Todas sem glúten, no e-book <b>Sobremesas de Domingo – Versão Zero</b>.",
    "24,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e marque quem<br>ama um docinho 💚")))
out["sobremesas"] = sob

import json
json.dump(out, open(f"{OUT}/2611.json", "w"), indent=1)
print(json.dumps(out, indent=1))

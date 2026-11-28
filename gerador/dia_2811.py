import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from artes import *
from PIL import Image

F = FOTOS + '/fotos'
out = {}

# Foto do brownie recheado (pequena): recorte centralizado, usada em tamanho moderado
BROWNIE = f"{OUT}/brownie-crop.jpg"
Image.open(F + '/sobremesas/p003-1.jpg').crop((20, 20, 280, 250)).save(BROWNIE, quality=95)


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


def foto_nome(foto, nome, h=330):
    return (f'<div><div class="photo" style="height:{h}px"><img src="{img(F + foto)}"></div>'
            f'<div class="pill" style="display:inline-block;margin-top:14px">{nome}</div></div>')


# ---------- 11:00 SALADA: venda (4 slides) ----------
sal = []
sal.append(render("2811-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">Mesma salada todo dia?</div>
  <h1 style="font-size:112px">Cansado de<br>comer <em>a mesma<br>salada?</em></h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto">
    <div class="photo" style="height:330px"><img src="{img(F+'/salada/p018-0.jpg')}"></div>
    <div class="photo" style="height:330px"><img src="{img(F+'/salada/p024-0.jpg')}"></div>
    <div class="photo" style="height:330px"><img src="{img(F+'/salada/p030-0.jpg')}"></div>
    <div class="photo" style="height:330px"><img src="{img(F+'/salada/p021-0.jpg')}"></div>
  </div>
</div>""", "OFERTA", foot=foot_swipe())))
sal.append(render("2811-salada-2", page("""
<div class="wrap">
  <h2>36 saladas, <em>zero tédio</em></h2>
  <div class="sub" style="margin:0 0 34px">Algumas que estão no e-book:</div>
  <div class="card" style="padding:44px 44px"><ul class="list" style="gap:30px">
    <li>Salada de Frango e Abacate</li><li>Salada de Abóbora Assada</li><li>Salpicão Fit</li>
    <li>Salada Proteica de Grão-de-bico</li><li>Salada de Brócolis com Lentilha</li>
    <li>Salada Waldorf</li><li>Salada Grega</li><li>Salada de Manga</li></ul></div>
  <div class="sub" style="font-size:32px;margin-top:auto">E ainda chips de batata-doce e crouton de frigideira.</div>
</div>""", None, contador="2/4")))
sal.append(render("2811-salada-3", page(f"""
<div class="wrap">
  <h2>Salada que vira <em>refeição</em></h2>
  <div class="sub" style="margin:0 0 30px">Com proteína, grãos e molhos caseiros.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:22px;margin-top:auto">
    {foto_nome('/salada/p006-0.jpg', 'Abóbora assada', 320)}{foto_nome('/salada/p025-0.jpg', 'Rúcula caprese', 320)}
    {foto_nome('/salada/p032-0.jpg', 'Tropical', 320)}{foto_nome('/salada/p028-0.jpg', 'Feijão-preto', 320)}
  </div>
</div>""", None, contador="3/4")))
sal.append(render("2811-salada-4", oferta(
    "E-book em PDF", "<em>36 Receitas</em><br>de Salada",
    "Pra sair do alface com tomate e montar pratos que matam a fome de verdade.",
    "9,90", "Pix ou cartão · chega no seu e-mail na hora · garantia de 7 dias", "Salve e mande pra<br>quem vive de salada 💚")))
out["salada"] = sal

# ---------- 17:30 CARNE: engajamento (post único) ----------
car = [render("2811-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Conta pra gente</div>
  <h1 style="font-size:104px">Qual é a receita<br>de carne moída<br>da <em>sua casa?</em></h1>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px 22px;margin-top:auto;margin-bottom:50px">
    {foto_nome('/carne/p021-1.jpg', '1 · Escondidinho', 260)}{foto_nome('/carne/p016-2.jpg', '2 · Almôndegas', 260)}
    {foto_nome('/carne/p010-1.jpg', '3 · Quibe', 260)}{foto_nome('/carne/p004-1.jpg', '4 · Rocambole', 260)}
  </div>
</div>
<div class="foot" style="bottom:52px"><span>Ou escreve a sua!</span><span>Comenta 1, 2, 3 ou 4 👇</span></div>
""", "ENQUETE"))]
out["carne"] = car

# ---------- 19:30 NATAL: Farofa especial de Natal (Reels -> carrossel 5) ----------
nat = []
nat.append(render("2811-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Faltam 27 dias</div>
  <div class="sub" style="margin:0 0 14px;font-size:38px">Esse vai ser o prato mais elogiado da ceia:</div>
  <h1 style="font-size:124px">Farofa<br><em>especial</em> de Natal</h1>
  <div class="photo" style="width:100%;height:540px;margin-top:auto"><img src="{img(F+'/natal/p059-0.jpg')}"></div>
</div>""", "NATAL", foot=foot_swipe())))
nat.append(render("2811-natal-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="padding:44px 44px"><ul class="list" style="gap:28px">
    <li>150 g de bacon em cubinhos</li><li>3 colheres (sopa) de manteiga</li>
    <li>1 cebola picada e 2 dentes de alho</li><li>½ xícara de damasco seco picado</li>
    <li>½ xícara de uva-passa</li><li>½ xícara de castanha de caju picada</li>
    <li>2 xícaras de farinha de mandioca flocada</li><li>Sal e salsinha picada</li></ul></div>
  <div class="pills" style="margin-top:auto"><span class="pill">Serve 10 pessoas</span><span class="pill">Cerca de 25 min</span></div>
</div>""", None, contador="2/5")))
nat.append(render("2811-natal-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Frite o bacon em fogo médio até dourar. Tire um pouco da gordura, deixe só 2 colheres na panela.</li>
    <li>Junte a manteiga, a cebola e o alho e refogue até a cebola ficar macia.</li>
    <li>Coloque o damasco, a uva-passa e a castanha e mexa por 2 minutos.</li>
    <li>Abaixe o fogo e junte a farinha aos poucos, mexendo por 5 a 8 min, até ficar soltinha e dourada. Acerte o sal e finalize com salsinha.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Segredo</div>
    <div style="font-size:38px;line-height:1.32">Fogo baixo e paciência: a farinha torra por igual e não fica com gosto de crua.</div></div>
</div>""", None, contador="3/5")))
nat.append(render("2811-natal-4", page("""
<div class="wrap">
  <h2>Truques de <em>ceia</em></h2>
  <div class="card" style="margin-bottom:26px"><div class="label">Adiante</div>
    <div style="font-size:40px;line-height:1.32">Faça até 2 dias antes e guarde em pote fechado na geladeira. No dia, é só aquecer na frigideira.</div></div>
  <div class="card" style="margin-bottom:26px"><div class="label">Sem bacon</div>
    <div style="font-size:40px;line-height:1.32">Troque por calabresa em cubos ou dobre a castanha e a manteiga.</div></div>
  <div class="card"><div class="label">Sirva com</div>
    <div style="font-size:40px;line-height:1.32">Peru, chester, pernil ou tender. Combina com todos.</div></div>
</div>""", None, contador="4/5")))
nat.append(render("2811-natal-5", oferta(
    "E-book em PDF", "<em>100 Receitas</em><br>Natalinas",
    "Farofas, arrozes, carnes, saladas e sobremesas: a ceia inteira planejada num só PDF.",
    "19,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Marque quem faz<br>a farofa aí 💚")))
out["natal"] = nat

# ---------- 21:00 SOBREMESAS: Brownie recheado fit (carrossel receita, 4) ----------
sob = []
sob.append(render("2811-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Passo a passo</div>
  <h1 style="font-size:124px"><em>Brownie</em><br>recheado fit</h1>
  <div class="pills"><span class="pill">Zero açúcar</span><span class="pill">Sem glúten</span><span class="pill">12 pedaços</span></div>
  <div class="photo" style="width:620px;height:550px;margin:auto auto 0"><img src="{img(BROWNIE)}"></div>
</div>""", "ZERO AÇÚCAR", foot=foot_swipe())))
sob.append(render("2811-sobremesas-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Massa</div><ul class="list" style="gap:10px">
    <li>3 ovos</li><li>½ xícara de xilitol</li><li>⅓ de xícara de óleo de coco derretido</li>
    <li>½ xícara de cacau em pó 100%</li><li>1 xícara de farinha de amêndoas</li>
    <li>1 colher (chá) de fermento e 1 pitada de sal</li></ul></div>
  <div class="card"><div class="label">Recheio cremoso</div><ul class="list" style="gap:10px">
    <li>1 xícara de leite em pó</li><li>½ caixinha de creme de leite (100 g)</li>
    <li>2 colheres (sopa) de xilitol</li></ul></div>
  <div class="pills" style="margin-top:auto"><span class="pill">Forma 20 x 20 cm</span></div>
</div>""", None, contador="2/4")))
sob.append(render("2811-sobremesas-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:28px">
    <li>Recheio: misture o leite em pó, o creme de leite e o xilitol até virar um creme liso. Reserve.</li>
    <li>Bata os ovos com o xilitol por 2 min. Junte o óleo de coco e o cacau e misture.</li>
    <li>Acrescente a farinha de amêndoas, o sal e, por último, o fermento.</li>
    <li>Metade da massa na forma untada, o recheio por cima e o resto da massa cobrindo. Asse a 180 °C por 25 a 30 min.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Ponto certo</div>
    <div style="font-size:36px;line-height:1.32">O centro sai úmido mesmo. Espere 1 hora antes de cortar e confira “não contém glúten” no rótulo do cacau e do leite em pó.</div></div>
</div>""", None, contador="3/4")))
sob.append(render("2811-sobremesas-4", oferta(
    "Gostou?", "<em>200 sobremesas</em><br>zero açúcar",
    "Todas sem glúten, no e-book <b>Sobremesas de Domingo – Versão Zero</b>.",
    "24,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e marque quem<br>ama um docinho 💚")))
out["sobremesas"] = sob

import json
json.dump(out, open(f"{OUT}/2811.json", "w"), indent=1)
print(json.dumps(out, indent=1))

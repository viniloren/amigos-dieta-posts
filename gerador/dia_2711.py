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


def dica(nome, n, total, titulo, sub, label, itens, label2, texto2):
    lis = "".join(f"<li>{i}</li>" for i in itens)
    return render(nome, page(f"""
<div class="wrap" style="justify-content:center;padding-bottom:40px">
  <h2 style="font-size:120px">{titulo}</h2>
  <div class="sub" style="margin:0 0 44px">{sub}</div>
  <div class="card"><div class="label">{label}</div><ul class="list">{lis}</ul></div>
  <div class="card" style="margin-top:36px"><div class="label">{label2}</div>
    <div style="font-size:38px;line-height:1.32">{texto2}</div></div>
</div>""", None, contador=f"{n}/{total}"))


# ---------- 11:00 SALADA: Abóbora assada com gorgonzola (carrossel receita, 4) ----------
sal = []
sal.append(render("2711-salada-1", page(f"""
<div class="wrap">
  <div class="kicker">Passo a passo</div>
  <h1 style="font-size:120px">Salada de<br><em>abóbora assada</em><br>com gorgonzola</h1>
  <div class="sub">Doce, salgada e crocante no mesmo prato.</div>
  <div style="display:flex;gap:34px;align-items:flex-end;margin-top:auto">
    <div class="photo" style="width:470px;height:570px"><img src="{img(F+'/salada/p006-0.jpg')}"></div>
    <div class="pills" style="flex-direction:column;align-items:flex-start;margin:0 0 20px">
      <span class="pill">Abóbora no forno</span><span class="pill">Nozes crocantes</span><span class="pill">2 porções</span>
    </div>
  </div>
</div>""", "RECEITA", foot=foot_swipe())))
sal.append(render("2711-salada-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Para a salada</div><ul class="list" style="gap:12px">
    <li>500 g de abóbora cabotiá em cubos (com casca)</li><li>2 colheres (sopa) de azeite</li>
    <li>Sal, pimenta e 1 ramo de alecrim</li><li>2 xícaras de rúcula</li>
    <li>80 g de gorgonzola esfarelado</li><li>⅓ de xícara de nozes picadas</li></ul></div>
  <div class="card"><div class="label">Para o molho</div><ul class="list" style="gap:12px">
    <li>2 colheres (sopa) de azeite</li><li>1 colher (sopa) de vinagre balsâmico</li>
    <li>1 colher (chá) de mel e uma pitada de sal</li></ul></div>
</div>""", None, contador="2/4")))
sal.append(render("2711-salada-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Misture a abóbora com azeite, sal, pimenta e alecrim. Espalhe na assadeira sem amontoar.</li>
    <li>Asse a 200 °C por 30 a 35 min, virando na metade, até dourar e ficar macia.</li>
    <li>Toste as nozes na frigideira seca por 2 a 3 min, mexendo.</li>
    <li>Monte a rúcula, a abóbora ainda morna, o gorgonzola e as nozes. Regue com o molho na hora de servir.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Dica</div>
    <div style="font-size:38px;line-height:1.32">Não curte gorgonzola? Troque por queijo de cabra ou ricota temperada.</div></div>
</div>""", None, contador="3/4")))
sal.append(render("2711-salada-4", oferta(
    "Gostou?", "Mais <em>35 saladas</em><br>que matam a fome",
    "Pratos completos, com proteína, grãos e molhos especiais, no e-book <b>36 Receitas de Salada</b>.",
    "9,90", "Pix ou cartão · chega no seu e-mail na hora · garantia de 7 dias", "Salve este post<br>pra fazer depois 💚")))
out["salada"] = sal

# ---------- 17:30 CARNE: Almôndegas ao molho de tomate (Reels -> carrossel 5) ----------
car = []
car.append(render("2711-carne-1", page(f"""
<div class="wrap">
  <div class="kicker">Janta resolvida em 30 min</div>
  <h1 style="font-size:128px"><em>Almôndegas</em><br>ao molho<br>de tomate</h1>
  <div class="photo" style="width:100%;height:560px;margin-top:auto"><img src="{img(F+'/carne/p016-2.jpg')}"></div>
</div>""", "RECEITA", foot=foot_swipe())))
car.append(render("2711-carne-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:24px"><div class="label">Almôndegas</div><ul class="list" style="gap:10px">
    <li>500 g de carne moída (patinho)</li><li>1 ovo</li><li>3 colheres (sopa) de farinha de rosca</li>
    <li>½ cebola ralada e 1 dente de alho</li><li>2 colheres (sopa) de parmesão ralado</li><li>Sal, pimenta e salsinha</li></ul></div>
  <div class="card"><div class="label">Molho</div><ul class="list" style="gap:10px">
    <li>1 colher (sopa) de azeite e 1 dente de alho</li><li>500 g de passata ou tomate pelado</li>
    <li>½ xícara de água, sal e manjericão</li></ul></div>
</div>""", None, contador="2/5")))
car.append(render("2711-carne-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:30px">
    <li>Misture os ingredientes das almôndegas só até unir. Faça bolinhas de 3 cm (rende umas 20).</li>
    <li>Doure numa frigideira com fio de azeite por 5 min, girando para dourar por igual.</li>
    <li>Na panela, refogue o alho, junte o tomate, a água e o sal e deixe ferver.</li>
    <li>Coloque as almôndegas no molho, tampe e cozinhe em fogo baixo por 15 min. Finalize com manjericão.</li>
  </ol>
  <div class="pills" style="margin-top:auto"><span class="pill">Serve 4 pessoas</span><span class="pill">Cerca de 30 min</span></div>
</div>""", None, contador="3/5")))
car.append(render("2711-carne-4", page("""
<div class="wrap">
  <h2>Truques pra <em>não desmanchar</em></h2>
  <div class="card" style="margin-bottom:26px"><div class="label">Não sove</div>
    <div style="font-size:40px;line-height:1.32">Misture só até a massa unir. Mexer demais deixa a almôndega dura.</div></div>
  <div class="card" style="margin-bottom:26px"><div class="label">Mãos molhadas</div>
    <div style="font-size:40px;line-height:1.32">Molhe as mãos para enrolar: a massa não gruda e as bolinhas ficam lisinhas.</div></div>
  <div class="card"><div class="label">Sirva com</div>
    <div style="font-size:40px;line-height:1.32">Arroz, macarrão, purê ou no pão, tipo sanduíche.</div></div>
</div>""", None, contador="4/5")))
car.append(render("2711-carne-5", oferta(
    "E amanhã?", "<em>90 receitas</em><br>com carne moída",
    "Almôndegas, escondidinhos, rocamboles, quibes, tortas e lanches no e-book <b>Carne Moída: 90 Receitas</b>.",
    "19,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e mande pra<br>quem cozinha aí 💚")))
out["carne"] = car

# ---------- 19:30 NATAL: Salpicão natalino tradicional (carrossel receita, 4) ----------
nat = []
nat.append(render("2711-natal-1", page(f"""
<div class="wrap">
  <div class="kicker">Faltam 28 dias · passo a passo</div>
  <h1 style="font-size:124px">Salpicão<br><em>natalino</em><br>tradicional</h1>
  <div class="photo" style="width:100%;height:540px;margin-top:auto"><img src="{img(F+'/natal/p018-0.jpg')}"></div>
</div>""", "NATAL", foot=foot_swipe())))
nat.append(render("2711-natal-2", page("""
<div class="wrap">
  <h2>O que você <em>vai usar</em></h2>
  <div class="card" style="margin-bottom:22px"><ul class="list" style="gap:10px">
    <li>800 g de peito de frango</li><li>2 cenouras raladas</li>
    <li>1 lata de milho e 1 de ervilha, escorridos</li><li>½ xícara de uva-passa</li>
    <li>1 maçã verde em cubinhos</li><li>Cheiro-verde picado</li></ul></div>
  <div class="card"><div class="label">Molho e final</div><ul class="list" style="gap:10px">
    <li>1 xícara de maionese</li><li>½ caixinha de creme de leite</li>
    <li>Suco de ½ limão, sal e pimenta</li><li>100 g de batata palha</li></ul></div>
  <div class="pills" style="margin-top:auto"><span class="pill">Serve 10 pessoas</span></div>
</div>""", None, contador="2/4")))
nat.append(render("2711-natal-3", page("""
<div class="wrap">
  <h2>Modo de <em>preparo</em></h2>
  <ol class="steps" style="gap:28px">
    <li>Cozinhe o frango em água com sal, cebola e louro por 25 min. Deixe amornar e desfie.</li>
    <li>Junte o frango, a cenoura, o milho, a ervilha, a uva-passa e a maçã (regada com limão pra não escurecer).</li>
    <li>Misture a maionese, o creme de leite, o limão, sal e pimenta e envolva tudo. Finalize com cheiro-verde.</li>
    <li>Leve à geladeira por 1 hora. A batata palha vai por cima só na hora de servir.</li>
  </ol>
  <div class="card" style="margin-top:auto"><div class="label">Adiante a ceia</div>
    <div style="font-size:38px;line-height:1.32">Dá pra fazer na véspera e guardar coberto na geladeira. Só não coloque a batata palha antes.</div></div>
</div>""", None, contador="3/4")))
nat.append(render("2711-natal-4", oferta(
    "E-book em PDF", "<em>100 Receitas</em><br>Natalinas",
    "Entradas, saladas, carnes, farofas e sobremesas: planeje a ceia inteira hoje e chegue no dia 24 sem estresse.",
    "19,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Marque quem faz<br>a ceia aí 💚")))
out["natal"] = nat

# ---------- 21:00 SOBREMESAS: 3 trocas para adoçar sem açúcar (carrossel dica, 5) ----------
sob = []
sob.append(render("2711-sobremesas-1", page(f"""
<div class="wrap">
  <div class="kicker">Doce sem açúcar</div>
  <h1 style="font-size:132px"><em>3 trocas</em><br>pra adoçar<br>sem açúcar</h1>
  <div class="sub">E em qual receita usar cada uma.</div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:auto">
    <div class="photo" style="height:470px"><img src="{img(F+'/sobremesas/p027-0.jpg')}"></div>
    <div class="photo" style="height:470px"><img src="{img(F+'/sobremesas/p111-0.jpg')}"></div>
  </div>
</div>""", "DICA", foot=foot_swipe())))
sob.append(dica("2711-sobremesas-2", 2, 5, "1. <em>Xilitol</em>",
                "Troca na mesma medida do açúcar e não deixa gosto residual.",
                "Use em", ["Brigadeiro e doces de panela", "Caldas e calda de pudim", "Mousses e cremes", "Sorvetes caseiros"],
                "Atenção", "Guarde longe do cachorro: xilitol faz mal para cães."))
sob.append(dica("2711-sobremesas-3", 3, 5, "2. <em>Eritritol</em>",
                "Adoça um pouco menos que o açúcar (cerca de 70%).",
                "Use em", ["Bolos e muffins", "Cookies e massas assadas", "Biscoitos amanteigados", "Misturas prontas com stevia"],
                "Medida", "Para 1 xícara de açúcar, use cerca de 1 xícara e ⅓ de eritritol puro. Em cremes gelados ele pode cristalizar."))
sob.append(dica("2711-sobremesas-4", 4, 5, "3. <em>Fruta madura</em>",
                "Banana, maçã ou purê de fruta dão doçura e umidade à massa.",
                "Use em", ["Bolos e panquecas", "Muffins de liquidificador", "Sorvete de banana", "Bolo de caneca"],
                "Truque", "Banana bem madura, com pintinhas, é a mais doce. Com purê de fruta, reduza um pouco o líquido."))
sob.append(render("2711-sobremesas-5", oferta(
    "Quer pronta?", "<em>200 sobremesas</em><br>zero açúcar",
    "Todas sem glúten e com as medidas certas, no e-book <b>Sobremesas de Domingo – Versão Zero</b>.",
    "24,90", "Pix ou cartão · chega no e-mail na hora · garantia de 7 dias", "Salve e marque quem<br>ama um docinho 💚")))
out["sobremesas"] = sob

import json
json.dump(out, open(f"{OUT}/2711.json", "w"), indent=1)
print(json.dumps(out, indent=1))

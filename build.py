import json
from pathlib import Path

FIM = "2026-11-29T23:59:59-03:00"
FIM_TXT = "domingo, 29/11, às 23h59"
S = "../img/stock/"
P = "../img/"

RACAO = {"n": "Ração Golden Special Cães Adultos 15 kg", "d": "Sabor frango e carne", "de": 289.9, "por": 199.9, "img": P + "racao.jpg", "alt": "Pacote de ração Golden Special 15 kg", "tipo": "Produto"}
AREIA = {"n": "Areia Pipicat Multi-Cat 12 kg", "d": "Grãos extrafinos, torrões firmes", "de": 59.9, "por": 39.9, "img": P + "areia.jpg", "alt": "Pacote de areia Pipicat 12 kg", "tipo": "Produto"}
CAMA = {"n": "Cama Redonda Xadrez Azul", "d": "Tecido lavável, para cães e gatos", "de": 149.9, "por": 89.9, "img": P + "caminha.jpg", "alt": "Cama redonda azul com borda xadrez", "tipo": "Produto"}
BIFINHO = {"n": "Kit 3 Bifinhos Origem Natural Cordeiro", "d": "3 pacotes de 60 g", "de": 69.9, "por": 44.9, "img": P + "petiscos.jpg", "alt": "Pacote de bifinho sabor cordeiro", "tipo": "Produto"}

def svc(n, d, de, por, img, alt):
    return {"n": n, "d": d, "de": de, "por": por, "img": img, "alt": alt, "tipo": "Serviço"}

LOJAS = {
    "metropole": dict(
        cores=dict(BRAND="#00807a", BRANDINK="#ffffff", ACCENT="#cc3366", ACCENTINK="#ffffff", PRICE="#cc3366", TINT="#e9f5f8"),
        cfg=dict(
            nome="Metrópole Pet Shop", whatsapp="5511992594990", fim=FIM, fimTexto=FIM_TXT,
            nota={"valor": "4,8", "total": "193"},
            depoimentos=[["Um lugar de confiança. Ambiente muito agradável. Ótimo atendimento.", "Valentina Pedroso"], ["Ótimo atendimento! Super atenciosos e carinhosos. Meu pet adora ir lá.", "Joyce"]],
            logo="img/logo.png",
            lede="Banho, tosa, consultas e produtos com desconto. Reserve pelo WhatsApp.",
            hero={"src": "img/hero.jpg", "alt": "Veterinária da Metrópole em frente ao logo da clínica", "pos": "70% 35%"},
            strip={"src": S + "tutora-beagle.jpg", "alt": "Tutora sorrindo com seu beagle", "titulo": "Clínica e estética na Vila Leopoldina"},
            info=[["Onde", "Rua Carlos Weber, 608, Vila Leopoldina, com estacionamento"], ["Horário", "Segunda a sábado, das 9h às 18h"], ["Agendamento", "Consultas e banhos com horário marcado pelo WhatsApp"]],
            ofertas=[
                svc("Banho + Hidratação", "Porte pequeno, sala climatizada", 120, 89.9, "img/sala.jpg", "Sala de banho e tosa da Metrópole"),
                svc("Tosa Completa", "Com tosadores formados em estética", 160, 119.9, "img/tesouras.jpg", "Tesouras de tosa na sala de estética"),
                svc("Pacote 4 Banhos no Mês", "Banhos semanais com um serviço de cortesia", 400, 319.9, S + "familia-banho.jpg", "Família dando banho no cachorro"),
                svc("Consulta Clínica Geral", "Com horário marcado", 220, 179.9, S + "tutora-cacheada.jpg", "Tutora sorrindo com seu cachorro"),
                RACAO, AREIA,
            ],
        ),
    ),
    "clinicanis": dict(
        cores=dict(BRAND="#6b1014", BRANDINK="#ffffff", ACCENT="#f0a07c", ACCENTINK="#3a0a0c", PRICE="#6b1014", TINT="#fbf1ec"),
        cfg=dict(
            nome="Clinicanis", whatsapp="551136443111", fim=FIM, fimTexto=FIM_TXT,
            nota={"valor": "4,8", "total": "315"},
            logo=None,
            lede="Estética, veterinário, day care e loja com desconto. Reserve pelo WhatsApp.",
            hero={"src": "img/fachada.jpg", "alt": "Fachada da Clinicanis na Rua Pio XI", "pos": "62% 40%"},
            strip={"src": S + "tutora-cacheada.jpg", "alt": "Tutora sorrindo com seu cachorro", "titulo": "Há 30 anos no Alto da Lapa"},
            info=[["Onde", "Rua Pio XI, 143, Alto da Lapa"], ["Leva e traz", "Buscamos e levamos seu pet com segurança"], ["Tudo num lugar só", "Veterinária, estética, loja e creche"]],
            ofertas=[
                svc("Banho e Tosa", "Estética assinada pela groomer Simone Garotti", 150, 119.9, "img/estetica.jpg", "Banho e tosa na Clinicanis"),
                svc("Consulta Veterinária", "Diagnóstico com a equipe da casa", 200, 159.9, "img/vet.jpg", "Consultório veterinário da Clinicanis"),
                svc("Diária de Day Care", "Atividades físicas e novos amiguinhos", 95, 69.9, S + "filhote.jpg", "Filhote feliz na grama"),
                svc("Banho + Leva e Traz", "A gente busca e devolve em casa", 140, 99.9, S + "tutora-labrador.jpg", "Tutora abraçando seu labrador"),
                RACAO, CAMA,
            ],
        ),
    ),
    "petclube": dict(
        cores=dict(BRAND="#3d3b33", BRANDINK="#ffffff", ACCENT="#e8d21f", ACCENTINK="#2b2a22", PRICE="#d9720f", TINT="#fbf7e3"),
        cfg=dict(
            nome="Petclube Experience", whatsapp="551145080044", fim=FIM, fimTexto=FIM_TXT,
            nota={"valor": "4,8", "total": "219"},
            logo="img/logo.png",
            lede="Daycare, hotel, banho e tosa e pet store com desconto. Reserve pelo WhatsApp.",
            hero={"src": S + "tutora-labrador.jpg", "alt": "Tutora abraçando seu labrador", "pos": "50% 40%"},
            strip={"src": S + "tutora-gatinho.jpg", "alt": "Tutora com um gatinho no colo", "titulo": "Um clube pro seu pet no Alto da Lapa"},
            info=[["Onde", "Rua Pio XI, 764, Alto da Lapa"], ["Horário", "Segunda a sábado, das 8h às 20h. Domingo, das 10h às 16h"], ["Tudo num lugar só", "Daycare, hotel, clínica, banho e tosa e pet store"]],
            ofertas=[
                svc("Diária de Daycare", "Brincadeira e cuidado o dia todo", 110, 79.9, S + "filhote.jpg", "Filhote feliz na grama"),
                svc("Pacote 10 Diárias de Daycare", "Pra usar quando precisar", 990, 749.9, S + "tutora-beagle.jpg", "Tutora sorrindo com seu beagle"),
                svc("Diária de Hotel", "Cães e gatos, com notícias pelo WhatsApp", 140, 109.9, S + "gato-manta.jpg", "Gato espiando debaixo da manta"),
                svc("Banho e Tosa", "Porte pequeno", 120, 89.9, P + "banho.jpg", "Cachorro sendo secado com luva de banho"),
                svc("Consulta Veterinária", "Com a equipe da clínica", 200, 159.9, S + "tutor-gato.jpg", "Tutor sorrindo com o gato no colo"),
                RACAO,
            ],
        ),
    ),
    "vet-leopoldina": dict(
        cores=dict(BRAND="#0e8f88", BRANDINK="#ffffff", ACCENT="#ffd23f", ACCENTINK="#1d1d1d", PRICE="#0e8f88", TINT="#e8f8f6"),
        cfg=dict(
            nome="Vet Leopoldina", whatsapp="5511996136804", fim=FIM, fimTexto=FIM_TXT,
            logo="img/logo.png",
            lede="Vacinas, consultas e produtos com desconto. Agende pelo WhatsApp.",
            hero={"src": S + "tutora-beagle.jpg", "alt": "Tutora sorrindo com seu beagle", "pos": "60% 40%"},
            strip={"src": S + "tutora-gatinho.jpg", "alt": "Tutora com um gatinho no colo", "titulo": "Clínica e pet shop na Vila Leopoldina"},
            info=[["Onde", "Rua Guaipá, 370, Vila Leopoldina"], ["Horário", "Segunda a sábado, das 10h às 19h"], ["Vacinas e consultas", "Com o Dr. José Alcides e equipe, com horário marcado"]],
            ofertas=[
                svc("Vacina V10 para Cães", "Aplicada pelo veterinário", 120, 89.9, S + "filhote.jpg", "Filhote feliz na grama"),
                svc("Consulta com Dr. José Alcides", "Com horário marcado", 180, 139.9, S + "tutora-cacheada.jpg", "Tutora sorrindo com seu cachorro"),
                RACAO, AREIA, BIFINHO, CAMA,
            ],
        ),
    ),
}

tpl = Path("template.html").read_text()
for slug, l in LOJAS.items():
    html = tpl.replace("__NOME__", l["cfg"]["nome"]).replace("__CONFIG__", json.dumps(l["cfg"], ensure_ascii=False, indent=2))
    for k, v in l["cores"].items():
        html = html.replace("__" + k + "__", v)
    assert "__" not in html.split("<script>")[0] or "__" not in html, slug
    Path(slug).mkdir(exist_ok=True)
    Path(slug, "index.html").write_text(html)
    print(slug, "ok")

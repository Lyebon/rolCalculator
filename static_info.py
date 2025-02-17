caracteristicas = {"fue": 0, "agi": 0, "con": 0, "int": 0, "i": 0, "pre": 0}
bonificador_car = {"fue": 0, "agi": 0, "con": 0, "int": 0,"i": 0, "pre": 0}
habilidades = {"mym":{"sa": 0, "c": 0, "ce": 0, "cm": 0, "co": 0},
                "arma":{"filo": 0, "contundentes": 0, "dos_manos": 0, "arrojadizas": 0,"proyectiles": 0, "asta": 0},
                "generales":{"trepar": 0, "montar": 0, "nadar": 0, "rastrear": 0,},
                "subterfugio":{"emboscar": 0, "asechar_esconderse": 0, "abrir_cerraduras": 0, "desactivar_trampas": 0},
                "magicas":{"leer_runas": 0, "usar_objeto": 0, "sortilegio_dirigido": 0, "sortilegio_base": 0},
                "fisico":{"vida":0, "persepcion": 0},
                "sortilegio":[],
                "idiomas":{},
                "historial": 0,}
resistencias = {"esencia": 0, "canalizacion": 0, "venenos": 0, "enfermedades": 0, "frio": 0, "calor": 0}
secundarias = {}
billetera = {"mm":0, "mo":0, "mp":0, "mb":0, "mc":0, "me":0}
experiencia = {"lvl": 0, "xp": 0, "movimiento": 1}
inventario = {"armas":{}, "objetos magicos":{}, "accesorios":{}, "hierbas y pociones":{}, "armadura":{}}

numero_por_car = {1:-35, 3:-30, 5:-25, 7:-20, 9:-15, 14:-10, 19:-5, 74:0, 89:5, 94:10, 97:15, 99:20, 100:25, 101:30, 102:35}

raza = {3:"hobbit", 8:"umli", 21:"enano", 25:"wose", 75:"humano", 78:"medio elfo", 91:"silvano", 97:"sindar", 100:"noldor"}
raza_humano = {5:"dunedain",10:"rohirrim", 15:"beornida", 20:"bosques", 25:"dorwinrim", 30:"lossoth"
    , 54:"campesino", 78:"burgues", 83:"dunlendino", 86:"este", 89:"haradrim", 92:"corsario", 95:"variag", 100:"numeroniano"}

bonif_raza = {
    "hobbit":{"fue": -20, "agi": 15, "con": 15, "int": 0, "i": -5, "pre": -5},
    "umli": {"fue": 5, "agi": 0, "con": 10, "int": 0, "i": -5, "pre": -5},
    "enano":{"fue": 5,"agi": -5,"con": 15,"int": 0,"i": -5,"pre": -5},
    "wose":{"fue": 0, "agi": 0, "con": 5, "int": 0,"i": 0, "pre": -5},
    "humano":{"fue": 5, "agi": 0, "con": 0, "int": 0,"i": 0, "pre": 0},
    "dunedain":{"fue": 5, "agi": 0, "con": 10, "int": 0,"i": 0, "pre": 5},
    "medio elfo":{"fue": 5, "agi": 5, "con": 5, "int": 0,"i": 0, "pre": 5},
    "silvano": {"fue": 0, "agi": 10, "con": 0, "int": 0,"i": 5, "pre": 5},
    "sindar": {"fue": 0, "agi": 10, "con": 5, "int": 0,"i": 5, "pre": 10},
    "noldor": {"fue": 0, "agi": 15, "con": 10, "int": 5,"i": 5, "pre": 15},
    "medio orco":{"fue": 5, "agi": 0, "con": 5, "int": 0,"i": 0, "pre": -5},
    "orco":{"fue": 5, "agi": -5, "con": 15, "int": -10,"i": -10, "pre": -10},
    "uruk-hai":{"fue": 10, "agi": 0, "con": 20, "int": 0,"i": -5, "pre": -10},
    "medio troll": {"fue": 10, "agi": -5, "con": 10, "int": -5,"i": -5, "pre": -5},
    "troll":{"fue": 15, "agi": -10, "con": 15, "int": -15,"i": -15, "pre": -10},
    "olog-hai":{"fue": 20, "agi": -5, "con": 15, "int": -5,"i": -10, "pre": -10}
}

resistencia = {
        "hobbit":[50,20,30,15,0,0],
        "umli":[20,0,5,5,0,0],
        "enano":[40,0,10,10,0,0],
        "wose":[20,0,0,0,0,0],
        "humano":[0,0,0,0,0,0],
        "dunedain":[0,0,5,5,0,0],
        "medio elfo":[0,0,5,50,0,0],
        "silvano":[0,0,10,100,0,0],
        "sindar":[0,0,10,100,0,0],
        "noldor":[0,0,10,100,0,0],
        "medio orco":[0,0,10,0,0,0],
        "orco":[0,0,20,5,0,0],
        "uruk-hai":[0,0,20,5,0,0],
        "medio troll":[0,0,15,5,0,0],
        "troll":[0,0,30,10,0,0],
        "olog-hai":[0,0,20,10,0,0]
}

adolescencia = {
    "hobbit":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":0,"contundente":0,"dos_manos":0,"arrojadizas":2,"proyectiles":2,"asta":0,
                                "trepar":2,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":5,"abrir_cerraduras":1,"desactivar_trampas":1,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":4,"sortilegio":0,"idiomas":3,"historial":5},
    "umli":{"sa":1,"c":3,"ce":3,"cm":0,"co":0,
            "filo":0,"contundente":3,"dos_manos":1,"arrojadizas":1,"proyectiles":0,"asta":0,
            "trepar":0,"montar":0,"nadar":1,"rastrear":0,
            "emboscar":0,"asechar_esconderse":1,"abrir_cerraduras":0,"desactivar_trampas":0,
            "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
            "vida":2,"persepcion":1,"sortilegio":5,"idiomas":3,"historial":4},
    "enano":{"sa":1,"c":0,"ce":1,"cm":3,"co":0,
            "filo":0,"contundente":4,"dos_manos":0,"arrojadizas":1,"proyectiles":0,"asta":0,
            "trepar":1,"montar":0,"nadar":0,"rastrear":0,
            "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":1,"desactivar_trampas":1,
            "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
            "vida":3,"persepcion":1,"sortilegio":3,"idiomas":4,"historial":4},
    "wose": {"sa":1,"c":3,"ce":0,"cm":0,"co":0,
             "filo":2,"contundente":0,"dos_manos":0,"arrojadizas":4,"proyectiles":0,"asta":1,
             "trepar":3,"montar":0,"nadar":2,"rastrear":0,
             "embocar":2,"asechar_esconderse":4,"abrir_cerraduras":0,"desactivar_trampas":0,
             "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
             "vida":3,"persepcion":1,"sortilegio":5,"idiomas":2,"historial":5},
    "beornida": {"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                "filo":0,"contundente":0,"dos_manos":1,"arrojadizas":1,"proyectiles":0,"asta":2,
                "trepar":2,"montar":0,"nadar":2,"rastrear":0,
                "emboscar":0,"asechar_esconderse":4,"abrir_cerraduras":0,"desactivar_trampas":0,
                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                "vida":3,"persepcion":1,"sortilegio":3,"idiomas":3,"historial":5},                    
    "numeroniano": {"sa":1,"c":0,"ce":0,"cm":2,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":0,
                                "trepar":0,"montar":1,"nadar":3,"rastrear":1,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":1,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":0,"sortilegio":10,"idiomas":6,"historial":3},
    "corsario": {"sa":1,"c":0,"ce":2,"cm":0,"co":0,
                                "filo":2,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":0,
                                "trepar":0,"montar":0,"nadar":5,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":0,"sortilegio":5,"idiomas":5,"historial":5},
    "dorwinrim": {"sa":1,"c":0,"ce":1,"cm":0,"co":0,
                                "filo":0,"contundente":1,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":1,
                                "trepar":0,"montar":2,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":0,"sortilegio":10,"idiomas":5,"historial":5},
    "dunlendinos": {"sa":1,"c":0,"ce":1,"cm":0,"co":0,
                                "filo":0,"contundente":1,"dos_manos":0,"arrojadizas":2,"proyectiles":1,"asta":2,
                                "trepar":5,"montar":0,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":2,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":3,"persepcion":1,"sortilegio":2,"idiomas":2,"historial":4},
    "este": {"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":2,"asta":2,
                                "trepar":0,"montar":5,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":1,"sortilegio":2,"idiomas":2,"historial":4},
    "haradrim": {"sa":1,"c":1,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":0,"asta":2,
                                "trepar":0,"montar":7,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":1,"sortilegio":2,"idiomas":3,"historial":5},
    "lossoth": {"sa":1,"c":3,"ce":0,"cm":0,"co":0,
                                "filo":0,"contundente":0,"dos_manos":0,"arrojadizas":3,"proyectiles":0,"asta":2,
                                "trepar":0,"montar":0,"nadar":2,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":4,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":3,"persepcion":1,"sortilegio":5,"idiomas":1,"historial":4},
    "rohirrim": {"sa":1,"c":0,"ce":1,"cm":2,"co":0,
                                "filo":2,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":1,"asta":1,
                                "trepar":0,"montar":8,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":3,"persepcion":1,"sortilegio":3,"idiomas":4,"historial":5},
    "campesinos": {"sa":1,"c":1,"ce":1,"cm":1,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":1,
                                "trepar":0,"montar":1,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":1,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":1,"sortilegio":3,"idiomas":4,"historial":5},
    "burgueses": {"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":1,"asta":0,
                                "trepar":0,"montar":0,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":1,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":1,"sortilegio":15,"idiomas":5,"historial":5},
    "variag": {"sa":1,"c":1,"ce":0,"cm":0,"co":0,
                                "filo":2,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":1,
                                "trepar":0,"montar":4,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":1,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":1,"sortilegio":5,"idiomas":3,"historial":4},
    "bosques": {"sa":1,"c":1,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":1,
                                "trepar":3,"montar":0,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":4,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":1,"sortilegio":3,"idiomas":2,"historial":5},
    "dunedain":{"sa":1,"c":0,"ce":1,"cm":2,"co":0,
                                "filo":2,"contundente":0,"dos_manos":1,"arrojadizas":0,"proyectiles":1,"asta":1,
                                "trepar":0,"montar":1,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":1,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":3,"persepcion":0,"sortilegio":10,"idiomas":6,"historial":3},
    "medio elfo":{"sa":1,"c":0,"ce":1,"cm":1,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":2,"asta":0,
                                "trepar":1,"montar":1,"nadar":1,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":2,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":1,"sortilegio":10,"idiomas":4,"historial":3},
    "silvano":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":3,"asta":0,
                                "trepar":2,"montar":1,"nadar":3,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":4,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":3,"sortilegio":20,"idiomas":6,"historial":4},
    "sindar":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":2,"asta":0,
                                "trepar":1,"montar":1,"nadar":2,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":3,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":1,"usar_objeto":1,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":3,"sortilegio":30,"idiomas":8,"historial":3},
    "noldor":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":1,"contundente":0,"dos_manos":0,"arrojadizas":0,"proyectiles":1,"asta":0,
                                "trepar":0,"montar":1,"nadar":2,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":2,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":2,"usar_objeto":1,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":1,"persepcion":3,"sortilegio":40,"idiomas":10,"historial":2},
    "medio orco":{"sa":1,"c":1,"ce":3,"cm":1,"co":0,
                                "filo":0,"contundente":3,"dos_manos":0,"arrojadizas":1,"proyectiles":1,"asta":0,
                                "trepar":1,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":1,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":0,"sortilegio":0,"idiomas":2,"historial":3},
    "orco":{"sa":1,"c":1,"ce":3,"cm":2,"co":0,
                                "filo":0,"contundente":3,"dos_manos":0,"arrojadizas":1,"proyectiles":0,"asta":1,
                                "trepar":1,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":1,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":2,"persepcion":0,"sortilegio":0,"idiomas":2,"historial":2},
    "uruk-hai":{"sa":1,"c":1,"ce":3,"cm":3,"co":0,
                                "filo":4,"contundente":1,"dos_manos":1,"arrojadizas":1,"proyectiles":1,"asta":1,
                                "trepar":1,"montar":1,"nadar":0,"rastrear":0,
                                "emboscar":1,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":3,"persepcion":1,"sortilegio":0,"idiomas":2,"historial":2},
    "medio troll":{"sa":1,"c":1,"ce":2,"cm":3,"co":0,
                                "filo":0,"contundente":0,"dos_manos":4,"arrojadizas":2,"proyectiles":0,"asta":0,
                                "trepar":1,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":1,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":4,"persepcion":0,"sortilegio":0,"idiomas":2,"historial":2},
    "troll":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":0,"contundente":0,"dos_manos":3,"arrojadizas":1,"proyectiles":0,"asta":0,
                                "trepar":1,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":5,"persepcion":0,"sortilegio":0,"idiomas":2,"historial":1},
    "olog-hai":{"sa":1,"c":0,"ce":0,"cm":0,"co":0,
                                "filo":0,"contundente":0,"dos_manos":5,"arrojadizas":2,"proyectiles":0,"asta":0,
                                "trepar":1,"montar":0,"nadar":0,"rastrear":0,
                                "emboscar":0,"asechar_esconderse":0,"abrir_cerraduras":0,"desactivar_trampas":0,
                                "leer_runas":0,"usar_objeto":0,"sortilegio_base":0,"sortilegio_dirigido":0,
                                "vida":5,"persepcion":1,"sortilegio":0,"idiomas":2,"historial":1}
}

player_info = {"id": None, "nombre": None,"familia": None, "estatura": None,
                "peso": None, "genero": None, "edad": None, "pelo": None,
                "ojos": None, "especial Fisico": None, "personalidad": None, "motivacion": None,
                "alineamiento": None, "status": None, "profesion": None, "apariencia": None}
idiomas = []
sortilegios= {}

bonificador_nivel = {
    "explorador":{"arma":1,"generales":1, "subterfugio":2, "fisico":{"persepcion":3}},
    "montaraz": {"arma":2,"generales":3, "fisico":{"persepcion":2}, "subterfugio":{"asechar_esconderse":2}},
    "guerrero": {"arma":3, "generales":1, "fisico":{"vida":2}},
    "bardo": {"arma":1, "generales":1, "subterfugio":1, "magicas":1, "fisico":{"persepcion":1}},
    "mago": {"magico":{"leer_runas":2, "usar_objeto":2, "sortilegio_dirigido":3, "sortilegio_base":2}},
    "animista": {"magico":{"leer_runas":1, "usar_objeto":1,"sortilegio_dirigido":2, "sortilegio_base":2}, "generales":1, "fisico":{"perspcion":1}}
    }

puntos_nivel = {
    "explorador":{"mym":1, "arma":3, "generales":3, "subterfugio":5, "magicas":0, "fisico":2 , "idiomas":1, "sortilegio":0},
    "montaraz":{"mym":2, "arma":3, "generales":4, "subterfugio":2, "magicas":0, "fisico":2 , "idiomas":1, "sortilegio":1},
    "guerrero":{"mym":3, "arma":5, "generales":2, "subterfugio":2, "magicas":0, "fisico":3 , "idiomas":0, "sortilegio":0},
    "bardo":{"mym":0, "arma":2, "generales":2, "subterfugio":2, "magicas":3, "fisico":1 , "idiomas":3, "sortilegio":2},
    "mago":{"mym":0, "arma":0, "generales":2, "subterfugio":0, "magicas":5, "fisico":1 , "idiomas":2, "sortilegio":5},
    "animista":{"mym":1, "arma":1, "generales":2, "subterfugio":1, "magicas":2, "fisico":1 , "idiomas":2, "sortilegio":5},
}

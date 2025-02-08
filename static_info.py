char_info = {
    "characteristicas":{"fue": None, "agi": None, "con": None, "int": None,"i": None, "pre": None},
    "bonificador": {"fue": None, "agi": None, "con": None, "int": None,"i": None, "pre": None},
    "habilidades": {"sa": None, "c": None, "ce": None, "cm": None, "co": None,
                    "filo": None, "contundentes": None, "dos manos": None, "arrojadizas": None,
                    "proyectiles": None, "asta": None, "Trepar": None, "Montar": None, "Nadar": None, "Rastrear": None,
                    "Emboscar": None, "Asechar/Esconderse": None, "Abrir Cerraduras": None, "Desactivar Trampas": None,
                    "Leer Runas": None, "Usar Objeto": None, "Sortilegio Dirigido": None, "Sortilegio Base": None,
                    "fisico":{"Vida": None, "Persepcion": None}, "sortilegio":[], "idiomas":{}, "historial": None,},
    "resistencias":{"Esencia": None, "Canalizacion": None, "Venenos": None, "Enfermedades": None, "Frio": None, "Calor": None},
    "secundarias":{},
    "billetera":["mm", "mo", "mp", "mb", "mc", "me"],
    "experiencia":{"lvl": None, "xp": None, ",movimiento": None},
    "inventario":{"armas":[], "objetos magicos":{}, "accesorios":{}, "hierbas y pociones":{}, "armadura":{}},
}

bonificador_car = {1:-35, 3:-30, 5:-25, 7:-20, 9:-15, 14:-10, 19:-5, 74:0, 89:5, 94:10, 97:15, 99:20, 100:25, 101:30, 102:35}

#adolescencia:
#MyM:SA,C,CE,CM,CO|ARMA:filo,contundente,dos manos,arrojadizas,proyectiles,asta|GENERALES:trepar,montar,nadar,rastrear|
#SUFTERFUGIO:emboscar|asechar/esconderse|abrir cerraduras|desactivar trampas|
#MAGICAS:leer runas|usar objetos|sortilegios dirigidos|sortilegio base|FISICO:desarrollo fisico|persepcion|
#SORTILEGIO%|IDIOMAS|HISTORIAL
raza = {3:"hobbit", 8:"umli", 21:"enano", 25:"wose", 75:{5:"dunedain",10:"rohirrim", 15:"beornida", 20:"bosques", 25:"dorwinrim", 30:"lossoth"
    , 54:"campesino", 78:"burgues", 83:"dunlendino", 86:"este", 89:"haradrim", 92:"corsario", 95:"variag", 100:"numeroniano"},
    78:"medio elfo", 91:"silvano", 97:"sindar", 100:"noldor"}
bonificador_raza = {
    "hobbit": {"bonificador":[-20, 15, 15, 0,-5,-5], "adolescencia":[1,0,0,0,0,0,0,0,2,2,0,2,0,0,0,0,5,1,1,0,0,0,0,2,4,0,3,5],
               "resistencias":[50,20,30,15,0,0]},
    "umli": {"characteristicas":[5,0,10,0,-5,-5],"adolescencia":[1,3,3,0,0,0,3,1,1,0,0,0,0,1,0,0,1,0,0,0,0,0,0,2,1,5,3,4],
             "resistencias":[20,0,5,5,0,0]},
    "enano": {"characteristicas":[5,-5,15,0,-5,-5],"adolescencia":[1,0,1,3,0,0,4,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,3,2,3,4,4],
              "resistencias":[40,0,10,10,0,0]},
    "wose": {"characteristicas":[0,0,5,0,0,-5],"adolescencia":[1,3,0,0,0,2,0,0,4,0,1,3,0,2,0,2,4,0,0,0,0,0,0,3,1,5,2,5],
             "resistencias":[20,0,0,0,0,0]},
    "humano": {"characteristicas":[5,0,0,0,0,0],
               "adolescencia":{"beornida": [1,0,0,0,0,0,0,1,1,0,2,2,0,2,0,0,4,0,0,0,0,0,0,3,1,3,3,5],
                               "numeroniano": [1,0,0,2,0,1,0,0,1,1,0,0,1,3,0,0,0,0,0,1,1,0,0,2,0,10,6,3],
                               "corsario": [1,0,2,0,0,2,0,0,1,1,0,0,0,5,0,0,0,0,0,0,0,0,0,2,0,5,5,5],
                               "dorwinrim": [1,0,1,0,0,0,1,0,1,1,1,0,2,1,0,0,0,0,0,0,0,0,0,1,0,10,5,5],
                               "dunlendinos": [1,0,1,0,0,0,1,0,2,1,2,5,0,1,0,0,2,0,0,0,0,0,0,3,1,2,2,4],
                               "este": [1,0,0,0,0,1,0,0,1,2,2,0,5,0,0,0,0,0,0,0,0,0,0,2,1,2,2,4],
                               "haradrim": [1,1,0,0,0,1,0,0,1,0,2,0,7,0,0,0,0,0,0,0,0,0,0,2,1,2,3,5],
                               "lossoth": [1,3,0,0,0,0,0,0,3,0,2,0,0,2,0,0,4,0,0,0,0,0,0,3,1,5,1,4],
                               "rohirrim": [1,0,1,2,0,2,0,0,0,1,1,0,8,1,0,0,0,0,0,0,0,0,0,3,1,3,4,5],
                               "campesinos": [1,1,1,1,0,1,0,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,2,1,3,4,5],
                               "burgueses": [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,0,1,1,15,5,5],
                               "variag": [1,1,0,0,0,2,0,0,1,1,1,0,4,0,0,0,1,0,0,0,0,0,0,2,1,5,3,4],
                               "bosques": [1,1,0,0,0,1,0,0,1,1,1,3,0,1,0,0,4,0,0,0,0,0,0,2,1,3,2,5]},
               "resistencias":[0,0,0,0,0,0]},
    "dunedain": {"characteristicas":[5,0,10,0,0,5],"adolescencia":[1,0,1,2,0,2,0,1,0,1,1,0,1,1,0,0,0,0,0,1,1,0,0,3,0,10,6,3],
                 "resistencias":[0,0,5,5,0,0]},
    "medio elfo": {"characteristicas":[5,5,5,0,0,5],"adolescencia":[1,0,1,1,0,1,0,0,0,2,0,1,1,1,0,0,2,0,0,1,0,0,0,1,1,10,4,3],
                   "resistencias":[0,0,5,50,0,0]},
    "silvano": {"characteristicas":[0,10,0,0,5,5],"adolescencia":[1,0,0,0,0,1,0,0,0,3,0,2,1,3,0,0,4,0,0,1,0,0,0,1,3,20,6,4],
                "resistencias":[0,0,10,100,0,0]},
    "sindar": {"characteristicas":[0,10,5,0,5,10],"adolescencia":[1,0,0,0,0,1,0,0,0,2,0,1,1,2,0,0,3,0,0,1,1,0,0,1,3,30,8,3],
               "resistencias":[0,0,10,100,0,0]},
    "noldor": {"characteristicas":[0,15,10,5,5,15], "adolescencia":[1,0,0,0,0,1,0,0,0,1,0,0,1,2,0,0,2,0,0,2,1,0,0,1,3,40,10,2],
               "resistencias":[0,0,10,100,0,0]},
    "medio orco": {"characteristicas":[5,0,5,0,0,-5],"adolescencia":[1,1,3,1,0,0,3,0,1,1,0,1,0,0,0,1,0,0,0,0,0,0,0,2,0,0,2,3],
                   "resistencias":[0,0,10,0,0,0]},
    "orco": {"characteristicas":[5,-5,15,-10,-10,-10],"adolescencia":[1,1,3,2,0,0,3,0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,2,0,0,2,2],
             "resistencias":[0,0,20,5,0,0]},
    "uruk-hai": {"characteristicas":[10,0,20,0,-5,-10],"adolescencia":[1,1,3,3,0,4,1,1,1,1,1,1,1,0,0,1,0,0,0,0,0,0,0,3,1,0,2,2],
                 "resistencias":[0,0,20,5,0,0]},
    "medio troll": {"characteristicas":[10,-5,10,-5,-5,-5],"adolescencia":[1,1,2,3,0,0,0,4,2,0,0,1,0,0,0,1,0,0,0,0,0,0,0,4,0,0,2,2],
                    "resistencias":[0,0,15,5,0,0]},
    "troll": {"characteristicas":[15,-10,15,-15,-15,-10],"adolescencia":[1,0,0,0,0,0,0,3,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,5,0,0,2,1],
              "resistencias":[0,0,30,10,0,0]},
    "olog-hai": {"characteristicas":[20,-5,15,-5,-10,-10],"adolescencia":[1,0,0,0,0,0,0,5,2,0,0,1,0,0,0,0,0,0,0,0,0,5,1,0,2,1],
                 "resistencias":[0,0,20,10,0,0]}
}
player_info = {"id": None, "nombre": None,"familia": None, "raza": None, "estatura": None,
                "peso": None, "genero": None, "edad": None, "pelo": None,
                "ojos": None, "especial Fisico": None, "personalidad": None, "motivacion": None,
                "alineamiento": None, "status": None, "profesion": None, "apariencia": None}





idiomas = []
sortilegios= {}
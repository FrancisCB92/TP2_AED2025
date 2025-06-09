#algoritmos de las tablas!!

#como agregamos la moneda! y los returns!???
#estan incompletas las funciones

#falta agregar moneda ARS
def com_1 (monto_nominal):
    comision = (9 * monto_nominal) / 100
    monto_base =  monto_nominal - comision
    return monto_base

#falta agregar moneda USD
def com_2 (monto_nominal):
    comision = 0
    if monto_nominal < 50000:
        comision = 0
    elif 50000 <= monto_nominal < 80000:
        comision = (5 * monto_nominal) / 100
    elif monto_nominal >= 80000:
        comision = (7.8 * monto_nominal) / 100
    monto_base = monto_nominal - comision
    return monto_base


#falta agregar moneda EUR o GBP
def com_3 (monto_nominal):
    monto_fijo = 100
    comision = 0
    if monto_nominal > 25000:
        comision =  (6 * monto_nominal) / 100

    monto_base = monto_nominal - (monto_fijo + comision)
    return monto_base

#moneda JPY
def com_4 (monto_nominal):
    comision = 0
    if monto_nominal <= 100000:
        comision = 500
    elif monto_nominal > 100000:
        comision = 1000
    monto_base = monto_nominal - comision
    return monto_base

def com_5 (monto_nominal):
    comision = 0
    if monto_nominal < 500000:
        comision = 0
    elif monto_nominal >= 500000:
        comision = (7 * monto_nominal) / 100
    monto_base = monto_nominal - comision
    return monto_base


# algoritmos para cálculo impositivo
def cal_imp1 (monto_base):
    impuestos = 0
    if monto_base <= 300000:
        impuesto = 0
    elif monto_base > 300000:
        excedente = monto_base - 300000
        impuestos =  (25 * excedente) / 100
    monto_final = monto_base - impuestos
    return monto_final

def cal_imp2 (monto_base):
    impuestos = 0
    if monto_base > 50000:
        impuestos = 50
    elif monto_base >= 50000:
        impuestos = 100
    monto_final = monto_base - impuestos
    return monto_final

def cal_imp3 (monto_base):
    impuesto =  (3 * monto_base) / 100
    monto_final = monto_base - impuesto
    return monto_final

#Funciones de consignas / requerimientos

#Punto 1
"""Peso argentino ARS
Dólar estadounidense USD
Euro EUR
Libra esterlina GBP
Yen JPY"""
monedas_validas = [ "ARS", "USD", "EUR", "GBP", "JPY" ]

def operaciones_invalidas(codigo_pago):
    mon_valida = 0
    ars = usd = eur = gbp = jpy = False
    for n in range(0, len(monedas_validas)):
        print(monedas_validas[n])
        if monedas_validas[n] in codigo_pago:
            mon_valida += 1
        else:
            return False

    return mon_valida





#Lectura del archivo, estructura basado en Ficha 11, pág. 227 (2025) ADAPTAR
archivo = open('ordenes_test1.txt', 'rt')

# leer la primera línea y procesarla por fuera…
line = archivo.readline()
print('timestamp: ', line)

while True:
    # intentar leer una línea...
    line = archivo.readline()
    # Si se obtuvo una cadena vacía... cortar el ciclo y terminar...
    if line == '':
        break
    # procesar aquí la línea leída...
    n_destinatario = line[0:19]
    cod_id_destinatario = line[20:29]
    cod_or_pago = line[30:39]
    monto_nominal = int(line[40:49])
    alg_calc_comision = int(line[50:51])
    agl_calc_impositivo = int(line[52:53])

    print('n_destinatario:', n_destinatario)
    print('cod_id_destinatario:', cod_id_destinatario)
    print('cod_or_pago:', cod_or_pago)
    print('monto_nominal:', monto_nominal)
    print('alg_calc_comision:', alg_calc_comision)
    print('agl_calc_impositivo:', agl_calc_impositivo)




# cerrar el archivo antes de terminar...
archivo.close()


print(operaciones_invalidas("ARSJJJ"))

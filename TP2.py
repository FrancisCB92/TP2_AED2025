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





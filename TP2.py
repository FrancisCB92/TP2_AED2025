#declaración de variables, banderas, contadores
op_v_moneda = op_inv_moneda = ac_monto_op_val = op_inv_id = op_v_id = 0




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

#falta agregar moneda JPY
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
#########################################
#PUNTO 1 - monedas del TP1
"""Peso argentino ARS
Dólar estadounidense USD
Euro EUR
Libra esterlina GBP
Yen JPY"""
#lista de comprobación
monedas_validas = [ "ARS", "USD", "EUR", "GBP", "JPY" ]

def comprobacion_monedas(codigo_pago):
    #es invalida la operacion si no encuentra monedas validas o si estan repetidas
    op_valida = False

    #bandera para comprobar si hay monedas repetidas
    mon_encontrada = None

    #comprobación moneda por moneda en la lista monedas_validas
    for n in range(0, len(monedas_validas)):

        #primer ciclo para comprobar si encuentra una de las monedas
        if monedas_validas[n] in codigo_pago:
            #primera asignación de la "bandera" (con el valor de la moneda que encuentra en lugar de ser binario: false o true)
            if mon_encontrada is None:
                mon_encontrada = monedas_validas[n]
                print("moneda encontrada:", mon_encontrada)
                op_valida = True

            #comprobacion de monedas repetidas diferentes
            elif monedas_validas[n] != mon_encontrada:
                op_valida = False
                print("dos monedas diferentes!", monedas_validas[n], mon_encontrada)
    return op_valida

#Parte del punto 1, comprobación de destinatarios mal identificados, luego en la llamada en el ciclo principal hay un contador
"""El código de identificación del destinatario de la orden de pago, debe componerse únicamente
por letras mayúsculas, dígitos o guiones (pueden ser solo mayúsculas, o solo números, o
cualquier combinación de mayúsculas, números y guiones, pero no solo guiones). Si no se cumple
esta regla, o aparece cualquier caracter de otro tipo en este identificador, implicará que la orden
de pago es inválida por “Destinatario mal identificado”."""
#FALTA no está finalizado, borrador con print(), probar con ejemplos
def comprobacion_id_dest(cod_id_destinatario):
    id_valido = True
    for n in range(0, len(cod_id_destinatario)):
        caracteres_permitidos = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-"
       #comprobación de condiciones que se cumplen o encontrar cuando no se cumple??
        if cod_id_destinatario[n] in caracteres_permitidos == False:
            print("id no permitido por caracter invalido: ", cod_id_destinatario[n])
            id_valido = False
            break
    return id_valido




#PUNTO 2 - Falta! debe tomar valores previamente procesador por comprobacion_monedas() que se agregan a un contador y tomar un acumulador de montos de op válidas.
#Adaptada para funcionar en cada ciclo o al final del procesamiento de todas las órdenes
#def operaciones_validas(op_validas, monto_op_validas):
    #...


#Lectura del archivo, estructura basado en Ficha 11, pág. 227 (2025). Texto de prueba es ordenes_test1.txt tambien en el repositorio
archivo = open('ordenes_test1.txt', 'rt')

# leer la primera línea y procesarla por fuera…
line = archivo.readline()
print('timestamp: ', line)

while True:
    #toma la primera línea - omitir?? ¿Cómo quitarla?, ver salida esperada
    line = archivo.readline()
    # Si se obtuvo una cadena vacía... cortar el ciclo y terminar...
    if line == '':
        break
    # toma valores de cada orden de cada línea y asigna a variables
    n_destinatario = line[0:19]
    cod_id_destinatario = line[20:29]
    cod_or_pago = line[30:39]
    monto_nominal = int(line[40:49])
    alg_calc_comision = int(line[50:51])
    agl_calc_impositivo = int(line[52:53])

    #procesamiento de las órdenes / llamada de funciones
    #PUNTO1 r1 operaciones inválidas por tipo de moneda y PUNTO2 cantidad de opreaciones validas y suma total de montos validas, (separar?)
    if comprobacion_monedas(cod_or_pago):
        op_v_moneda += 1
        #monto final? Punto 2 suma de montos de operaciones válidas
        ac_monto_op_val += monto_nominal
    else:
        op_inv_moneda += 1

    #PUNTO1 r2- cantidad de operaciones inválidas por id destinatario
    if not comprobacion_id_dest(cod_id_destinatario):
        op_inv_id += 1


    print('n_destinatario:', n_destinatario)
    print('cod_id_destinatario:', cod_id_destinatario)
    print('cod_or_pago:', cod_or_pago)
    print('monto_nominal:', monto_nominal)
    print('alg_calc_comision:', alg_calc_comision)
    print('agl_calc_impositivo:', agl_calc_impositivo)

# cerrar el archivo antes de terminar...
archivo.close()

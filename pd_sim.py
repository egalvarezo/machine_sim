class DataFrame:
    def __init__(self, data, *args, **kwargs):
        self.data = data

    def __str__(self):
        return str(self.data)

    def __getitem__(self, indice):
        print('indice', indice)
        if isinstance(indice, slice):
            print('slice', indice.start, indice.step, indice.stop)

    def _index_(arch):
        arch = open(arch)
        for i in arch.keys():
            indice = arch.keys()
            indices = []
            indices.append(indice)
            return indices

    def __setitem__(indice, valor):
        pass

    def iat(self, row, column):
        a = self.data
        b = a[row]
        c = b[column]
        print(c)

    def head(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[n:]

    def T(self, d):
        # print("Hola Mundo"
        print(d.data)
        keys = dict.keys(d.data)

    # Realizar lecturas según su posición
    def iloc(self, i):  # Se debe crear la funcion iloc para el funcionamiento, de leer los datos segun su posicion
        if isinstance(i, slice):
            # if isinstance (j,slice):
            pass

        if isinstance(i, int):
            for i in range(0, i):
                print(self.data[i])
                a = d.data[i][0]


    def funcion_tail(arch, n):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]


    def funcion_crea_Archivo(arch, sep=','):
        # esta funcion creara y guardara un nuevo archivo CSV con el mismo contenido.
        pass


    def funcion_tail(arch, n, sep=';'):
        with open(arch) as f:
            lineas = [lineas.strip('\n') for lineas in f.readlines()]
        return lineas[-n:]

    # Nicolas Arevalo 20202005024
    # Crear el comando copy


    def copy(arch, sep=';'):
        arch = open(arch)

    # Funcion encargada de localizar filas y columnas del documento e identificar si la entrada es un int,str o slice. Imprimiendo los datos.


    def loc(self, columna, fila=None):
        dat = self.data
        # fila=dat[titulos(0)]
        dat[0]
        return fila

    def __neg__(self):
        '''
        Gerardo Muñoz
        Crea un nuevo DataFrame con cada elemento negado
        uso: df2 = -df 
        '''

        # recupera el diccionario del este DataFrame 
        diccionario = self.data
        diccionario_nuevo = {}


        # niega cada elemento del diccionario (si se puede)
        llaves = diccionario.keys()

        for llave in llaves:
            lista = diccionario[llave]
            lista_nueva = []

            diccionario_nuevo[llave] = []
            for elemento in lista:
                try:
                    elemento_nuevo = - elemento
                except Exception as e:
                    elemento_nuevo = elemento
                    print('__neg__.error:',e)
                lista_nueva.append(elemento_nuevo)

            diccionario_nuevo[llave]=lista_nueva
        return DataFrame(diccionario_nuevo)








def read_csv(arch, sep=','):
    arch = open(arch)
    linea = arch.readline()
    data = {}
    titulos = []
    for titulo in linea.split(sep):
        titulo = titulo.strip()
        data[titulo] = []
        titulos.append(titulo)
    for linea in arch.readlines():
        for i, elem_str in enumerate(linea.split(sep)):
            try:
                elem = int(elem_str)
            except:
                try: 
                    elem = float(elem_str)
                except:
                    elem=elem_str.strip()

            data[titulos[i]].append(elem)
    return DataFrame(data)


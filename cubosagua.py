import sys
'''
..include:: ../documentacion.md
'''

class juegoCubos:
    """
    Clase En la que se desarrolla el juego al completo.
    """
    pasos = 0
    aguaEnCubos = {'8': 0, '5': 0, '3': 0}
    """
    Agua inicial en los cubos.
    """

    def __init__(self, fobjetivo):
        """
        Constructor de la clase.
        :param fobjetivo:
        """
        self.objetivo = fobjetivo

    def genStrCubos(self):
        """
        Metodo que genera y nos permite ver los cubos.
        :return:
        """

        caracterAgua = '~'
        visualizadorCubos = []

        for i in range(1, 9):
            if self.aguaEnCubos['8'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 6):
            if self.aguaEnCubos['5'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        for i in range(1, 4):
            if self.aguaEnCubos['3'] < i:
                visualizadorCubos.append('      ')
            else:
                visualizadorCubos.append(caracterAgua * 6)

        # Devuelve una cadena con los cubos y su contenido de agua
        return '''
        8|{7}|
        7|{6}|
        6|{5}|
        5|{4}|  5|{12}|
        4|{3}|  4|{11}|
        3|{2}|  3|{10}|  3|{15}|
        2|{1}|  2|{9}|  2|{14}|
        1|{0}|  1|{8}|  1|{13}|
         +------+   +------+   +------+
            8L         5L         3L
        '''.format(*visualizadorCubos)

    def mostrarEstadoCubos(self):
        """
        Metodo que muestra los cubos y su estado actual.
        :return:
        """
        print()
        print('Intenta conseguir ' + str(self.objetivo) + ' litros de agua en uno de estos cubos')
        print(self.genStrCubos())

    def checkObjetivo(self):
        """
        Metodo que comprueba si has cumplido con el objetivo.
        :return:
        """
        # Comprueba si uno de los cubos ha conseguido el objetivo
        for cantidadAgua in self.aguaEnCubos.values():
            if cantidadAgua == self.objetivo:
                print('Bien hecho! Lo has resuelto en', self.pasos, 'pasos!')
                sys.exit()

    def selecOpcion(self):
        """
        Metodo que muestra un menu permitiendo asi decidir que hacer con los cubos.
        :return:
        """
        # Selección de una opción
        print('Elige una opción:')
        print('  (L)lenar un cubo')
        print('  (V)aciar un cubo')
        print('  (M)over el agua de un cubo a otro')
        print('  (D)escargar todos los cubos')
        print('  (T)odos los cubos llenos')
        print('  (S)alir')

        while True:
            move = input('> ').upper()
            if move == 'SALIR' or move == 'S':
                print('Gracias por jugar!')
                sys.exit()

            if move in ('L', 'V', 'M', 'D', 'T'):
                return move

    def selecCubo(self, mensaje):
        """
        Metodo con el que seleccionas en cubo sobre el que vas a actuar.
        :param mensaje:
        :return:
        """
        while True:
            print(mensaje)
            cuboOrigen = input('> ').upper()

            if cuboOrigen in ('8', '5', '3'):
                return cuboOrigen

    def llenarCubo(self, cuboOrigen):
        """
        Metodo para llenar un unico cubo.
        :param cuboOrigen:
        :return:
        """
        cuboOrigenTam = int(cuboOrigen)
        self.aguaEnCubos[cuboOrigen] = cuboOrigenTam
        self.pasos += 1

    def vaciarCubo(self, cuboOrigen):
        """
        Metodo para vaciar un unico cubo.
        :param cuboOrigen:
        :return:
        """
        self.aguaEnCubos[cuboOrigen] = 0
        self.pasos += 1

    def moverCubo(self, cuboOrigen, cuboDestino):
        """
        Metodo para mover el contenido de un cubo a otro.
        :param cuboOrigen:
        :param cuboDestino:
        :return:
        """
        cuboDestinoTam = int(cuboDestino)
        espacioVacioCuboDestino = cuboDestinoTam - self.aguaEnCubos[cuboDestino]
        aguaEnCuboOrigen = self.aguaEnCubos[cuboOrigen]
        cantidadAMover = min(espacioVacioCuboDestino, aguaEnCuboOrigen)

        # Saco el agua de este cubo
        self.aguaEnCubos[cuboOrigen] -= cantidadAMover

        # Introduzco el agua en este cubo
        self.aguaEnCubos[cuboDestino] += cantidadAMover
        self.pasos += 1

    def jugar(self):
        """
        Metodo con el que llamas a los metodos anteriores para poder jugar.
        :return:
        """
        self.mostrarEstadoCubos()
        while True:
            opcion = self.selecOpcion()
            if opcion == 'L':
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.llenarCubo(cubo)
            elif opcion == "V":
                cubo = self.selecCubo('Selecciona el cubo 8, 5, 3 o SALIR:')
                self.vaciarCubo(cubo)
            elif opcion == "M":
                cuboOrigen = self.selecCubo('Selecciona el cubo ORIGEN 8, 5, 3 o SALIR:')
                cuboDestino = self.selecCubo('Selecciona el cubo DESTINO 8, 5, 3 o SALIR:')
                self.moverCubo(cuboOrigen, cuboDestino)
            elif opcion == "D":
                self.vaciarCubo("8")
                self.vaciarCubo("5")
                self.vaciarCubo("3")
            elif opcion == "T":
                self.llenarCubo("8")
                self.llenarCubo("5")
                self.llenarCubo("3")
            self.mostrarEstadoCubos()
            self.checkObjetivo()


if __name__ == "__main__":
    juego = juegoCubos(4)
    juego.jugar()

class Liquid:
    '''Жидкость'''

    def __init__(self, density: float = 0, name: str = 'liquid'):
        '''density - плотность, name - название'''
        self._density, self._name = density, name  # начальные значения

    density, name = property(), property()

    @density.setter
    def density(self, value: float):
        '''Установка значения плотности'''
        self._density = value

    @name.setter
    def name(self, value: str):
        '''Установка имени'''
        self._name = value


class Alcohol(Liquid):
    '''Алкоголь'''

    def __init__(self, density: float = 0, name: str = 'alcohol', percent: float = 0):
        '''density - плотность, name - название, percent - крепкость'''
        super().__init__(density, name)
        self._percent = percent

    name, percent = property(), property()

    @name.setter
    def name(self, value: str):
        '''Установка имени алкогольного напитка'''
        self._name = value

    @percent.setter
    def percent(self, value: float):
        '''Установка крепкости'''
        self._percent = value
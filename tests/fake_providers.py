import random
from src.modelo.album import Medio

from faker.providers import BaseProvider

class AlbumTituloProvider(BaseProvider):
    def albumTitulo(self):
        albumesTitulo = [
            'Latin Jazz Compilation',
            'Bandas sonoras famosas',
            'The Dark Side of the Moon',
            'The Bodyguard',
            'Rumours',
            'Saturday Night Fever',
            'El fantasma de la ópera',
            'Come on Over',
            'The Dark Side Of The Moon',
            'Rumours',
            'Revolver',
            'Nevermind',
            'American Idiot',
            'OK Computer',
            'Is This It']
        return random.choice(albumesTitulo)

class AlbumAnioProvider(BaseProvider):
    def albumAnio(self):
        anio = [2018, 2019, 2020, 2021]
        return random.choice(anio)

class AlbumDescripcionProvider(BaseProvider):
    def albumDescripcion(self):
        descripcion = ["Album original", "Compilación","Ganó el Grammy"]
        return random.choice(descripcion)

class AlbumMedioProvider(BaseProvider):
    def albumMedio(self):
        self.medios = [ Medio.CD , Medio.CASETE , Medio.DISCO ]
        return random.choice(self.medios)

class AlbumFechaProvider(BaseProvider):
    def AlbumFecha(self):
        new_date = datetime(2019, 2, 28, 00, 00, 00, 00000)
        fecha = [new_date, new_date + timedelta(days=-1), new_date + timedelta(days=-2)]
        return random.choice(fecha)

class CancionTituloProvider(BaseProvider):
    def cancionTitulo(self):
        cancion = [
            'Bam bam',
            'Chica paranormal',
            'Contigo Perú',
            'Hasta los dientes',
            'Lobo hombre en Paris',
            'Ojos así',
            'Soñe',
            'Soñe',
            'Querido Amigo',
            'Devuélveme a mi chica',
            'Whats Up',
            'Eyes Without A Face',
            'Bendita tu luz',
            'Billie Jean',
            'Rocket Man',
            'Duele el amor',
            'She Will Be Loved',
            'cant hold us',
            'Amapolas',
            'Tiroteo',
            'En esta habitación',
            'happier']
        return random.choice(cancion)


class CancionMinutosProvider(BaseProvider):
    def cancionMinutos(self):
        minutos = [1, 2, 3, 4, 5]
        return random.choice(minutos)


class CancionSegundosProvider(BaseProvider):
    def cancionSegundos(self):
        segundos = [10, 20, 30, 40, 50]
        return random.choice(segundos)


class CancionCompositorProvider(BaseProvider):
    def cancionCompositor(self):
        compositor = ['Leo Rizzi', 'Maluma baby', 'Ben Goldwasser', 'Aleks Syntek', 'ChavezMax', 'Faraón',
                      'Rauw Alejandro']
        return random.choice(compositor)
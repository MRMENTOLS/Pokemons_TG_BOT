from random import randint
import requests
import json

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = randint(1, 1000)
        self.fetch_pokemon_data()

        Pokemon.pokemons[pokemon_trainer] = self

    def fetch_pokemon_data(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Проверка кода ответа (200 OK)
            data = response.json()

            self.name = data['name']
            self.img = data["sprites"]["front_default"]
            self.types = [type_data['type']['name'] for type_data in data['types']]
            self.abilities = [ability_data['ability']['name'] for ability_data in data['abilities']]
            self.height = data['height']
            self.weight = data['weight']
            self.stats = {stat_data['stat']['name']: stat_data['base_stat'] for stat_data in data['stats']}

        except requests.exceptions.RequestException as e:
            print(f"Ошибка сети: {e}")
            self.handle_api_error()

        except KeyError as e:
            print(f"Ошибка в данных API: {e}, pokemon_number: {self.pokemon_number}")
            self.handle_api_error()


    def handle_api_error(self):
        self.name = "Pikachu"
        self.img = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png" #Замена на картинку Пикачу
        self.types = ["Electric"]
        self.abilities = ["Static"]
        self.height = 4
        self.weight = 60
        self.stats = {"hp": 35, "attack": 55, "defense": 40, "special-attack": 50, "special-defense": 50, "speed": 90}


    def get_name(self):
        return self.name

    def get_img(self):
        return self.img

    def get_types(self):
        return self.types

    def get_abilities(self):
        return self.abilities

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_stats(self):
        return self.stats

    def set_name(self, new_name):
        self.name = new_name

    def set_img(self, new_img):
        self.img = new_img

    def set_types(self, new_types):
        self.types = new_types

    def info(self):
        stats_str = "\n".join([f"{stat}: {value}" for stat, value in self.stats.items()])
        return f"Тренер: {self.pokemon_trainer}\nИмя покемона: {self.name}\nТипы: {', '.join(self.types)}\nСпособности: {', '.join(self.abilities)}\nРост: {self.height}\nВес: {self.weight}\nСтаты:\n{stats_str}"

    def show_img(self):
        if self.img:
            return self.img  # Возвращаем ссылку на изображение
        else:
            return "Изображение не найдено."

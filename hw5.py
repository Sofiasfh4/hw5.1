import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_job(self):
        if self.car and self.car.drive():
            self.job = Job(job_list)
        else:
            self.to_repair()

    def get_home(self):
        if not self.home:
            self.home = House()
    def get_car(self):
        if not self.car:
            self.car = Auto(brands_of_cars)
    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            self.satiety = min(self.satiety + 5, 100)
            self.home.food -= 5
    def work(self):
        if self.job:
            if self.car and self.car.drive():
                self.money += self.job.salary
                self.gladness -= self.job.gladness
                self.satiety -= 4
            else:
                self.shopping("fuel") if self.car.fuel <= 0 else self.to_repair()
        else:
            self.get_job()

    def shopping(self, manage):
        if not self.car or not self.car.drive():
            print("Problems with the car. Trying to solve it...")
            if self.car.fuel <= 0:
                self.shopping("fuel")
            else:
                self.to_repair()
            return

        if manage == "food":
            if self.money >= 20:
                self.money -= 20
                self.home.food += 20
                print(f"{self.name} I bought food.")
            else:
                print("Not enough money to buy food.")
        elif manage == "fuel":
            if self.money >= 50:
                self.money -= 50
                self.car.fuel += 50
                print(f"{self.name} I refueled my car.")
            else:
                print("Not enough money for fuel.")
        elif manage == "delicacies":
            if self.money >= 15:
                self.money -= 15
                self.gladness += 5
                self.satiety += 2
                print(f"{self.name} I bought delicacies for joy.")
            else:
                print("Not enough money for delicacies.")

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        print(f"{self.name} cleaned the House.")
    def to_repair(self):
        if self.car and self.money >= 50:
            self.money -= 50
            self.car.strength = min(self.car.strength + 100, 100)
            print(f"{self.name} I repaired the car.")
        else:
            print("Not enough money to repair a car.")

    def days_indexes(self, day):
        pass

    def is_alive(self):
        if(self.gladness < 0):
            print(f"{self.name} has depression ...")
            return False
        if(self.satiety < 0):
            print(f"{self.name} is dead...")
            return False
        if (self.money < -500):
            print(f"{self.name} is bankrupt ...")
            return False
        return True

    def live(self,day):
        if self.is_alive() == False:
            return False


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            return True
        else:
            print("Car cannot move")
            return False

class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job]['gladness']


job_list = {
    'Java Developer' :
        {'salary': 50, 'gladness': 10, },
    'Python Developer' :
        {'salary': 100, 'gladness': 10, },
    'C++ Developer' :
        {'salary': 100, 'gladness': 5, },
    'Rust Developer' :
        {'salary': 50, 'gladness': 3, },
}

brands_of_cars = {
    'BMW' : {'fuel': 100, 'strength': 100, 'consumption': 6 },
    'Volvo' : {'fuel': 200, 'strength': 120, 'consumption': 20 },
    'Ferrari' : {'fuel': 80, 'strength': 120, 'consumption': 8 },
}

first_car = Auto(brands_of_cars)
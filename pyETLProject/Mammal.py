import abc
class Mammal(abc.ABC):


    def __init__(self,birth,sound,legs):
        self.__birth = birth
        self.__sound = sound
        self.__legs = legs

    @abc.abstractmethod
    def calling(self):
        '''
        what sound this mammal calling
        '''

    @abc.abstractmethod
    def run_speed(self):
        '''
        how this mammal run
        '''

    @property
    def birth(self):
        return self.__birth

    @property
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, sound):
        self.__sound = sound
        return None

    @property
    def legs(self):
        return self.__legs

class Cat(Mammal):
    def __init__(self, birth, sound, legs):
        super().__init__(birth, sound, legs)

    def calling(self):
        if(self.sound == 'Meow'):
            return "This is Cat"
        else:
            return "Fake Cat!"

    def new_calling(self, sound):
        self.sound = sound
        return self.calling()

    def run_speed(self):
        return self.legs*10

class Dog(Mammal):
    def __init__(self, birth, sound, legs,is_pet):
        super().__init__(birth, sound, legs)
        self.__is_pet = is_pet

    def calling(self):
        if(self.sound == 'Wang'):
            return "This is Dog"
        else:
            return "Fake Dog!"

    def run_speed(self):
        return self.legs*20

    def check_pet(self):
        return "Pet is " +str(self.__is_pet)

class Monkey(Mammal):
    def __init__(self, birth, sound, legs, tool):
        super().__init__(birth, sound, legs)
        self.__tool = tool

    def calling(self):
        if(self.sound == 'Gau'):
            return "This is Monkey"
        else:
            return "Fake Monkey!"

    def run_speed(self):
        return self.legs*2

    def tool(self):
        return self.__tool

    def use_tool(self):
        return "This Monkey can use " +self.__tool


if __name__ == '__main__':
    cat =Cat("1990/01/01", "Meow", 4)
    print("birthday is " + cat.birth)
    print(cat.calling())
    print(cat.new_calling("Wang"))
    print(cat.run_speed())

    dog = Dog("2000/01/01", "Wang", 4, False)
    print("birthday is " + dog.birth)
    print(dog.calling())
    print(dog.check_pet())
    print(dog.run_speed())

    monkey = Monkey("2005/01/01", "Gau", 4, "stone")
    print("tool is " + monkey.tool())
    print(monkey.calling())
    print(monkey.use_tool())
    print(monkey.run_speed())
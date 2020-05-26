# -*- coding:utf-8 -*-
'''
简单工厂模式
'''

class Animal(object):
    def GetName(self):
        raise NotImplementedError

class Dog(Animal):
    def GetName(self):
        print('Dog')

class Cat(Animal):
    def GetName(self):
        print('Cat')

class AnimalsFactory(object):
    def CreateAnimal(self, name):
        if name == 'Dog':
            return Dog()
        elif name == 'Cat':
            return Cat()
        else:
            return None


if __name__ == '__main__':
    animalsFactory = AnimalsFactory()
    animal = animalsFactory.CreateAnimal('Dog')
    name = animal.GetName()

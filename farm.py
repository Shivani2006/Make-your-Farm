class Farm:
    def __init__(self, type_farm, type_soil ,type_seeds, extra_equipments, farm_animals):
        self.typeOfFarm= type_farm
        self.typeOfSoil= type_soil
        self.typeOfSeeds= type_seeds
        self.typesOfEquipments= extra_equipments
        self.animals= farm_animals
    
    def farmPlan(self):
        print("Your blueprint of ", self.typeOfFarm," is ready!" )
    
    def feedBack(self):
        print("Thanks for creating a plan for the farm! We wish you best of luck on the most effecient and beautiful farm! You are honestly changing our Earth and making it a better place! Please provide a feedback so other people can change the world too!")
        rating1=input("How was the planning details? Rate from 1 to 5 ")
        rating2=input("How was the service? Rate from 1 to 5 ")
        suggestions=input("Please provide your detailed suggestion ")
        print("Thanks for the feedback! Make a change :)")

#compiling the farm
print("Welcome to our PastaCorner")
name=input("Pls enter your name: ")
type=input( "what kind of farm do you plan to make- flower farm, Vegetable farm, Fruit farm, Grain farm, etc. ")
soil=input( "What kind of soil do you prefer- clay,silty,loamy, etc.: ")
seeds=input( "What 3 seeds would you start off your farm with- based on the type of farm you want (flowers-rose,sunflower,tulips; Vegetable:peas,carrot,potato; Fruit:apple,banana,kiwi... ): ")
equipments=input( "The three basic farming supplies you want to start off with- showel, water can, tractor, etc: ")
animals=input("Get yourselves some soulful animals to make your farm more enjoyable!- dogs,cats,chickens,cows,horses,etc: ")


p1=Farm(type,soil,seeds,equipments,animals)
print(name)
p1.farmPlan()
p1.feedBack()
        
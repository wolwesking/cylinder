from math import *
#created by wolwesking
PI = 3.14

def process():
    radiusInput = input("Radius: ")
    heightInput = input("Height: ")

    height = float(radiusInput)
    radius = float(radiusInput)

    print("Area: {}".format(vector(radius, height)))
    print("Volume: {}".format(area(radius, height)))

    asd = input("Do you want to continue? ")

    if asd == "yes":
        process()


def vector(radius, height):
    result = PI * pow(radius, 2) * height
    return result


def area(radius, height):
    result = PI * pow(radius, 2) * 2 + PI * radius * 2 * height
    return result

process()
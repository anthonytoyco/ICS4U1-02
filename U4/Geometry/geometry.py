import math as m


def area_rectangle(length, width):
    return length * width


def area_circle(radius):
    return m.pi * (radius**2)


def circumference(radius):
    return 2 * (m.pi * radius)


def volume_rectangular_prism(length, width, height):
    return length * width * height


def volume_cylinder(radius, height):
    return m.pi * (radius**2) * height


def surface_area_rectangular_prism(length, width, height):
    return 2 * (
        area_rectangle(length, width) + (height * length) + (height * width)
    )


def surface_area_cylinder(radius, height):
    return (2 * (area_circle(radius))) + area_rectangle(
        circumference(radius), height
    )

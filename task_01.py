#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Docstring. """

import decimal
ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """ Function takes input farhneit temperature and returns celsius.
        Arg:
            Degrees(int): Input value of fahrenheit temperature.

        Returns:
            Celsius(float): return the decimal value of Celsius temperature.

    """
    celsius = decimal.Decimal(((int(degrees)-32)*5)/9)

    return celsius


def celsius_to_kelvin(degrees):
    """Function takes the input celsius temperature and returns kelvin.
       Arg:
           Degrees(int): Input value of celsius temperature.

       Returns:
           Kelvin(decimal): return the decimal value of Kelvin temperature.
    """
    kelvin = decimal.Decimal(ABSOLUTE_DIFFERENCE) + decimal.Decimal(degrees)

    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Function converts fahrenheit to kelvin by calling  two functions above.
       The function first returns the fahrennheit to celsius by calling
       fahrenheit_to_celsius and then returns the value to kelvin by
       calling the celsius_to_kelvin temperature.

    """
    fahrenheit = (celsius_to_kelvin(fahrenheit_to_celsius(degrees)))

    return fahrenheit

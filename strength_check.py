import numpy as np
import pandas as pd
import math


def check_password_strength(password):
    if len(password) < 8:
        strength = "Weak"
    elif len(password) < 12:
        strength = "Medium"
    else: 
        strength = "Strong"

    upper_count = sum(1 for c in password if c.isupper())
    lower_count = sum(1 for c in password if c.islower())
    number_count = sum(1 for c in password if c.isdigit())
    symbol_count = sum(1 for c in password if not c.isalnum())
    if upper_count + lower_count + number_count + symbol_count < 3:
        strength = min(strength, "Weak")

    return strength



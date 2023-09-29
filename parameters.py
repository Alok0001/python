#defining a function with paprameters and return value
def calculater_power(base, exponent):
    result = base ** exponent
    return result

#calling the fucntion
base_value = 2
exponent_value = 3
power_reuslt = calculater_power(base_value,exponent_value)
print(f"{base_value} raised to the power of {exponent_value} is {power_reuslt}")

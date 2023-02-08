# Todo: Code is a bit unclear

def convert_fahr_to_cels(x):
    """ 
    Given a temp in fahrenheit, converts it to celsius
    
    :param fahr: the temperature in fahrenheit
    :raises ValueError: If temp is below absolute zero
    :return: the temperature in celsius
    """
    s
    cel = (farh - 32) * (5 / 9)
    if celsius < -273.15:
        raise ValueError(
            f"trying to convert impossible temperature: {fahr}"
        )
    return cel

def convert_fahr_to_K(x):
    cels = convert_fahr_to_cels(x)
    kel = cels + 273.15
    return Kel

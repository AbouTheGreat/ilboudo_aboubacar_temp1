while True:
    print("temperature: "+ input.temperature(TemperatureUnit.FAHRENHEIT))
    if input.temperature(TemperatureUnit.FAHRENHEIT) > 70:  
        light.set_all(light.rgb(255,0,0))
    elif 40 < input.temperature(TemperatureUnit.FAHRENHEIT) < 70:
        light.set_all(light.rgb(0, 255, 0))
    else:
        light.set_all(light.rgb(0, 0, 255)
        )
    
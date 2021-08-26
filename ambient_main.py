import AmbientAPI as ambient_api

if __name__ == '__main__':
    rate = 0.1

    monitor = ambient_api.AmbientAPI(rate)

    curr_temp = monitor.get_temperature()
    print("current temperature ")
    print(curr_temp)
    print()

    curr_temp_list = monitor.get_temperature_extremes()
    print("current temperature List")
    print(curr_temp_list)
    print()

    curr_hum = monitor.get_humidity()
    print("current humidity ")
    print(curr_hum)
    print()

    curr_hum_list = monitor.get_humidity_extremes()
    print("current humidity List ")
    print(curr_hum_list)
    print()

    print(monitor.reset_temperature())

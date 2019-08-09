from colorama import init
init()

from colorama import Fore, Back, Style
init()

import pyowm
print ("Привет, я умная программа, которая может рассказать тебе о погоде и порекомендовать, в чём сегодня можно выйти на улицу.")
print ("\n")
owm = pyowm.OWM('ade741680232727541aebcd332259989', language = "ru")

print ( Back.BLUE )
print ( Fore.WHITE )

place = input("Введите город, в котором вы проживаете: ")

print ( Back.RESET )
print ( Fore.RESET )

observation = owm.weather_at_place(place)
w = observation.get_weather()


#--Сбор информации о погоде в городе
wind_speed 	= str(w.get_wind()['speed'])
min_temp 	= str(w.get_temperature('celsius')["temp_min"])
tek_temp 	= str(w.get_temperature('celsius')["temp"]) 
max_temp 	= str(w.get_temperature('celsius')["temp_max"])
humidity 	= str(w.get_humidity())

#Шкала скорости ветра
no_wind         = "Штиль"
small_wind      = "Легкий ветерок"
light_wind      = "Слабый ветер"
moderately_wind = "Умеренный ветер"
strong_wind     = "Сильный ветер"
storm           = "Шторм"
hurricane       = "Ураган"



print ( Back.WHITE )
print ( Fore.BLACK )


if place == "Москва":

	print ("\n\n\n\n\n\n\n\n")
	print ("------------------------------------------------------------")
	print ("                   ►Прогноз на сегодня◄                     ")
	print ("------------------------------------------------------------")
	print ("\n")

	print ("Сегодня в столице России - " + w.get_detailed_status())

else:

	print ("\n\n\n\n\n\n\n\n")
	print ("------------------------------------------------------------")
	print ("                    ►Прогноз на сегодня◄                    ")
	print ("------------------------------------------------------------")
	print ("\n")

	print ("Сегодня в городе " + place + " - " + w.get_detailed_status())

print ("\n")

print ( Back.CYAN )
print ( Fore.BLACK )

print ("Комфорт:")
print ("Скорость ветра приблизительно равна " + wind_speed + " м/с")



if wind_speed <= str(0.2):
    print (no_wind)
elif wind_speed <= str(1.5) and wind_speed >= str(0.3):
    print (small_wind)
elif wind_speed <= str(5.4) and wind_speed >= str(1.5):
    print (light_wind)
elif wind_speed <= str(10.7) and wind_speed >= str(5.5):
    print (moderately_wind)
elif wind_speed <= str(20.7) and wind_speed >= str(10.8):
    print (strong_wind)
elif wind_speed <= str(32.6) and wind_speed >= str(20.8):
    print (storm)
elif wind_speed >= str(33):
    print (hurricane)



print ("Влажность воздуха равна " + humidity + " %")

print ("Минимальная температура за сегодня равна " + min_temp + " °С.")
print ("Максимальная температура за сегодня равна " + max_temp + " °С.")
print ("Текущая температура - " + tek_temp + " °С.")

print ("\n")

print ( Back.YELLOW )
print ( Fore.BLACK )

print ("Рекомендации:")

if w.get_detailed_status() == "дождь" or w.get_detailed_status() == "сыро":
    print ("Если соберётесь пойти на прогулку, не забудьте взять зонтик.")
if w.get_detailed_status() == "пасмурно":
    print ("Если соберётесь пойти на прогулку, не забудьте взять зонтик.")
elif tek_temp <= str(0):
    print ("На улице холодно, оденьтесь потеплее.")
elif tek_temp >= str(1) and tek_temp <= str(12):
    print ("Стоит одеть осеннюю куртку")
elif tek_temp >= str(13) and tek_temp <= str(25):
    print ("Умеренная температура, можно гулять в летней одежде.")
elif tek_temp >= str(26) and tek_temp <= str(31):
    print ("Без панамы или зонтика на улицу выходить не стоит.")
elif tek_temp >= str(32):
    print ("Включите конденционер, запасайтесь мороженным и отдыхайте у себя дома. ☼")

input("Для продолжения нажмите клавишу \"Enter\"")
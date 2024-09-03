CURRENT_YEAR = 2024

try:
    your_age = input("how old are you ")
    years = 100 - int(your_age)
    print(years + int(CURRENT_YEAR))
except:
    print("faulty input")

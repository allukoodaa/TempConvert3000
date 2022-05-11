#----AlluKoodaa----#

import temp_conversion_module as converter


def menu():
    print("""Choose conversion:
1) Celsius->Fahrenheit
2) Celsius->Kelvin
3) Fahrenheit->Kelvin
4) Fahrenheit->Celsius
5) Kelvin->Celsius
6) Kelvin->Fahrenheit
0) Quit""")

    choice = input("Your choice: ")
    try:
        if int(choice) % 1 != 0:
            return None
    except ValueError:
        return None
    else:
        return int(choice)

def main():
    print(f"Using temperature conversion module, version: {converter.VERSION}")

    while True:
        choice = menu()
        if choice == 0:
            break
        elif choice == None:
            print("\nInvalid input. Please input number.\n")
            continue
        if choice == 1:
            temperature = float(input("Input temperature: "))
            tulos = converter.ctf(temperature)
            print(f"{temperature}C in Fahrenheit:", round(tulos, 2))
        elif choice == 2:
            temperature = float(input("Input temperature: "))
            tulos = converter.ctk(temperature)
            print(f"{temperature}C in Kelvin:", round(tulos, 2))
        elif choice == 3:
            temperature = float(input("Input temperature: "))
            tulos = converter.ftk(temperature)
            print(f"{temperature}F in Kelvin:", round(tulos, 2))
        elif choice == 4:
            temperature = float(input("Input temperature: "))
            tulos = converter.ftc(temperature)
            print(f"{temperature}F in Celcius:", round(tulos, 2))
        elif choice == 5:
            temperature = float(input("Input temperature: "))
            tulos = converter.ktc(temperature)
            print(f"{temperature}K in Celsius:", round(tulos, 2))
        elif choice == 6:
            temperature = float(input("Input temperature: "))
            tulos = converter.ktf(temperature)
            print(f"{temperature}K in Fahrenheit:", round(tulos, 2))
        else:
            print("\nInvalid input. Try again.")
        print()
    print("\nThanks for using my converter. Peace out!")

main()

#----eof----#

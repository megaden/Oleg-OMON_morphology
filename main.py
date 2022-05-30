from bone_mass import main_bone
from muscle_mass import main_muscle
from fat_mass import fat_mass_body
from fat_free import fat_free_body_weight
import pyfiglet
from database.service import register_user, login_on


def menu():
    while True:
        task_input = int(input('Выберите задачу \n'
                               '1. Определение костного компонента "1" \n'
                               '2. Определение мышечной массы тела "2" \n'
                               '3. Определение жирового компонетнта "3" \n'
                               '4. Определение обезжиреной массы тела "4" \n'
                               '==> '))
        if task_input == 1:
            main_bone()

        if task_input == 2:
            main_muscle()

        if task_input == 3:
            fat_mass_body()

        if task_input == 4:
            fat_free_body_weight()


if __name__ == "__main__":
    preview = pyfiglet.figlet_format('MORHOLOGY', font="slant")
    print(preview)
    print('Чтобы войти введите логин и пароль: ')
    login = input('логин:\n==>')
    password = input('пароль:\n==>')

    # login_on(login, password)
    register_user(login, password)
    # if login_on:
    #     menu()
    # else:
    #     register_user(login, password)
    #     if register_user:
    #         menu()


name = ""

def set_name(name_passed_in):
    name = name_passed_in
    print(name)


def display_welcome():
    print('Welcome to this application')


def run():
    display_welcome()
    set_name('Lambou')

    run()

def main():

    ryr = input()
    ryr0 = input()

    if ('да' or 'нет') in (ryr and ryr0):
        print('ВЕРНО')
    elif ('нет' or 'да') in (ryr and ryr0):
        print('ВЕРНО')
    else:
        print('НЕВЕРНО')

if __name__ == "__main__":
    main()
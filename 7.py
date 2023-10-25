def main():

    cat = input('Категория: ')
    if cat == 'продукты':
        pr = int(input('Цена:'))
        if pr < 100:
            print('Попробуйте нашу выпечку!')
        elif pr in range(100, 500):
            print('Как насчёт орехов в шоколаде?')
        elif pr >= 500:
            print('Попробуйте экзотические фрукты!')
    else:
        print('Загляните в товары для дома!')
if __name__ == "__main__":
    main()
def main():

    c = int(input())
    a = int(input())
    t = int(input())
    y = c + a + t
    if c < a < t:
        print('Акция!')
        print('К оплате:', y // 2)
    elif c > a > t:
        print('Акция!')
        print('К оплате:', y // 3)
    else:
        print('К оплате:', y)
if __name__ == "__main__":
    main()
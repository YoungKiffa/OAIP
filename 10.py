def main():
    
    c = int(input())
    if (c % 4 == 0) and (c % 100 != 0) or (c % 400 == 0):
        print('Является високоcным годом')
    else:
        print('Не является високосным годом')
if __name__ == "__main__":
    main()
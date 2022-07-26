print('Добро пожаловать в Super-pizza')
start = input('Хотите заказать пиццу?: y || n.')
price = 0

if start == 'y':
    print('У нас есть пицца разных размеров!\n'
          'На выбор: S(Small) , M (Medium), L (Large)')
    size = input('Введите какую вы хотите S,M или L ?:')
    add_pepperoni = input("Желаете добавить вкуснейшие колбаски пепперони? y || n ")
    extra_cheese = input('Добавить мнооого сыра? y || n "')
    if size == 'S' or size == 's':
        price = 500
        print(f'Вы выбрали пиццу размером ~S~, цена ее {price}₽')
    elif size == 'M' or size == 'm':
        price = 700
        print(f'Вы выбрали пиццу размером ~M~, цена ее {price}₽')
    elif size == 'L' or size == 'l':
        price = 900
        print(f'Вы выбрали пиццу размером ~L~, цена ее {price}₽')

    if add_pepperoni == 'y':
        if size == 'S' or size == 's':
            price += 100
            print(f'К вашей  пицце добавили пепперони \n цена 100₽')
        else:
            price += 150
            print(f'К вашей  пицце добавили пепперони \n цена 150₽')

    if extra_cheese == 'y':
        price += 100
        print(f'будет оооочень сырно + 100₽!')

    print(f"Мы приняли ваш заказ! Сумма к оплате {price}₽")
else:
    print('До свидания! \n ;)')

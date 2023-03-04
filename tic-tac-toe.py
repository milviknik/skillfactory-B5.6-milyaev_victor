# Функция для отображения поля
def display_board(board):
    print(" 123")
    for i in range(3):
        print(str(i + 1) + board[i * 3:i * 3 + 3])


# Функция для проверки выигрыша
def check_win(board):
    # Проверка горизонталей
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != "-":
            return True
    # Проверка вертикалей
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != "-":
            return True
    # Проверка диагоналей
    if board[0] == board[4] == board[8] != "-" or \
            board[2] == board[4] == board[6] != "-":
        return True
    # Нет выигрыша
    return False


# Функция для получения хода игрока и обновления поля
def get_move(board, player):
    while True:
        try:
            move = int(
                input(f"Игрок {player}, введите номер клетки (1-9): ")) - 1  # Отнимаем единицу для индексации с нуля
            if move not in range(9):  # Проверка на допустимый диапазон
                print("Неверный номер клетки. Попробуйте еще раз.")
                continue
            if board[move] != "-":  # Проверка на занятость клетки
                print("Клетка уже занята. Попробуйте еще раз.")
                continue
            break  # Выход из цикла при корректном ходе
        except ValueError:  # Обработка исключения при некорректном вводе
            print("Неверный формат ввода. Попробуйте еще раз.")

    # Обновление поля с учетом хода игрока
    board = board[:move] + player + board[move + 1:]
    return board


# Основная функция игры
def tic_tac_toe():
    # Инициализация пустого поля и текущего игрока
    board = "---------"
    player = "X"

    # Цикл игры до выигрыша или заполнения поля
    while True:

        # Отображение текущего состояния поля
        display_board(board)

        # Получение хода игрока и обновление поля
        board = get_move(board, player)

        # Проверка условия выигрыша
        if check_win(board):
            display_board(board)  # Отображение финального состояния поля
            print(f"Игрок {player} победил!")
            return True

        # Проверка условия ничьей (поле заполнено)
        if "-" not in board:
            display_board(board)  # Отображение финального состояния поля
            print("Ничья!")
            return True

        # Смена текущего игрока
        if player == "X":
            player = "O"
        else:
            player = "X"


# Запуск игры
tic_tac_toe()
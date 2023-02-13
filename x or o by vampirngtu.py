# --- XO game for practical work on SkillFactory FPW-2.0 course
# --- Evgeniy Ivanov, flow FPW-42, Okt'2021
# Не плохо, настолько крут, что даже добавили ссылку GitHab на международной библиотеке Википедиа.
# Несомненно, такая задача мне не под силу, либой займет много времени, поэтому сыграл, код посмотрел, перевел, сдал домашку
# и пошел дальше, учиться...
BOARD = {7: '-', 8: '-', 9: '-', 4: '-', 5: '-', 6: '-', 1: '-', 2: '-', 3: '-'}  # - Игровая доска в консоль

PLAYERS = {
    'X': [],  # - Первый ход делается знаком Х
    'O': []   # - Второму игроку достаётся только символ 0
}

WIN_RULES = (
    (7, 8, 9),  # - тут
    (4, 5, 6),  # - приведены
    (1, 2, 3),  # - все
    (1, 4, 7),  # - выиграшные
    (2, 5, 8),  # - комбинации
    (3, 6, 9),  # - возможные
    (3, 5, 7),  # - \ для
    (1, 5, 9)   # - / поля 3*3
)


def print_board():
    print(f'{BOARD[7]} {BOARD[8]} {BOARD[9]}')
    print(f'{BOARD[4]} {BOARD[5]} {BOARD[6]}')
    print(f'{BOARD[1]} {BOARD[2]} {BOARD[3]}')
#Практично, нумерация сделана именно под раскладку цифр в NumLock

def win_check(sign):
    board_mask = set(PLAYERS[sign])
    winner = bool([True for rule in WIN_RULES if len(board_mask.intersection(rule)) == 3])
    return winner


def set_cell(cell, sign):
    BOARD[cell] = sign
    PLAYERS[sign].append(cell)


def start():
    sign = 'X'  # - current sign
    step = 1    # - current step
    while True:
        # - печатаю доску
        print_board()

        # - ждем, проверяем корректность вводимого числа
        cell = input(f'\nИгрок {sign}, введи число [1-9] или 0 для выхода из игры: ')

        # - if 0 - exit
        if cell == '0':
            break

        # - if in range [1-9] proceed game process
        elif cell in list(map(str, range(1, 10))):
            # - If cell is not busy then set current sign to it
            if BOARD[int(cell)] == '-':
                set_cell(int(cell), sign)
            else:
                print(f'\nПоле занято... выберите другое поле ')
                continue
            # - Winner check
            if win_check(sign):
                print(f'\nИгрок {sign} Победитель по жизни!!!')
                print_board()
                break
            else:
                # - If no winner, check steps
                if step == 9:
                    print(f'\nПустых полей не осталось!!! Никто не поддался, попробуйте еще раз')
                    print_board()
                    break
                else:
                    step += 1
            # - Replace current sign
            sign = 'O' if sign == 'X' else 'X'

        # - if otherwise print a warning and continue
        else:
            print('\nТакого поля не существует, мы играем на поле 3*3, введи значение [1-9] что бы сделать ход, или 0 чтобы выйти из игры')
            continue


if __name__ == '__main__':
    print(f'\nWelcome to XO-game. Game play step by step, from X to O sign.')
    print(f'Используйте Numpad для выбора игрового поля в которое Вы хотите сделать ход.\n')
    start()
import requests
import json
from config import values_dict, HELP


class ApiExeption(Exception):
    '''Класс для обработки исключений'''

    def __init__(self, error_msg):
        self.error_msg = error_msg

    def errors_loging(self, userinfo, message):
        '''Залогировать ошибку, вызвать исключение.'''
        my_file = open("log.txt", "a+")
        my_file.write(f'{str(userinfo)}\nErrMsg: {message} \n\n')
        my_file.close()
        raise ApiExeption(self.error_msg)


class CryptoCompare:
    '''Класс для запроса стоимости обмена валют.'''

    URL_API = ('https://min-api.cryptocompare.com/'
               'data/price?fsym={}&tsyms={}')

    def __init__(self, currency_out, currency_in, quantity):
        self.currency_out = currency_out
        self.currency_in = currency_in
        self.quantity = float(quantity)

    def get_url(self):
        '''Форматировать URL.'''
        url = (self.URL_API.format
               (self.currency_out,
                self.currency_in))
        return url

    def get_exchange(self):
        '''Вычислить стоимость обмена валют.'''
        get_exchange = requests.get(self.get_url())
        total = (float(json.loads(get_exchange.content)
                       [self.currency_in])
                 * (self.quantity))
        return total

    def send_answer(self):
        '''Веруть строку с ответом.'''
        answer = (f'{self.quantity} {self.currency_out} '
                  f'➡️ {self.get_exchange():.2f} {self.currency_in}')
        return answer


class MenuCommands:
    '''Класс для вызова команд из меню.'''

    def __init__(self, message):
        self.message = message

    def all_values(self):
        '''Вернуть строку со всеми доступными валютами.'''
        all_values = 'Доступные валюты:'
        for key, val in values_dict.items():
            all_values = '\n'.join((all_values, '💹 '
                                    + key.capitalize()
                                    + ' - ' + val))
        return all_values

    def help(self):
        return HELP


def process_message(message, userinfo):
    '''Обработка входящего запроса.'''
    COMMANDS = {
            'все валюты': MenuCommands(message).all_values(),
            'помощь': MenuCommands(message).help()
            }

    message = message.lower()
    message_list = list(message.split())

    if message in COMMANDS:
        crp_obj = COMMANDS[message]

    elif len(message_list) == 3:
        if message_list[0] in values_dict and message_list[1] in values_dict:
            val_in = values_dict[message_list[0]]
            val_out = values_dict[message_list[1]]
            val_num = message_list[2]
            if val_out.isnumeric():
                crp_obj = CryptoCompare(val_in, val_out, val_num).send_answer()
            else:
                crp_obj = ApiExeption('Упс... кажется вы ошиблись☹️\n'
                                      f'"{val_num}" не является числовым'
                                      ' значением.').errors_loging(userinfo,
                                                                   message)
        else:
            crp_obj = ApiExeption('Упс... кажется вы ошиблись☹️\n'
                                  'Введенная валюта не может быть'
                                  ' обработана.\n'
                                  'Доступные валюты '
                                  '/values').errors_loging(userinfo,
                                                           message)
    else:
        crp_obj = ApiExeption('Упс... кажется вы ошиблись☹️\n'
                              f'Команда "{message}" '
                              'не определена.').errors_loging(userinfo,
                                                              message)
    return crp_obj

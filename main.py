import requests
import json
import time


def get_price():
    """Получаем текущую цену из API binance"""

    url = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    response = requests.get(url)
    data = json.loads(response.text)
    return float(data['price'])


def check_price():
    """Заждую секунду проверяем текущую цену и сохраняем ее в список prices.
      Держим в этом списке цены за последние 60 минут,
      устаревшие данные удаляем"""
    current_price = get_price()
    prices = [current_price]
    while True:
        time.sleep(1)
        current_price = get_price()
        prices.append(current_price)
        if len(prices) > 3600:
            prices.pop(0)
        price_change = (current_price - prices[0]) / prices[0] * 100
        if abs(price_change) >= 1:
            print(f'Цена изменилась: {price_change:.2f}% за последний час')
        else:
            time.sleep(60)
            print('Цена не выросла более чем на 1% за последние 60 минут')


if __name__ == "__main__":
    check_price()

import requests
import Mcd_link
from xml.etree import ElementTree


def make_url(pbo_number: str):
	"""
	Метод для генерации url
	:param:pb0_number взят из input
	:return: url
	"""
	if pbo_number == str(90033):
		print(f"Введен {pbo_number}. Выполняю...")
		url = Mcd_link.URL + Mcd_link.PBO_33
	if pbo_number == str(90034):
		print(f"Введен {pbo_number}. Выполняю...")
		url = Mcd_link.URL + Mcd_link.PBO_34
	if pbo_number != str(str(90033) or str(90034)):
		print(f"Введен неверный ПБО - {pbo_number}. Доступны только 90033 и 90034")
	
	return str(url)


def send_request(url: str):
	"""
	Метод для отправки запроса GET product_bd
	:param: сгенерированный url
	:return: info product_id, status, price
	"""
	
	response = requests.get(url, stream=True)
	response.raw.decode_content = True
	events = ElementTree.iterparse(response.raw)
	
	print(f'Отправил запрос ...')
	return events


def parse_product_db(events):
	"""
	Метод для обработки xml-ответа на GET-запрос
	:param events: дерево полученное из ответа за GET запрос
	:return:
	"""
	print(f"Обрабатываю product_db. Займет какое то время...")
	
	product_id_array = []
	status_product = []
	prices = []
	
	for events, elem in events:
		if elem.tag == "Product":
			product_id_array.append(int(elem[0].text))
			status_product.append(elem.attrib['statusCode'])
		if elem.tag == "Price":
			prices.append(elem.text)
	
	final = dict(zip(product_id_array, zip(status_product, prices[::3])))
	return final


def display_info(final: dict):
	"""
	Метод для вывода информации на экран
	:param final:
	:return:
	"""
	for key in final:
		print(f" Product_id: {key} \n Статус: {final[key][0]}, Цена: {final[key][1]} \n ______")

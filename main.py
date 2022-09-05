import Methods

if __name__ == "__main__":
	while True:
		pbo_number = input("Укажите ПБО (90033 или 90034). Для выхода введите \"exit\" \n")
		pbo_number = pbo_number.replace(" ", "")
		
		if pbo_number == "exit":
			print("Завершаю.")
			break
		else:
			url_link = Methods.make_url(pbo_number)
			
			xml_events = Methods.send_request(url_link)
			
			final_info = Methods.parse_product_db(xml_events)
			
			Methods.display_info(final_info)

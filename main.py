import Methods

if __name__ == "__main__":
	
	pbo_number = input("Укажите ПБО (90033 или 90034)\n")
	pbo_number = pbo_number.replace(" ", "")
	
	url_link = Methods.make_url(pbo_number)
	
	xml_events = Methods.send_request(url_link)
	
	final_info = Methods.parse_product_db(xml_events)

	Methods.display_info(final_info)
	
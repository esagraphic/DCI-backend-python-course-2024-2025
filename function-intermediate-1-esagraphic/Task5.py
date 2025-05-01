def calculate_area(length, width):
    return length * width


dimensions_list = [5, 10]
list_area = calculate_area(*dimensions_list)
print(f'Area from list:{list_area}')


dimensions_dict = {'length': 5, 'width': 10}
area_from_dict = calculate_area(**dimensions_dict)  
print(f"Area from dictionary: {area_from_dict}")
def get_average_score():
	school_data = [
	    {'school_class': '4a', 'scores': [3,4,4,5,2]}, 
	    {'school_class': '5', 'scores': [3,4,5,2,2]},
	    {'school_class': '6', 'scores': [3,4,4,5,2]},
	    {'school_class': '7', 'scores': [5,5,5,5,5,1]},
	    {'school_class': '8', 'scores': [3,4,4,5,2]},
	    {'school_class': '10a', 'scores': [3,4,5,5,2]},
	    {'school_class': '11', 'scores': [3,4,4,3,2,3,4,4,4,4,5]}
	]
	average_school = 0
	for class_data in school_data:
		average_score = sum(class_data['scores'])/len(class_data['scores'])
		average_school += average_score
		print('Класс {}. Средний балл: {}'.format(class_data['school_class'], round(average_score, 2)))
	print('Средний балл по школе: {}'.format(round(average_school/len(school_data), 2)))

get_average_score()

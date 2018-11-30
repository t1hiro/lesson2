def ask_user():
	while True:
		try:
			answer = input('Как дела?\n')
			if answer == 'Хорошо':
				break
		except KeyboardInterrupt:
			print('\nПока!')
			break

def answer_to_the_question():
	q_and_a = {'Как дела?': 'Хорошо', 'Что делаешь?': 'Программирую'}
	while True:
		question = input("Скажи что-нибудь: ")
		answer = q_and_a.get(question, None)
		if not answer:
			break
		print(answer)

ask_user()
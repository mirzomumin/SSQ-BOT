from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


def send_anonimous_question(update, context):
	buttons = [
		[KeyboardButton('Qonun Qoidalar')],
		[KeyboardButton('Orqaga')],
		[KeyboardButton('Menyuga qaytish')],
	]
	update.message.reply_html('Please, select one of the options below!',
		reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
			one_time_keyboard=True))


def handle_text_message(update, context):
	text = update.message.text

	if text == 'Qonun Qoidalar':
		terms_conditions_text = '1. Qoida №1 keyboard smaller if there are just\
		\n2. Qoida №2 keyboard smaller if there are just\
		\n3. Qoida №3 keyboard smaller if there are just\n...'

		buttons = [
			[KeyboardButton('Savolni yuborish')],
			[KeyboardButton('Orqaga')],
			[KeyboardButton('Menyuga qaytish')],
		]
		update.message.reply_html(terms_conditions_text,
			reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
				one_time_keyboard=True))
	elif text == 'Orqaga':
		update.message.reply_html('Selected option: Orqaga')
	elif text == 'Menyuga qaytish':
		update.message.reply_html('Selected option: Menyuga qaytish')
	elif text == 'Savolni yuborish':
		buttons = [
			[KeyboardButton('Orqaga')],
			[KeyboardButton('Menyuga qaytish')],
		]
		update.message.reply_html('Sizni qiziqtirayotgan savolni yozib yuboring!',
			reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
				one_time_keyboard=True))
	else:
		buttons = [
			[KeyboardButton('Orqaga')],
			[KeyboardButton('Menyuga qaytish')],
		]
		update.message.reply_html('Savolingiz qabul qilindi!',
			reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True,
				one_time_keyboard=True))
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_datas import * # callback data

# main keyboard, shown on the /start command
main = InlineKeyboardMarkup(row_width=1) # creating the keyboard with 1 button per line

show_items = InlineKeyboardButton(text='Afișează lista de caiete \U0001F4CC', # creating a button and mentioning the callback data
                                  callback_data=show_list.new(items_available=True))

main.insert(show_items) # adding the button to the keyboard


# the list of notebooks
notebooks_list = InlineKeyboardMarkup(row_width=1)

first = InlineKeyboardButton(text='🟥 Exersăm pentru Bacalaureat 🟥', callback_data=first.new(first_notebook=True))
second = InlineKeyboardButton(text='🟧 Exerciții aplicative, clasa 10-12 🟧', callback_data=second.new(second_notebook=True))
third = InlineKeyboardButton(text='🟨 Consilier de lectură, clasa 5-9 🟨', callback_data=third.new(third_notebook=True))
fourth = InlineKeyboardButton(text='🟩 Limba Română de nota 10, clasa 8-9 🟩', callback_data=fourth.new(fourth_notebook=True))
fifth = InlineKeyboardButton(text='🟦 Caietul meu, clasa 5 🟦', callback_data=fifth.new(fifth_notebook=True))
sixth = InlineKeyboardButton(text='🟪 Lecția-atelier, clasa 10-12 🟪', callback_data=sixth.new(sixth_notebook=True))

notebooks_list.insert(first)
notebooks_list.insert(second)
notebooks_list.insert(third)
notebooks_list.insert(fourth)
notebooks_list.insert(fifth)
notebooks_list.insert(sixth)

# keyboard under every notebook (after pressed notebooks_list)
notebooks_keyboard = InlineKeyboardMarkup(row_width=1)

# home button
home_button = InlineKeyboardButton(text='Înapoi la lista de caiete ⬅️', callback_data=home.new(home_button=True))
buy_button = InlineKeyboardButton(text='Comandă Online 📱', callback_data=buy.new(buy_=True))
instagram_button = InlineKeyboardButton(text='💡 Pagina noastră de Instagram 💡', callback_data=instagram.new(instagram_=True), url='https://instagram.com/suporturi_didactice?igshid=vz553pnlvbp6')
questions_buttons = InlineKeyboardButton(text='❓ Întrebări ❓', callback_data=question.new(question_=True))

notebooks_keyboard.insert(home_button)
notebooks_keyboard.insert(buy_button)
notebooks_keyboard.insert(instagram_button)
notebooks_keyboard.insert(questions_buttons)

back_keyboard = InlineKeyboardMarkup(row_width=1)

back_keyboard.insert(home_button)
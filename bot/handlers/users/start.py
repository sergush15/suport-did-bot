from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters import Command
from aiogram.utils.emoji import emojize

from keyboards.inline.choice_buttons import *
from loader import dp, bot

from text import *

@dp.message_handler(CommandStart())
async def greetings(message: types.Message):
    await message.answer(text=f'Salutare, {message.from_user.full_name}!\n{greeting}',
                         reply_markup=main)

@dp.callback_query_handler(text_contains='home')
async def home(call: types.CallbackQuery):
    await call.message.edit_text(list_notebooks)
    await call.message.edit_reply_markup(notebooks_list)


@dp.callback_query_handler(text_contains='show')
async def showing_list(call: types.CallbackQuery):
    await call.message.edit_text(list_notebooks)
    await call.message.edit_reply_markup(notebooks_list)

@dp.callback_query_handler(text_contains='buy')
async def buy(call: types.CallbackQuery):
    await call.message.edit_text(comanda)
    await call.message.edit_reply_markup(back_keyboard)

@dp.callback_query_handler(text_contains='question')
async def question(call: types.CallbackQuery):
    await call.message.edit_text(question_text)
    await call.message.edit_reply_markup(back_keyboard)

@dp.callback_query_handler(text_contains='first') # pregatire de bacalaureat
async def first_notebook(call: types.CallbackQuery):
    await call.message.edit_text(bacalaureat)
    await call.message.edit_reply_markup(notebooks_keyboard)


@dp.callback_query_handler(text_contains='second') # exerctii aplicative, clasa 10-12
async def second_notebook(call: types.CallbackQuery):
    await call.message.edit_text(exercitii_aplicative)
    await call.message.edit_reply_markup(notebooks_keyboard)


@dp.callback_query_handler(text_contains='third')
async def third_notebbok(call: types.CallbackQuery):
    await call.message.edit_text(consilier)
    await call.message.edit_reply_markup(notebooks_keyboard)


@dp.callback_query_handler(text_contains='fourth') # limba romana de nota 10
async def second_notebook(call: types.CallbackQuery):
    await call.message.edit_text(nota_10)
    await call.message.edit_reply_markup(notebooks_keyboard)


@dp.callback_query_handler(text_contains='fifth') # caietul meu, clasa 5
async def fifth_notebook(call: types.CallbackQuery):
    await call.message.edit_text(caietul_meu)
    await call.message.edit_reply_markup(notebooks_keyboard)


@dp.callback_query_handler(text_contains='sixth') # lectia-atelier, clasa 10-12
async def sixth_notebook(call: types.CallbackQuery):
    await call.message.edit_text(lectie_atelier)
    await call.message.edit_reply_markup(notebooks_keyboard)





# app/keyboards.py

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.config import settings


class ActionCallback(CallbackData, prefix="action"):
    """
    CallbackData factory for general action buttons.

    Attributes:
        name (str): The name of the action to perform (e.g., 'restart', 'reset').
    """
    name: str


def get_start_keyboard() -> InlineKeyboardMarkup:
    """
    Builds the keyboard for the start message with a "Help" button.
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="❓ Помощь",
        callback_data=ActionCallback(name="help").pack()
    )
    return builder.as_markup()


def get_help_keyboard() -> InlineKeyboardMarkup:
    """
    Builds the keyboard for the help message, providing quick access to common actions.
    """
    builder = InlineKeyboardBuilder()
    builder.button(
        text="📲 Связаться",
        url=settings.MANAGER_TELEGRAM_URL
    )
    builder.button(
        text="🔄 Перезапустить бота",
        callback_data=ActionCallback(name="restart").pack()
    )
    builder.button(
        text="🗑️ Очистить историю",
        callback_data=ActionCallback(name="reset").pack()
    )
    builder.adjust(2, 1)
    return builder.as_markup()

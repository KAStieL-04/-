"""Логика творческого агента «Архивариус странных вещей»."""

import random
from world_data import GENRES


class OddObjectAgent:
    """Превращает обычный предмет в зацепку для короткой истории."""

    def create_dossier(self, object_name: str, genre_id: str) -> str:
        object_name = object_name.strip()
        if not object_name:
            return "Напиши название предмета — например, ключ, варежка или чашка."

        world = GENRES.get(genre_id)
        if world is None:
            return "Не понял жанр. Выбери 1, 2 или 3."

        title = random.choice(world["titles"])
        origin = random.choice(world["origins"])
        power = random.choice(world["powers"])
        cost = random.choice(world["costs"])
        quest = random.choice(world["quests"])

        return (
            f"\n=== ДОСЬЕ: {object_name.upper()} ===\n"
            f"Жанр: {world['name']}\n"
            f"Имя артефакта: {title}\n\n"
            f"Происхождение: {origin}\n\n"
            f"Способность: {power}\n\n"
            f"Цена или странность: {cost}\n\n"
            f"Твоя сюжетная миссия: {quest}\n"
            f"================================\n"
        )

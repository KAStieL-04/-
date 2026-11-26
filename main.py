"""Точка запуска агента. Запускай этот файл: python main.py"""

from agent import OddObjectAgent
from world_data import GENRES


def main() -> None:
    agent = OddObjectAgent()
    print("АРХИВАРИУС СТРАННЫХ ВЕЩЕЙ")
    print("Назови обычный предмет — я превращу его в начало истории.")
    print("Для выхода напиши: выход\n")

    while True:
        object_name = input("Какой предмет исследуем? ").strip()
        if object_name.lower() in {"выход", "стоп", "quit", "exit"}:
            print("Архив закрыт. До новых странностей!")
            break
        if not object_name:
            print("Ты ничего не ввёл. Попробуй ещё раз.\n")
            continue

        print("\nВыбери жанр:")
        for genre_id, world in GENRES.items():
            print(f"{genre_id}. {world['name']}")
        genre_id = input("Номер жанра: ").strip()
        print(agent.create_dossier(object_name, genre_id))


if __name__ == "__main__":
    main()

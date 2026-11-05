#!/usr/bin/env python3
"""Терминальные часы: показывают текущее время и обновляют его каждую секунду.

Запуск:
    python3 clock.py          # живые часы, выход — Ctrl+C
    python3 clock.py --once   # вывести время один раз и выйти
"""

import argparse
import sys
import time
from datetime import datetime

WEEKDAYS = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]


def format_now() -> str:
    now = datetime.now()
    return f"{now:%H:%M:%S}  |  {now:%d.%m.%Y}, {WEEKDAYS[now.weekday()]}"


def run_live() -> None:
    sys.stdout.write("\033[?25l")  # спрятать курсор
    try:
        while True:
            sys.stdout.write("\r\033[K" + format_now())
            sys.stdout.flush()
            time.sleep(1 - time.time() % 1)  # синхронизация с началом секунды
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033[?25h\n")  # вернуть курсор
        sys.stdout.flush()


def main() -> None:
    parser = argparse.ArgumentParser(description="Показывает текущее время в терминале.")
    parser.add_argument("--once", action="store_true", help="вывести время один раз и выйти")
    args = parser.parse_args()

    if args.once:
        print(format_now())
    else:
        run_live()


if __name__ == "__main__":
    main()

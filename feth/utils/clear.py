from feth.utils.path import (
    BIN_PATH,
    CSV_PATH,
    JSON_PATCHED_PATH,
    JSON_RAW_PATH,
    MODS_PATH,
)


def clear_all() -> None:
    clear_bin()
    clear_json()
    clear_mods()
    clear_csv()


def clear_bin() -> None:
    for file in BIN_PATH.glob("*"):
        file.unlink()


def clear_json() -> None:
    for file in JSON_RAW_PATH.glob("*.json"):
        file.unlink()
    for file in JSON_PATCHED_PATH.glob("*.json"):
        file.unlink()


def clear_mods() -> None:
    for file in MODS_PATH.glob("*"):
        file.unlink()


def clear_csv() -> None:
    for file in CSV_PATH.glob("*"):
        file.unlink()

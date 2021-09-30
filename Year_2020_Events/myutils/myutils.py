from typing import List


def get_int_list(filename: str) -> List[int]:
    with open(filename, "r") as f:
        report = f.read().splitlines()
    report = [int(i) for i in report]
    f.close()
    return report


def get_str_list(filename: str) -> List[str]:
    with open(filename, "r") as f:
        report = f.read().splitlines()
    f.close()
    return report

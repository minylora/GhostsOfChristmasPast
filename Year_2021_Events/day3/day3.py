from typing import List, Literal

from Year_2020_Events.myutils.myutils import get_str_list


VALID_DIRECTIONS = ["up", "down", "forward"]


def calculate_gamma_rate(report: List[str]) -> int:
    pass


def calculate_epsilon_rate(report: List[str]) -> int:
    pass


def get_power_consumption(report: List[str]) -> int:
    gamma = calculate_gamma_rate(report)
    epsilon = calculate_epsilon_rate(report)
    return gamma * epsilon


def main():
    pass


if __name__ == "__main__":
    main()

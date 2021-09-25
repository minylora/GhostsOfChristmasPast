from typing import List
from math import floor


def part2(modules: List[int]) -> int:
    total_fuel = 0
    for module in modules:
        total_module_fuel = 0
        while module > 6:
            module = floor(module/3)-2
            total_module_fuel = total_module_fuel + module
        total_fuel = total_fuel + total_module_fuel
    return total_fuel


# module_fuel = round_down(module_mass / 3) - 2
# input = [module_mass1, module_mass2, ...]
# need sum of all fuel values
def part1(modules: List[int]) -> int:
    total_fuel = 0
    for i in range(0, len(modules)):
        fuel = floor(modules[i]/3) - 2
        total_fuel = total_fuel + fuel
    return total_fuel


def get_input(filename: str) -> List[int]:
    with open(filename, 'r') as f:
        data = f.read().splitlines()
    data = [int(d) for d in data]
    return data


def main():
    modules = get_input('input.txt')
    ans = part1(modules)
    print(ans)
    ans = part2(modules)
    print(ans)


if __name__ == "__main__":
    main()

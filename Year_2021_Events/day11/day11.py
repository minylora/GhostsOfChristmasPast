from typing import List, Tuple, Optional

from Year_2020_Events.myutils.myutils import get_list_of_int_lists

ENERGY_TYPE = List[List[int]]
OCTOPUS_ROWS = 10
OCTOPUS_COLS = 10


# when a step is taken
#      - first everything increases by 1
#      - then greater than 9 flashes - flash resets energy to 0
#      - all adjacent, including diagonals, increase by 1
#      - then greater than 9 flashes - flash resets energy to 0
#      - each octopus can only flash once in a step


def increase_adjacent_energy(energy_grid: ENERGY_TYPE, octopus: List[int]) -> ENERGY_TYPE:
    octopus_energy = energy_grid.copy()
    r = octopus[0]
    c = octopus[1]
    adjacent_octos = []
    if r-1 >= 0 and c-1 >= 0:
        adjacent_octos.append([r-1, c-1])
    if r-1 >= 0 and c+1 < OCTOPUS_COLS:
        adjacent_octos.append([r-1, c+1])
    if r+1 < OCTOPUS_ROWS and c-1 >= 0:
        adjacent_octos.append([r+1, c-1])
    if r+1 < OCTOPUS_ROWS and c+1 < OCTOPUS_COLS:
        adjacent_octos.append([r+1, c+1])
    if r-1 >= 0:
        adjacent_octos.append([r-1, c])
    if r+1 < OCTOPUS_ROWS:
        adjacent_octos.append([r+1, c])
    if c-1 >= 0:
        adjacent_octos.append([r, c-1])
    if c+1 < OCTOPUS_COLS:
        adjacent_octos.append([r, c+1])

    for octo in adjacent_octos:
        r = octo[0]
        c = octo[1]
        if octopus_energy[r][c] > 0:
            octopus_energy[r][c] += 1
    return octopus_energy


def flash(energy_grid: ENERGY_TYPE, already_flashed: List[List[int]] = None) -> Optional[Tuple[ENERGY_TYPE, int]]:
    octopus_energy = energy_grid.copy()
    if already_flashed is None:
        already_flashed = []

    # get all the values that should flash
    new_flash = []
    for r in range(0, OCTOPUS_ROWS):
        for c in range(0, OCTOPUS_COLS):
            if octopus_energy[r][c] >= 10 and [r, c] not in already_flashed:
                new_flash.append([r, c])
                octopus_energy[r][c] = 0

    # exit if there are none
    if len(new_flash) == 0:
        return octopus_energy, len(already_flashed)

    # otherwise keep doing stuffs
    for octo in new_flash:
        octopus_energy = increase_adjacent_energy(octopus_energy, octo)
        already_flashed.append(octo)

    return flash(octopus_energy, already_flashed)


def take_a_step(energy_grid: ENERGY_TYPE) -> (ENERGY_TYPE, int):
    # every value increases by 1
    for r in range(0, OCTOPUS_ROWS):
        for c in range(0, OCTOPUS_COLS):
            energy_grid[r][c] += 1

    # flash
    octo_energy, num_flashes = flash(energy_grid)
    return octo_energy, num_flashes


def take_x_steps(energy_grid: ENERGY_TYPE, x_steps: int) -> int:
    octo_energy = energy_grid.copy()
    total_flashes = 0
    for x in range(0, x_steps):
        octo_energy, new_flashes = take_a_step(octo_energy)
        total_flashes += new_flashes
    return total_flashes


def main():
    octo_grid = get_list_of_int_lists("day11_input.txt")
    part_one = take_x_steps(octo_grid, 100)
    print(part_one)


if __name__ == "__main__":
    main()

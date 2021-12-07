from typing import List


def get_initial_state(filename: str) -> List[int]:
    f = open(filename, "r")
    timer = f.readline().split(",")
    f.close()
    timer = [int(i) for i in timer]
    return timer


## part one; no optimization
# def how_many_lantern_fish(init_state: List[int], days: int) -> int:
#     if days < 0:
#         raise ValueError
#     if days == 0:
#         return len(init_state)
#
#     current_state = init_state
#     for day in range(1, days+1):
#         next_state = [None]*len(current_state)
#         new_fish = 0
#         for i in range(0, len(current_state)):
#             next_state[i] = current_state[i] - 1
#             if next_state[i] < 0:
#                 next_state[i] = 6
#                 new_fish += 1
#         for i in range(0, new_fish):
#             next_state.append(8)
#         current_state = next_state
#
#     return len(current_state)


def how_many_lantern_fish(init_state: List[int], days: int) -> int:
    if days < 0:
        raise ValueError
    if days == 0:
        return len(init_state)

    # create fish tracker
    fish_tracker = []
    for i in range(9):
        empty_fish = [i, 0]
        fish_tracker.append(empty_fish)

    # update fish tracker to init state
    for state in init_state:
        fish_tracker[state][1] += 1

    # update fish tracker over number of days
    for day in range(0, days):
        # store how many fish are at 0
        new_fish = fish_tracker[0][1]

        # number of days is reduced by one
        for state in range(0, 8):
            fish_tracker[state][1] = fish_tracker[state+1][1]

        # use stored fish count to reset fish and to create new fish
        fish_tracker[6][1] += new_fish
        fish_tracker[8][1] = new_fish

    # calculate number of fish tracked
    fish_count = 0
    for state in fish_tracker:
        fish_count += state[1]
    return fish_count


def main():
    init_fish = get_initial_state("day6_input.txt")
    day_one = how_many_lantern_fish(init_fish, 80)
    print(day_one)
    day_two = how_many_lantern_fish(init_fish, 256)
    print(day_two)


if __name__ == "__main__":
    main()

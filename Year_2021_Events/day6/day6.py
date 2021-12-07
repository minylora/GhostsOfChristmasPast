from typing import List


def get_initial_state(filename: str) -> List[int]:
    f = open(filename, "r")
    timer = f.readline().split(",")
    f.close()
    timer = [int(i) for i in timer]
    return timer


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
    init_state.sort()
    f = 0
    fish_tracker = [[init_state[0], 1]]
    for i in range(1, len(init_state)):
        if fish_tracker[f][0] == init_state[i]:
            fish_tracker[f][1] += 1
        else:
            fish_tracker.append([init_state[i], 1])
            f += 1



    return 1


def main():
    init_fish = get_initial_state("mini_state")
    day_one = how_many_lantern_fish(init_fish, 80)
    print(day_one)
    # day_two = how_many_lantern_fish(init_fish, 256)
    # print(day_two)


if __name__ == "__main__":
    main()

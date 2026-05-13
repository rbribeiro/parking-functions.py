import random


def generate_bernoulli_prefs(length: int, p: float | int) -> list[int]:
    prefs = []

    for _ in range(length):
        direction = 1 if random.uniform(0, 1) <= p else -1
        prefs.append(direction)

    return prefs


def park_a_car(
    parking_lot: list[int],
    car_number: int,
    car_preference: int,
    search_direction: int = 1,
) -> list[int]:
    if search_direction != -1 and search_direction != 1:
        raise ValueError(
            f"Search direction must be either -1 or 1. Provided {search_direction}"
        )
    if car_preference < 0 or car_preference > len(parking_lot) - 1:
        raise ValueError(f"car_preference out of bounds. Provided {car_preference}")

    while car_preference >= 0 and car_preference < len(parking_lot):
        if not parking_lot[car_preference]:
            parking_lot[car_preference] = car_number
            return parking_lot
        car_preference += search_direction

    return parking_lot


def parking(
    num_spots: int,
    car_preferences: list[int],
    search_direction_prefs: list[float | int],
) -> list[int | None]:
    parking_lot = [None] * num_spots

    for car, car_preference in enumerate(car_preferences):
        parking_lot = park_a_car(
            parking_lot, car, car_preference, search_direction_prefs[car]
        )

    return parking_lot


def uniform_bernoulli_parking(num_spots: int, num_cars: int, p: float | int):
    car_preferences = random.choices(rage(num_spots), k=num_cars)
    search_direction_prefs = generate_bernoulli_prefs(num_cars, p)

    park_result = parking(num_spots, car_preferences, search_direction_prefs)

    return car_preferences, search_direction_prefs, park_result

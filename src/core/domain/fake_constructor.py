import random

import faker
from src.core.domain.model import Bus
fake = faker.Faker()


def get_fake_bus():
    return Bus(
        fio=fake.name(),
        bus_number=random.randint(1, 100),
        route_number=random.randint(1, 100),
        brand=fake.license_plate(),
        creation_year=random.randint(1988, 2022),
        vehicle=random.randint(1, 500)
    )

import datetime
from unittest import mock

import pytest

from app.main import outdated_products
from freezegun import freeze_time


@pytest.mark.parametrize(
    ("products,fake_date,expected"),
    [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            "2022-02-02",
            [
                "duck"
            ],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            "2022-02-11",
            [
                "salmon",
                "chicken",
                "duck",
            ],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            "2022-01-20",
            [],
        ),
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2022, 2, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2022, 2, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2022, 2, 1),
                    "price": 160
                }
            ],
            "2022-02-01",
            [],
        )
    ],
    ids=[
        "Should return one outdated product('duck')",
        "Should return two outdated products('duck' and 'chicken')",
        "Should return no one product when date less the expiration date",
        "Product with expiration date equals today is not outdated."
    ]
)
def test_outdated_products(products: list[dict],
                           fake_date: str,
                           expected: list[str]) -> None:
    with freeze_time(fake_date):
        assert (outdated_products(products)
                == expected)
from dataclasses import dataclass


@dataclass
class TestUser:
    first_name: str
    last_name: str
    email: str
    password: str
    birthday: str

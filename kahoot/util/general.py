import random
from string import ascii_letters, digits

async def generate_random_string(length: int) -> str:
    return "".join(random.choices(ascii_letters + digits, k=length))
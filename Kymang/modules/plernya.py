from Kymang.config import ADMINS
from Kymang.modules.data import *


async def plernya():
    if 6946216221 not in await cek_seller():
        await add_seller(6946216221)

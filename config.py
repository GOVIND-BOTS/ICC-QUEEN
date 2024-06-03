from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "25698939"))
API_HASH = getenv("API_HASH", "7430f53836560b21010e8cfd92e0239b")

BOT_TOKEN = getenv("BOT_TOKEN", "6105046691:AAGfz5sTkZX20EaNW_U2AQ_FCIVQxePAxIk")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5350640981"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/232c3ca139605681dce4e.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/91c7806b38e7b149f5c10.jpg")

SESSION = getenv("SESSION", "AQGIInsABuNr2vi-VJCr6EVlhmFxwWzk5_DtbEB5tM_CBrGEYrmcx-saCl1CZqhMvjUXMMFdiRctNr8bJJv49PbP48B8cBGU5Uks6E4SKBJgSKAKWL0aqZiNXaLWf-6Z-U-MNpvItlPJb7x9tAtIpZv_C-cxuIPdmsgGAZ37BiXePbwAIBFac1Ct28gsrYExbiEMYime3_tGthXS1_h_IPHNph9BOmDJqZ3Tr5XeLEI5HlNiXr4AiEP3yKDvTc10P1eqtJJMRn53kvoTGM5p9JHSRATUwn_-HFdgXu3fQWftFxfYO--jFidzKW1hOF47Q_HOeeHVxHcolLP_KegE57VW4MZTKQAAAAFyb8lPAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_chatting_club_offical")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shayari_ka_tadka")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7142344123").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"

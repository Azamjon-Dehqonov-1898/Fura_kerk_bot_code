from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()
kanallar = ["@furaga_ish_UZBda"]
adminlar = [1240250960]
# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
IP = env.str("ip")  # Xosting ip manzili
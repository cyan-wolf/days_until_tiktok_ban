from datetime import date, timedelta
from color_print import Color, color_str

BAN_SIGN_DATE = date(year=2024, month=4, day=24)

SHORTEST_BAN_DATE = BAN_SIGN_DATE + timedelta(days=9*30)
LONGEST_BAN_DATE = BAN_SIGN_DATE + timedelta(days=365)

TIKTOK_STR = color_str("TikTok", Color.MAGENTA)

def days_until_ban():
    now = date.today()
    diff_short = SHORTEST_BAN_DATE - now
    diff_long = LONGEST_BAN_DATE - now

    return diff_short.days, diff_long.days


def days_since_ban_was_signed():
    now = date.today()
    diff = now - BAN_SIGN_DATE

    return diff.days


def main():
    d_until_ban_short, d_until_ban_long = days_until_ban()
    d_since_sign = days_since_ban_was_signed()

    print(f"Today: {color_str(date.today(), Color.YELLOW)}")
    print()

    print(f"Date that the bill banning {TIKTOK_STR} was signed: {color_str(BAN_SIGN_DATE, Color.CYAN)}")
    print(f"Date that {TIKTOK_STR} will be banned (at the earliest): {color_str(SHORTEST_BAN_DATE, Color.CYAN)}")
    print(f"Date that {TIKTOK_STR} will be banned (approximately at the latest): {color_str(LONGEST_BAN_DATE, Color.CYAN)}")
    print()

    print(f"Days until {TIKTOK_STR} is banned (at the earliest): {color_str(d_until_ban_short, Color.RED)}")
    print(f"Days until {TIKTOK_STR} is banned (at the latest): {color_str(d_until_ban_long, Color.RED)}")
    print(f"Days since the bill banning {TIKTOK_STR} was signed: {color_str(d_since_sign, Color.RED)}")
    print()

    progress_short = f"{d_since_sign/d_until_ban_short*100:.2f}%"
    progress_long = f"{d_since_sign/d_until_ban_long*100:.2f}%"

    print(f"Progress on {TIKTOK_STR} getting banned (at the earliest): {color_str(progress_short, Color.GREEN)}")
    print(f"Progress on {TIKTOK_STR} getting banned (at the latest): {color_str(progress_long, Color.GREEN)}")
    print()

    _ = input("Press any key to exit...")


if __name__ == '__main__':
    main()

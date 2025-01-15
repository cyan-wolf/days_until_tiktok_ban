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

    return max(diff_short.days, 0), max(diff_long.days, 0)


def days_since_ban_was_signed():
    now = date.today()
    diff = now - BAN_SIGN_DATE

    return max(diff.days, 0)


def main():
    d_until_ban_short, d_until_ban_long = days_until_ban()
    d_since_sign = days_since_ban_was_signed()

    should_show_shortest_ban_info = d_until_ban_short > 0
    should_show_longest_ban_info = d_until_ban_long > 0

    print(f"Today: {color_str(date.today(), Color.YELLOW)}")
    print()

    print(f"Date that the bill banning {TIKTOK_STR} was signed: {color_str(BAN_SIGN_DATE, Color.CYAN)}")
    print(f"Date that {TIKTOK_STR} will be banned (at the earliest): {color_str(SHORTEST_BAN_DATE, Color.CYAN)}")
    print(f"Date that {TIKTOK_STR} will be banned (at the latest): {color_str(LONGEST_BAN_DATE, Color.CYAN)}")
    print()

    if should_show_shortest_ban_info:
        print(f"Days until {TIKTOK_STR} is banned (at the earliest): {color_str(d_until_ban_short, Color.RED)}")

    if should_show_longest_ban_info:
        print(f"Days until {TIKTOK_STR} is banned (at the latest): {color_str(d_until_ban_long, Color.RED)}")

    print(f"Days since the bill banning {TIKTOK_STR} was signed: {color_str(d_since_sign, Color.RED)}")
    print()

    progress_short = min(d_since_sign / (SHORTEST_BAN_DATE - BAN_SIGN_DATE).days, 1.0)
    progress_short = f"{progress_short*100:.2f}%"
    print(f"Progress on {TIKTOK_STR} getting banned (at the earliest): {color_str(progress_short, Color.GREEN)}")
    
    progress_long = min(d_since_sign / (LONGEST_BAN_DATE - BAN_SIGN_DATE).days , 1.0)
    progress_long = f"{progress_long*100:.2f}%"
    print(f"Progress on {TIKTOK_STR} getting banned (at the latest): {color_str(progress_long, Color.GREEN)}")

    print()

    _ = input("Press any key to exit...")


if __name__ == '__main__':
    main()

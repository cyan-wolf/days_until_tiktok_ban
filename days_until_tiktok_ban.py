from datetime import time, date, datetime, timedelta, UTC

BAN_SIGN_DATE = date(year=2024, month=4, day=24)

SHORTEST_BAN_DATE = BAN_SIGN_DATE + timedelta(days=9*30)
LONGEST_BAN_DATE = BAN_SIGN_DATE + timedelta(days=365)

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

    print(f"Today: {date.today()}")
    print(f"Date that the bill banning TikTok was signed: {BAN_SIGN_DATE}")
    print(f"Date that TikTok will be banned (at the earliest): {SHORTEST_BAN_DATE}")
    print(f"Date that TikTok will be banned (approximately at the latest): {LONGEST_BAN_DATE}")
    print()

    print(f"Days until TikTok is banned (at the earliest): {d_until_ban_short}")
    print(f"Days until TikTok is banned (at the latest): {d_until_ban_long}")
    print(f"Days since the bill banning TikTok was signed: {d_since_sign}")
    print()

    print(f"Progress on TikTok getting banned (at the earliest): {d_since_sign/d_until_ban_short*100:.2f}%")
    print(f"Progress on TikTok getting banned (at the latest): {d_since_sign/d_until_ban_long*100:.2f}%")
    print()

    _ = input("Press any key to exit...")


if __name__ == '__main__':
    main()

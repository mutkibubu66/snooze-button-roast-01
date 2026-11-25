import os

FRIEND = "The snooze button is my most loyal friend: "
FAIL = "it lets me fail at waking up nine times before 8 a.m. "
JUDGE = "and never once judges me for it."
LINE = FRIEND + FAIL + JUDGE

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))

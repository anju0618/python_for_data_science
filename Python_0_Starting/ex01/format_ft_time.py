#!/usr/bin/env python3
import time
from datetime import date

if __name__ == "__main__":
    now = time.time()

    print(f"Seconds since January 1, 1970: {now:,.4f} or {now:.2e} "
          "in scientific notation")
    print(date.today().strftime("%b %d %Y"))

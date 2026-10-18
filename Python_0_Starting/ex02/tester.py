#!/usr/bin/env python3
import sys
from find_ft_type import all_thing_is_obj


ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}


def main() -> None:
    try:
        all_thing_is_obj(ft_list)
        all_thing_is_obj(ft_tuple)
        all_thing_is_obj(ft_set)
        all_thing_is_obj(ft_dict)
        all_thing_is_obj("Brian")
        all_thing_is_obj("Toto")
        print(all_thing_is_obj(10))

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

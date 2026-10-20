ARGS ?=

SCRIPT_00 := tester.py
SCRIPT_01 := tester.py
SCRIPT_02 := tester.py
SCRIPT_03 := tester.py
SCRIPT_04 := tester.py
SCRIPT_05 := tester.py
SCRIPT_06 := tester.py
SCRIPT_07 := tester.py
SCRIPT_08 := tester.py

NUMS := 00 01 02 03 04 05 06 07 08
EXS := $(NUMS)
RUNS := $(addprefix run-,$(NUMS))

.PHONY: install lint clean fclean $(RUNS)

install:
	uv sync

lint:
	uv run flake8 --exclude=.venv .
	for d in ex*/; do \
		if ls $$d*.py >/dev/null 2>&1; then \
			uv run mypy $$d || exit 1; \
		fi; \
	done

clean:
	find . -name .venv -prune -o \( -name __pycache__ -o -name .mypy_cache \
		-o -name .pytest_cache -o -name '*.egg-info' \) -type d -prune \
		-exec rm -rf {} +
	rm -f ex*/tester.py ex*/test_array2D.py
	rm -rf ex09/build ex09/dist

fclean: clean
	rm -rf .venv

$(RUNS): run-%: tester
	uv run python ex$*/$(SCRIPT_$*) $(ARGS)

define CASES_00
$(T_SH)

sh("ex00/Hello.py | cat -e")
endef

define CASES_01
$(T_SH)

sh("ex01/format_ft_time.py | cat -e")
endef

define CASES_02
from find_ft_type import all_thing_is_obj
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set   = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))
endef

define CASES_03
from NULL_not_found import NULL_not_found
Nothing = None
Garlic = float("NaN")
Zero    = 0
Empty   = ""
Fake    = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
endef

define CASES_04
$(T_SH)

sh("ex04/whatis.py 14")
sh("ex04/whatis.py -5")
sh("ex04/whatis.py")
sh("ex04/whatis.py 0")
sh("ex04/whatis.py Hi!")
sh("ex04/whatis.py 13 5")
endef

define CASES_05
$(T_SH)

sh("ex05/building.py \"Python 3.0, released in 2008, was a major revision that is not completely backward compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020.\"")
sh('ex05/building.py', 'echo "Hello World!" | ')
endef

define CASES_06
$(T_SH)

sh("ex06/sos.py \"sos\" | cat -e")
sh("ex06/sos.py 'h$$llo'")
endef

define CASES_07
$(T_SH)

sh("ex07/filterstring.py 'Hello the World' 4")
sh("ex07/filterstring.py 'Hello the World' 99")
sh("ex07/filterstring.py 3 'Hello the World'")
sh("ex07/filterstring.py")
endef

define CASES_08
from ft_filter import ft_filter

print(list(ft_filter(lambda x: x % 2 == 0, range(10))))
endef

# `make tester` writes ex<nn>/tester.py from CASES_<nn> (the tester shown in the subject).
# Do not use a dollar sign in the macros (make would expand it).
tester:
	@$(foreach n,$(EXS),$(file >ex$(n)/tester.py,$(CASES_$(n))))
	@echo "tester.py generated in: $(addprefix ex,$(EXS))"

.PHONY: tester

# helper for the testers that run a script like the subject does: python <cmd>
define T_SH
import os
import sys


def sh(cmd, pre=''):
    print('$$> ' + pre + 'python ' + cmd, flush=True)
    os.system(pre + sys.executable + ' ' + cmd)
endef

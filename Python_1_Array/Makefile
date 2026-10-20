ARGS ?=

SCRIPT_00 := tester.py
SCRIPT_01 := tester.py
SCRIPT_02 := tester.py
SCRIPT_03 := zoom.py
SCRIPT_04 := rotate.py
SCRIPT_05 := tester.py

NUMS := 00 01 02 03 04 05
EXS := 00 01 02 05
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
from give_bmi import give_bmi, apply_limit
height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))
endef

define CASES_01
from array2D import slice_me
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))
endef

define CASES_02
from load_image import ft_load
print(ft_load("landscape.jpg"))
endef

define CASES_05
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
array = ft_load("landscape.jpg")
ft_invert(array)
ft_red(array)
ft_green(array)
ft_blue(array)
ft_grey(array)
print(ft_invert.__doc__)
endef

# `make tester` writes ex<nn>/tester.py from CASES_<nn> (the tester shown in the subject).
# Do not use a dollar sign in the macros (make would expand it).
tester:
	@$(foreach n,$(EXS),$(file >ex$(n)/tester.py,$(CASES_$(n))))
	@echo "tester.py generated in: $(addprefix ex,$(EXS))"

.PHONY: tester

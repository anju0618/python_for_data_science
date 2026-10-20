ARGS ?=

SCRIPT_00 := tester.py
SCRIPT_01 := aff_life.py
SCRIPT_02 := aff_pop.py
SCRIPT_03 := projection_life.py

NUMS := 00 01 02 03
EXS := 00
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
from load_csv import load
print(load("life_expectancy_years.csv"))
endef

# `make tester` writes ex<nn>/tester.py from CASES_<nn> (the tester shown in the subject).
# Do not use a dollar sign in the macros (make would expand it).
tester:
	@$(foreach n,$(EXS),$(file >ex$(n)/tester.py,$(CASES_$(n))))
	@echo "tester.py generated in: $(addprefix ex,$(EXS))"

.PHONY: tester

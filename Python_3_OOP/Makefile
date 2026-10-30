ARGS ?=

SCRIPT_00 := S1E9.py
SCRIPT_01 := S1E7.py
SCRIPT_02 := DiamondTrap.py
SCRIPT_03 := ft_calculator.py
SCRIPT_04 := ft_calculator.py

NUMS := 00 01 02 03 04
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

$(RUNS): run-%:
	cd ex$* && uv run python $(SCRIPT_$*) $(ARGS)

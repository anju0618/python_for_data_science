ARGS ?=

SCRIPT_00 := Hello.py
SCRIPT_01 := format_ft_time.py
SCRIPT_02 := tester.py
SCRIPT_03 := NULL_not_found.py
SCRIPT_04 := whatis.py
SCRIPT_05 := building.py
SCRIPT_06 := sos.py
SCRIPT_07 := filterstring.py
SCRIPT_08 := ft_filter.py

NUMS := 00 01 02 03 04 05 06 07 08
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
	rm -rf ex09/build ex09/dist

fclean: clean
	rm -rf .venv

$(RUNS): run-%:
	uv run python ex$*/$(SCRIPT_$*) $(ARGS)

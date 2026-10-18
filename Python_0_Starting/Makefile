ARGS ?=

SCRIPT_00 := Hello.py
SCRIPT_01 := format_ft_time.py
SCRIPT_02 := tester.py
SCRIPT_03 := tester.py
SCRIPT_04 := tester.py
SCRIPT_05 := tester.py
SCRIPT_06 := tester.py
SCRIPT_07 := tester.py
SCRIPT_08 := tester.py

NUMS := 00 01 02 03 04 05 06 07 08
RUNS := $(addprefix run-,$(NUMS))

.PHONY: install tester lint clean fclean $(RUNS)

install:
	uv sync

tester:
	@for d in testers/ex*/; do cp -f $$d* $${d#testers/}; done

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

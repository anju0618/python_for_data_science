ARGS ?=

SCRIPT_00 := tester.py
SCRIPT_01 := tester.py
SCRIPT_02 := tester.py
SCRIPT_03 := tester.py

NUMS := 00 01 02 03
EXS := 00 01 02 03
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
from statistics import ft_statistics
ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
print("-----")
ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")
endef

define CASES_01
from in_out import outer
from in_out import square
from in_out import pow
my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
endef

define CASES_02
from callLimit import callLimit

@callLimit(3)
def f():
    print ("f()")

@callLimit(1)
def g():
    print ("g()")

for i in range(3):
    f()
    g()
endef

define CASES_03
from new_student import Student
student = Student(name = "Edward", surname = "agle")
print(student)
endef

include ../tester.mk

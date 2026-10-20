ARGS ?=

SCRIPT_00 := tester.py
SCRIPT_01 := tester.py
SCRIPT_02 := tester.py
SCRIPT_03 := tester.py
SCRIPT_04 := tester.py

NUMS := 00 01 02 03 04
EXS := 00 01 02 03 04
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
from S1E9 import Character, Stark
Ned = Stark("Ned")
print(Ned.__dict__)
print(Ned.is_alive)
Ned.die()
print(Ned.is_alive)
print(Ned.__doc__)
print(Ned.__init__.__doc__)
print(Ned.die.__doc__)
print("---")
Lyanna = Stark("Lyanna", False)
print(Lyanna.__dict__)
endef

define CASES_01
from S1E7 import Baratheon, Lannister
Robert = Baratheon("Robert")
print(Robert.__dict__)
print(Robert.__str__)
print(Robert.__repr__)
print(Robert.is_alive)
Robert.die()
print(Robert.is_alive)
print(Robert.__doc__)
print("---")
Cersei = Lannister("Cersei")
print(Cersei.__dict__)
print(Cersei.__str__)
print(Cersei.is_alive)
print("---")
Jaine = Lannister.create_lannister("Jaine", True)
print(f"Name : {Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")
endef

define CASES_02
from DiamondTrap import King
Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
endef

define CASES_03
from ft_calculator import calculator
v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5
endef

define CASES_04
from ft_calculator import calculator
a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)
endef

# `make tester` writes ex<nn>/tester.py from CASES_<nn> (the tester shown in the subject).
# Do not use a dollar sign in the macros (make would expand it).
tester:
	@$(foreach n,$(EXS),$(file >ex$(n)/tester.py,$(CASES_$(n))))
	@echo "tester.py generated in: $(addprefix ex,$(EXS))"

.PHONY: tester

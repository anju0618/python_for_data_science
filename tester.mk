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

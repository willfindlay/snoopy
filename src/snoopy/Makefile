QML = $(shell ls ./gui/*.ui)
RES = $(shell ls ./gui/*.qrc)
PROJECT_ROOT = $(shell pwd)
QMLPY = $(QML:.ui=.py)
RESPY = $(RES:.qrc=_rc.py)
PY = $(QMLPY) $(RESPY)

all: $(PY)

$(QMLPY): $(QML)
	$(foreach i, $(QML), pyside2-uic $(i) > $(PROJECT_ROOT)/$(shell basename $(i:.ui=.py));)

$(RESPY): $(RES)
	$(foreach i, $(RES), pyside2-rcc $(i) > $(PROJECT_ROOT)/$(shell basename $(i:.qrc=_rc.py));)

clean:
	@rm $(PY)

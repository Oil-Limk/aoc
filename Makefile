YEAR = 2015
DAY = 19
PYFILE = $(YEAR)/d$(DAY).py
TXTFILE = $(YEAR)/d$(DAY).txt
RUN = @uv run

.PHONY: run, setup, lint, format, clean

run: setup
	$(RUN) $(PYFILE) $(TXTFILE)

setup:
	@if [ -d "$(YEAR)" ]; then echo "directory $(YEAR) already exists"; else mkdir $(YEAR); fi
	@if [ -f "$(PYFILE)" ]; then echo "file $(PYFILE) already exists"; else touch $(PYFILE); fi
	@if [ -f "$(TXTFILE)" ]; then echo "file $(TXTFILE) already exists"; else touch $(TXTFILE); fi
	clear

lint:
	$(RUN) ruff check
	$(RUN) ruff format --check

format:
	$(RUN) ruff check --fix
	$(RUN) ruff format

clean:
	@rm */*.txt
	clear

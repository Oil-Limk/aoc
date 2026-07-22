YEAR = 2015
DAY = 14
PT = 1
PYFILE = $(YEAR)/d$(DAY).$(PT).py
TXTFILE = $(YEAR)/d$(DAY).txt
RUN = @uv run

run: setup
	$(RUN) $(PYFILE) $(TXTFILE)

setup:
	@if [ -d "$(YEAR)" ]; then echo "directory $(YEAR) already exists"; else mkdir $(YEAR); fi
	@if [ -f "$(PYFILE)" ]; then echo "file $(PYFILE) already exists"; else touch $(PYFILE); fi
	@if [ -f "$(TXTFILE)" ]; then echo "file $(TXTFILE) already exists"; else touch $(TXTFILE); fi
	@clear

check:
	$(RUN) ruff check

format:
	$(RUN) ruff format

.PHONY: clean

clean:
	@rm */*.txt
	

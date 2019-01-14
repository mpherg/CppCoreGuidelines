.PHONY: all book clean docker

PARENTDIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))/..)

all: docker
	@docker run --rm -v $(PARENTDIR):/work cppcoreguidelines make -C latex VERBOSE=2 CppCoreGuidelines.pdf

# Builds the docker image if it doesn't yet exist
docker:
ifeq (,$(wildcard /.dockerenv))
ifeq ($(shell docker images | grep cppcoreguidelines),)
	docker build -t cppcoreguidelines .
endif
endif

CppCoreGuidelines.pdf: variables.tex
	@pandoc ../CppCoreGuidelines.md -o CppCoreGuidelines.pdf --template template.latex --listings

clean:
	-rm CppCoreGuidelines.pdf
	-rm variables.tex

variables.tex:
	@echo "\\def \\docversion   {$$(git describe --dirty)}"                                       >> variables.tex
	@echo "\\def \\docdate      {$$(date)}"                                                       >> variables.tex
	@echo "\\def \\commit       {$$(git rev-parse  HEAD)}"                                        >> variables.tex
	@echo "\\def \\shortcommit  {$$(git rev-parse --short HEAD)}"                                 >> variables.tex
	@echo "\\def \\commitdate   {$$(git show --oneline --pretty='%ci' | head -1)}"                >> variables.tex
	@echo "\\def \\license      {$$(cat ../LICENSE)}"                                                >> variables.tex
	@echo "\\def \\contributors {$$(git shortlog -s -n --all --no-merges | python people.py)}"    >> variables.tex
	@if git describe --dirty | grep -q dirty; then echo '\def \dirty { (with uncommitted changes)}' >> variables.tex; else echo '\def \dirty {}' >> variables.tex; fi

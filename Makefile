BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"

bake:
	rm -rf fast-api-endpoint
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

clean:
	rm -rf fast-api-endpoint

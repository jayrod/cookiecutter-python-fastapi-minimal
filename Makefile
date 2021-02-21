BAKE_OPTIONS=--no-input

help:
	@echo "bake 	generate project using defaults"
	@echo "clean	delete old folder"

bake:
	rm -rf fast-api-endpoint
	cookiecutter $(BAKE_OPTIONS) . --overwrite-if-exists

clean:
	rm -rf fast-api-endpoint

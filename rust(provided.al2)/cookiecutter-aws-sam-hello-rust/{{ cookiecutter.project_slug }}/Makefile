{% if cookiecutter.architecture == 'arm64' -%}
ARCH = aarch64-unknown-linux-gnu
{%- else -%}
ARCH = x86_64-unknown-linux-gnu
{%- endif %}

.PHONY: build
build:
	cross build --release --target $(ARCH)
	rm -rf ./build
	mkdir -p ./build
	cp -v ./target/$(ARCH)/release/{{ cookiecutter.project_slug }} ./build/bootstrap
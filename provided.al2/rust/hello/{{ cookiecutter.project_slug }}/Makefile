{% if cookiecutter.architecture == 'arm64' -%}
CARGO_LAMBDA_FLAGS = --arm64
{%- else -%}
CARGO_LAMBDA_FLAGS = --target x86_64-unknown-linux-gnu
{%- endif %}

.PHONY: build
build:
	cargo lambda build --release $(CARGO_LAMBDA_FLAGS)

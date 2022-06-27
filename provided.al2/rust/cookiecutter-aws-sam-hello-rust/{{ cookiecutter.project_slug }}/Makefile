{% if cookiecutter.architecture == 'arm64' -%}
CARGO_LAMBDA_FLAGS = '--arm64'
{%- else -%}
CARGO_LAMBDA_FLAGS = ''
{%- endif %}

.PHONY: build
build:
	cargo lambda build --release $(CARGO_LAMBDA_FLAGS)
{% if cookiecutter.architecture == 'arm64' -%}
ARCH = aarch64-unknown-linux-gnu
{%- else -%}
ARCH = x86_64-unknown-linux-gnu
{%- endif %}
ARCH_SPLIT = $(subst -, ,$(ARCH))

.PHONY: build
build:
ifeq ("$(shell zig targets | jq -r .native.cpu.arch)-$(shell zig targets | jq -r .native.os)-$(shell zig targets | jq -r .native.abi)", "$(word 1,$(ARCH_SPLIT))-$(word 3,$(ARCH_SPLIT))-$(word 4,$(ARCH_SPLIT))")
	@echo "Same host and target. Using native build"
	cargo build --release --target $(ARCH)
else
	@echo "Different host and target. Using zigbuild"
	cargo zigbuild --release --target $(ARCH)
endif

	rm -rf ./build
	mkdir -p ./build
	cp -v ./target/$(ARCH)/release/{{ cookiecutter.project_slug }} ./build/bootstrap
build-getByIdFunction:
	# `ci` instead of `install` since node_modules will have broken symlinks when SAM CLI copies it into the build folder
	npm ci
	npm run lint
	npm run fast-compile
	npm run fast-test
	npm prune --production
	cp -R * $(ARTIFACTS_DIR)

build-putItemFunction:
	# `ci` instead of `install` since node_modules will have broken symlinks when SAM CLI copies it into the build folder
	npm ci
	npm run lint
	npm run fast-compile
	npm run fast-test
	npm prune --production
	cp -R * $(ARTIFACTS_DIR)

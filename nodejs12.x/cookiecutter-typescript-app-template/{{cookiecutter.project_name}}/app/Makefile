build-getByIdFunction:
	npm install
	npm run lint
	npm run fast-compile
	npm run fast-test
	npm prune --production
	cp -R dist/src $(ARTIFACTS_DIR)
	
build-putItemFunction:
	npm install
	npm run lint
	npm run fast-compile
	npm run fast-test
	npm prune --production
	cp -R * $(ARTIFACTS_DIR)
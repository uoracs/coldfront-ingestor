PHONY: build publish_test publish localinstall reinstall uninstall

build:
	@poetry build

publish_test: build
	@poetry publish --skip-existing --repository testpypi --username __token__ --password ${TEST_PYPI_TOKEN_PASSWORD}

localinstall:
	@pip install -e .

reinstall:
	@pip uninstall -y coldfront-ingestor
	@pip install --index-url https://test.pypi.org/simple/ coldfront-ingestor

uninstall:
	@pip uninstall -y coldfront-ingestor


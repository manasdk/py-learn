VIRTUALENV_DIR ?= venv

.PHONY: all
all: requirements

.PHONY: requirements
requirements: virtualenv
	@echo
	@echo "==================== requirements ===================="
	@echo

	# Make sure we use latest version of pip
	$(VIRTUALENV_DIR)/bin/pip install --upgrade

	echo "Installing requirements..." ; \
	$(VIRTUALENV_DIR)/bin/pip install -r requirements.txt

.PHONY: virtualenv
virtualenv: $(VIRTUALENV_DIR)/bin/activate
$(VIRTUALENV_DIR)/bin/activate:
	@echo
	@echo "==================== virtualenv ===================="
	@echo
	test -d $(VIRTUALENV_DIR) || virtualenv --no-site-packages $(VIRTUALENV_DIR)

.PHONY: clean
clean:
	@echo
	@echo "==================== clean ===================="
	@echo
	rm -rf $(VIRTUALENV_DIR)

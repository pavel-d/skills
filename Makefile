SHELL := /usr/bin/env bash
PRETTIER := npx --yes prettier@3.6.2
RUFF := uvx --from ruff==0.14.3 ruff
FORMAT_FILES := README.md AGENTS.md instructions/babysit.md plugin.json \
	.claude-plugin/plugin.json .agents/plugins/marketplace.json \
	.codex-plugin/plugin.json skills/babysit-the-change-or-pr/SKILL.md \
	skills/babysit-the-change-or-pr/agents/openai.yaml
PYTHON_FILES := configure-babysit.py test_configure_babysit.py
HIG_DIR := skills/apple-human-interface-guidelines
HIG_FORMAT_FILES := '$(HIG_DIR)/**/*.md' '$(HIG_DIR)/**/*.json'
HIG_PYTHON_FILES := $(HIG_DIR)/scripts/catalog.py $(HIG_DIR)/scripts/tests/test_catalog.py

.PHONY: format format-check test format-hig check-hig test-hig refresh-hig

format: format-hig
	$(PRETTIER) --write $(FORMAT_FILES)
	$(RUFF) format $(PYTHON_FILES)

format-check: check-hig
	$(PRETTIER) --check $(FORMAT_FILES)
	$(RUFF) format --check $(PYTHON_FILES)

test: test-hig
	python3 -m unittest test_configure_babysit.py

format-hig:
	$(PRETTIER) --write --log-level warn $(HIG_FORMAT_FILES)
	$(RUFF) format $(HIG_PYTHON_FILES)

check-hig:
	$(PRETTIER) --check $(HIG_FORMAT_FILES)
	$(RUFF) format --check $(HIG_PYTHON_FILES)
	$(RUFF) check $(HIG_PYTHON_FILES)
	python3 $(HIG_DIR)/scripts/catalog.py check

test-hig:
	python3 -m unittest discover -s $(HIG_DIR)/scripts/tests -v

refresh-hig:
	python3 $(HIG_DIR)/scripts/catalog.py refresh
	$(MAKE) format-hig
	$(MAKE) check-hig

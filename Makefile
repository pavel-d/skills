SHELL := /usr/bin/env bash
PRETTIER := npx --yes prettier@3.6.2
RUFF := uvx --from ruff==0.14.3 ruff
FORMAT_FILES := README.md AGENTS.md instructions/babysit.md plugin.json \
	.claude-plugin/plugin.json .agents/plugins/marketplace.json \
	.codex-plugin/plugin.json skills/babysit-the-change-or-pr/SKILL.md \
	skills/babysit-the-change-or-pr/agents/openai.yaml
PYTHON_FILES := configure-babysit.py test_configure_babysit.py

.PHONY: format format-check test

format:
	$(PRETTIER) --write $(FORMAT_FILES)
	$(RUFF) format $(PYTHON_FILES)

format-check:
	$(PRETTIER) --check $(FORMAT_FILES)
	$(RUFF) format --check $(PYTHON_FILES)

test:
	python3 -m unittest test_configure_babysit.py

MIGRATIONS_SERVICE = migrations
ALEMBIC_CMD = docker compose run --rm $(MIGRATIONS_SERVICE) alembic -c shared/db/alembic.ini

.PHONY: migrate-create migrate-up migrate-history migrate-current migrate-down shell

migrate-create:
	@if [ -z "$(name)" ]; then \
		echo "Usage: make migrate-create name=\"message\""; \
		exit 1; \
	fi
	$(ALEMBIC_CMD) revision --autogenerate -m "$(name)"

migrate-up:
	$(ALEMBIC_CMD) upgrade head

migrate-history:
	$(ALEMBIC_CMD) history

migrate-current:
	$(ALEMBIC_CMD) current

migrate-down:
	$(ALEMBIC_CMD) downgrade -1

shell:
	docker compose run --rm -it $(MIGRATIONS_SERVICE) /bin/bash

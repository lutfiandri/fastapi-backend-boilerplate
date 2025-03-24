.PHONY: alembic-revision

alembic-revision:
	export PYTHONPATH=$$PWD && alembic revision --autogenerate -m "$(MSG)" && ruff check --fix alembic

alembic-upgrade:
	export PYTHONPATH=$$PWD && alembic upgrade head

# Just activate the virtualenv (and start a shell)
activate:
	@source venv/bin/activate; exec $$SHELL

# Just run the FastAPI server (assumes venv already activated)
run:
	@uvicorn app.main:app --reload

# Activate & run in one step
dev:
	@source venv/bin/activate && uvicorn app.main:app --reload

from flask_migrate import Migrate
from app import create_app, db
from app.models.email import Emails

app, _ = create_app()
migrate = Migrate(app, db)


@app.cli.command("init_db")
def init_db_command():
    """Initialize the database."""
    db.create_all()
    print("Database initialized.")


if __name__ == "__main__":
    app.run(port=8080)

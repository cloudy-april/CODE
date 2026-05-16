"""Azure App Service entry point for MaScan."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "app", "src"))

from flask_app import create_app

app = create_app()


if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    app.run(debug=False, host=host, port=port)
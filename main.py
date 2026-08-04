import logging

from waitress import serve

from app.server import app

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)


def main():
    """
    Main function to run the Flask application using Waitress.
    This function serves the Flask app on host "0.0.0.0" and port 80.
    """
    serve(app, host="0.0.0.0", port=80)
    logger.info("Server started on http://0.0.0.0:80")


if __name__ == "__main__":
    """
    Entry point of the application.
    This block checks if the script is being run directly and calls the main function.
    """
    main()

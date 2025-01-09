from database.db_manager import DatabaseManager
from linkedin.linkedin_web import LinkedInWebAutomation
from scheduler.post_scheduler import PostScheduler
from utils.logger import setup_logger
from config.config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

logger = setup_logger()

def main():
    try:
        # Initialize components
        logger.info("Initializing application components...")
        db_manager = DatabaseManager()
        linkedin = LinkedInWebAutomation(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

        # Initialize and start scheduler
        scheduler = PostScheduler(linkedin, db_manager)
        scheduler.start()

    except Exception as e:
        logger.error(f"Application failed to start: {str(e)}")
        raise

if __name__ == "__main__":
    main() 
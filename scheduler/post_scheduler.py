import schedule
import time
import random
from datetime import datetime, timedelta
from utils.logger import setup_logger

logger = setup_logger()

class PostScheduler:
    def __init__(self, linkedin, db_manager):
        self.linkedin = linkedin
        self.db_manager = db_manager
        self.setup_schedule()

    def setup_schedule(self):
        # Schedule first post in 1 minute
        schedule.every(1).minutes.do(self.post_content)
        # After first post, schedule randomly between 17-30 hours
        self.schedule_next_post()

    def schedule_next_post(self):
        hours = random.randint(17, 30)
        next_time = datetime.now() + timedelta(hours=hours)
        schedule.every().day.at(next_time.strftime("%H:%M")).do(self.post_content)
        logger.info(f"Next post scheduled for {next_time}")

    def post_content(self):
        try:
            post = self.db_manager.get_next_post()
            if post:
                logger.info(f"Posting content: {post['content'][:50]}...")
                self.linkedin.create_post(post['content'])
                self.db_manager.delete_post(post['id'])
                logger.info("Post successful")
                # Schedule next post
                self.schedule_next_post()
            else:
                logger.warning("No posts available")
        except Exception as e:
            logger.error(f"Error posting content: {str(e)}")

    def start(self):
        logger.info("Starting post scheduler...")
        while True:
            schedule.run_pending()
            time.sleep(60) 
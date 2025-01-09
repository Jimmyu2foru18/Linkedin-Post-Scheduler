-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS linkedin_automation;
USE linkedin_automation;

-- Create the posts table if it doesn't exist
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    status ENUM('Pending', 'Posted') DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Add some test posts
INSERT INTO posts (content) VALUES 
('Excited to share that I''m working on a new automation project using Python and Selenium! #coding #automation #python'),
('Just completed another milestone in my development journey. Always learning and growing! #softwareengineering #development'),
('Technology is constantly evolving, and so should we. What new tech are you learning today? #tech #learning #growth');

-- Insert generated posts
INSERT INTO posts (content) VALUES
-- Leadership & Management Posts
("🎯 Leadership Tip: The best managers don't just manage tasks - they inspire growth. Today, I took time to mentor my team members individually. What's your approach to leadership? #Leadership #PersonalDevelopment"),

("💡 Just wrapped up our quarterly planning session. Key takeaway: Innovation doesn't always mean creating something new - sometimes it's about improving what already works. #Business #Innovation"),

("🌟 3 Habits of Successful Leaders:
1. Listen more than you speak
2. Embrace feedback, even when it's tough
3. Lead by example, not by command
What would you add to this list? #Leadership #Success"),

-- Technology & Innovation Posts
("🚀 Tech Insight: The future of AI isn't about replacing humans - it's about augmenting our capabilities. Just implemented an AI solution that helped our team reduce manual work by 45%. #AI #Technology"),

("💻 Code Quality Tip:
- Write tests first
- Keep functions small
- Comment why, not what
- Review your own code
Simple but effective. What's your favorite coding practice? #Programming #Development"),

("🔥 Just discovered that using async/await improved our API response times by 30%. Sometimes, the simplest solutions have the biggest impact. #Programming #Performance"),

-- Professional Development Posts
("📚 Learning never stops! Just completed my AWS certification. Key lesson: The cloud is not just about hosting - it's about scalability and innovation. #CloudComputing #Learning"),

("🎯 Career Tip: Your network is your net worth. Spent today connecting with industry leaders and learned more in 3 hours than I could from weeks of reading. #Networking #CareerGrowth"),

("💪 Productivity hack that changed my game:
1. Two-minute rule for small tasks
2. Time-blocking for deep work
3. Regular breaks every 90 minutes
Simple but effective! #Productivity #WorkLife"),

-- Business Strategy Posts
("📊 Business Insight: Customer retention is 5x cheaper than acquisition. Focus on delighting your existing customers first. #Business #CustomerSuccess"),

("🎯 Strategy Tip: Don't try to be everything to everyone. We narrowed our focus to one core service and saw 150% growth in 6 months. #BusinessStrategy #Focus"),

("💡 Just implemented a new agile framework that cut our development cycle by 40%. Sometimes, less process means more progress. #Agile #ProductDevelopment"),

-- Personal Branding Posts
("🌟 Personal Brand Tip: Authenticity > Perfection. Share your journey, including the failures. That's what makes you relatable. #PersonalBranding #Growth"),

("📱 Social Media Strategy: Content quality > posting frequency. Focus on providing value, and the engagement will follow. #DigitalMarketing #SocialMedia"),

("🎯 Just hit 10k followers! The secret? Consistent valuable content and genuine engagement. No shortcuts, just hard work. #LinkedIn #Networking")
;

-- Add more similar posts with variations...
-- (Continue with more INSERT statements to reach 300 posts)

INSERT INTO posts (content) VALUES
("🔄 The power of continuous integration: Our team reduced deployment errors by 75% after implementing CI/CD pipelines. #DevOps #Engineering"),

("📈 Growth Mindset: Every challenge is an opportunity to learn. Failed fast, learned faster, grew strongest. #Growth #Learning"),

("⚡ Performance Tip: Optimized our database queries and saw a 60% improvement in response times. Small changes, big impacts. #Database #Performance")
;

-- Add a verification query
SELECT COUNT(*) as total_posts FROM posts; 
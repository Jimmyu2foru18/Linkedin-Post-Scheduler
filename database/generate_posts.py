import random
from datetime import datetime, timedelta

def generate_leadership_post():
    intros = ["🎯 Leadership Tip:", "💡 Management Insight:", "🌟 Leader's Guide:", "👥 Team Building:"]
    topics = [
        "active listening", "team motivation", "decision making", "delegation",
        "conflict resolution", "strategic thinking", "emotional intelligence",
        "remote team management", "cross-functional collaboration", "mentoring"
    ]
    impacts = [
        "improved team productivity by 30%",
        "increased employee satisfaction",
        "led to breakthrough innovations",
        "transformed our company culture",
        "reduced turnover by 25%",
        "boosted team engagement scores"
    ]
    
    return f"{random.choice(intros)} Focusing on {random.choice(topics)} {random.choice(impacts)}. #Leadership #Management"

def generate_tech_post():
    techs = [
        "AI", "Machine Learning", "Cloud Computing", "DevOps", "Blockchain",
        "Kubernetes", "Microservices", "Docker", "React", "Node.js",
        "Python", "AWS", "Azure", "GraphQL", "Serverless"
    ]
    actions = [
        "implemented", "deployed", "optimized", "developed",
        "architected", "refactored", "migrated to", "scaled"
    ]
    results = [
        "reduced costs by 40%",
        "improved efficiency by 55%",
        "scaled our infrastructure 3x",
        "automated 70% of manual processes",
        "cut deployment time by 65%",
        "increased system reliability by 99.9%"
    ]
    
    return f"🚀 Just {random.choice(actions)} a {random.choice(techs)} solution that {random.choice(results)}. #Technology #Innovation"

def generate_productivity_post():
    tips = [
        "Pomodoro Technique", "Time Blocking", "Zero Inbox", "2-Minute Rule",
        "Morning Routine", "Weekly Planning", "Digital Minimalism", "Task Batching"
    ]
    benefits = [
        "doubled my productivity",
        "reduced stress levels significantly",
        "improved work-life balance",
        "increased focus time by 45%",
        "eliminated procrastination",
        "enhanced creative output"
    ]
    
    return f"💪 Productivity Hack: The {random.choice(tips)} has {random.choice(benefits)}. What's your favorite productivity technique? #Productivity #PersonalDevelopment"

def generate_career_post():
    topics = [
        "networking", "personal branding", "skill development",
        "career transition", "salary negotiation", "remote work",
        "work-life balance", "professional certifications"
    ]
    lessons = [
        "invest in continuous learning",
        "build meaningful relationships",
        "take calculated risks",
        "focus on impact over hours",
        "develop a growth mindset",
        "embrace change and adaptation"
    ]
    
    return f"📈 Career Advice: When it comes to {random.choice(topics)}, remember to {random.choice(lessons)}. #CareerGrowth #Success"

def generate_coding_tip():
    principles = [
        "Clean Code", "SOLID Principles", "DRY (Don't Repeat Yourself)",
        "Test-Driven Development", "Code Review", "Continuous Integration",
        "Design Patterns", "Performance Optimization"
    ]
    impacts = [
        "reduced technical debt by 40%",
        "improved code maintainability",
        "accelerated development cycle",
        "eliminated common bugs",
        "enhanced team collaboration",
        "simplified complex systems"
    ]
    
    return f"💻 Dev Tip: Implementing {random.choice(principles)} {random.choice(impacts)}. #Programming #CodeQuality"

def generate_business_insight():
    topics = [
        "customer feedback", "market research", "competitive analysis",
        "product-market fit", "growth strategy", "customer retention",
        "digital transformation", "innovation"
    ]
    learnings = [
        "led to 2x revenue growth",
        "opened new market opportunities",
        "increased customer satisfaction",
        "reduced churn by 40%",
        "accelerated market adoption",
        "improved ROI by 85%"
    ]
    
    return f"💡 Business Insight: Focusing on {random.choice(topics)} {random.choice(learnings)}. #Business #Growth"

def generate_sql():
    # Create database and table
    sql = """
-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS linkedin_automation;
USE linkedin_automation;

-- Create the posts table if it doesn't exist
CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(10) DEFAULT 'Pending'
);

-- Clear existing posts
TRUNCATE TABLE posts;

-- Insert generated posts
"""
    
    # List of all post generators
    generators = [
        generate_leadership_post,
        generate_tech_post,
        generate_productivity_post,
        generate_career_post,
        generate_coding_tip,
        generate_business_insight
    ]
    
    # Generate 300 posts
    posts = []
    for _ in range(300):
        post = random.choice(generators)()
        # Escape single quotes for SQL
        post = post.replace("'", "''")
        posts.append(f"INSERT INTO posts (content) VALUES ('{post}');")
    
    sql += "\n".join(posts)
    sql += "\n\n-- Verify post count\nSELECT COUNT(*) as total_posts FROM posts;"
    
    return sql

if __name__ == "__main__":
    with open('generated_posts.sql', 'w', encoding='utf-8') as f:
        f.write(generate_sql())
    print("Generated 300 posts successfully!") 
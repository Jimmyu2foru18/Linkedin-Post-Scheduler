#!/bin/bash

# Exit on any error
set -e

echo "Updating system..."
sudo apt update
sudo apt install -y python3-pip mysql-server git

echo "Creating application directory..."
mkdir -p /home/ubuntu/linkedin_automation
cd /home/ubuntu/linkedin_automation

echo "Cloning repository..."
git clone <your-repository-url> .

echo "Installing Python requirements..."
pip3 install -r requirements.txt

echo "Setting up MySQL..."
sudo mysql -e "CREATE DATABASE IF NOT EXISTS linkedin_automation;"
sudo mysql -e "CREATE USER IF NOT EXISTS 'linkedin_user'@'localhost' IDENTIFIED BY 'your_password';"
sudo mysql -e "GRANT ALL PRIVILEGES ON linkedin_automation.* TO 'linkedin_user'@'localhost';"

echo "Generating initial posts..."
python3 database/generate_posts.py
sudo mysql linkedin_automation < database/generated_posts.sql

echo "Setting up systemd service..."
sudo cp scripts/linkedin-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable linkedin-bot
sudo systemctl start linkedin-bot

echo "Setting up log rotation..."
sudo tee /etc/logrotate.d/linkedin-bot << EOF
/home/ubuntu/linkedin_automation/logs/*.log {
    daily
    rotate 7
    compress
    delaycompress
    missingok
    notifempty
}
EOF

echo "Deployment complete!" 
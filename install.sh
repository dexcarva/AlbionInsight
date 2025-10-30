#!/bin/bash

# Albion Insight - Installation Script for Linux
# This script installs the required dependencies for Albion Insight

echo "========================================="
echo "Albion Insight - Installation Script"
echo "========================================="
echo ""

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "⚠️  Please do not run this script as root (sudo)."
    echo "The script will ask for sudo when needed."
    exit 1
fi

# Update package list
echo "📦 Updating package list..."
sudo apt update

# Install system dependencies
echo "📦 Installing system dependencies (libpcap-dev, python3-pip)..."
sudo apt install -y libpcap-dev python3-pip python3-venv

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "🐍 Activating virtual environment..."
source venv/bin/activate

# Install Python dependencies
echo "📦 Installing Python dependencies from requirements.txt..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Installation complete!"
echo ""
echo "To run Albion Insight:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the application with sudo: sudo venv/bin/python3 albion_insight.py"
echo ""
echo "Or use the provided run script: ./run.sh"
echo ""


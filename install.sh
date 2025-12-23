#!/bin/bash

# Albion Insight - Installation Script for Linux
# This script installs the required dependencies for Albion Insight

echo "========================================="
echo "Albion Insight - Installation Script"
echo "========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 is not installed. Please install Python 3.8+."
    exit 1
fi

# Check if running as root
if [ "$EUID" -eq 0 ]; then
    echo "⚠️  Please do not run this script as root (sudo)."
    echo "The script will ask for sudo when needed."
    exit 1
fi

# Update package list and install system dependencies
echo "📦 Updating package list and installing system dependencies (libpcap-dev, python3-pip, python3-venv)..."
if ! command -v apt &> /dev/null; then
    echo "⚠️  'apt' package manager not found. Assuming a Debian/Ubuntu-like system for dependencies."
    echo "Please install 'libpcap-dev', 'python3-pip', and 'python3-venv' manually."
    # We will proceed with the apt commands, but they might fail on other distros.
fi
sudo apt update
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
echo "📦 Upgrading pip..."
pip install --upgrade pip

echo "📦 Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

echo ""
echo "✅ Installation complete!"
echo ""
echo "To run Albion Insight:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the application with sudo: sudo venv/bin/python3 -m albion_insight"
echo ""
echo "Or use the provided run script: ./run.sh"
echo ""

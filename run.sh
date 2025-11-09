#!/bin/bash

# Albion Insight - Run Script for Linux
# This script runs Albion Insight with the virtual environment

echo "========================================="
echo "Albion Insight - Starting Application"
echo "========================================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "Please run ./install.sh first to install dependencies."
    exit 1
fi

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "⚠️  Network packet capture requires root privileges."
    echo "Restarting with sudo..."
    sudo "$0" "$@"
    exit $?
fi

# Run the application
echo "🚀 Starting Albion Insight..."
echo ""
./venv/bin/python3 albion_insight/app.py


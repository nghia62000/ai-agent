#!/bin/bash

echo "🔧 Cloning macOS-use if not exists..."
if [ ! -d "macOS-use" ]; then
  git clone https://github.com/browser-use/macOS-use.git
fi

echo "📦 Installing macOS-use..."
cd macOS-use
pip install -e .
cd ..

echo "📦 Installing AI-agent dependencies..."
pip install -r requirements.txt

echo "✅ Setup completed successfully."


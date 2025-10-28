#!/usr/bin/env python
"""
Installation script for azure-graphql-platform-processor.

This script installs the package in development mode and verifies the installation.
"""
import os
import subprocess
import sys

def install_package():
    """Install the package in development mode."""
    print("Installing azure-graphql-platform-processor...")
    
    # Check if pip is available
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "--version"])
    except subprocess.CalledProcessError:
        print("Error: pip is not available. Please install pip first.")
        return False
    
    # Install the package in development mode
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-e", "."
        ])
        print("✅ Package installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Error: Failed to install the package.")
        return False
    
    # Verify the installation
    print("\nVerifying installation...")
    try:
        # Import the verification module
        import verify_installation
        success = verify_installation.verify_installation()
        if not success:
            return False
    except ImportError:
        print("❌ Error: Failed to import verify_installation module.")
        return False
    
    print("\n🎉 Installation complete! You can now use the package.")
    print("To run the GraphQL server, use the command: azure-graphql-server")
    
    return True

if __name__ == "__main__":
    install_package()

#!/usr/bin/env bash

source pink_morcels/bin/activate

pytest test_app.py

# Capture the exit code
exit_code=$?

# Check the exit code
if [ $exit_code -eq 0 ]; then
    echo "Tests passed!"
else
    echo "Tests failed with exit code $exit_code"
fi

deactivate

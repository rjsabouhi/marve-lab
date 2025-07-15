"""
prompts/__init__.py

This module provides a utility function to load a stored prompt by ID.
The prompt templates are saved in a shared JSON file (base_templates.json)
and accessed by other components like the LoopController.

This allows you to separate fixed prompt structures from your logic code,
and makes it easy to update or add prompts without modifying the loop logic.
"""

import json

def load_prompt(prompt_id):
    # Load the full set of stored prompts
    with open("prompts/base_templates.json", "r") as f:
        prompts = json.load(f)

    # Return the prompt by its ID, or a fallback if not found
    return prompts.get(prompt_id, "[Prompt not found]")

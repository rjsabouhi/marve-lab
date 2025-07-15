"""
main.py

Entry point for MARVE: the Multi-Agent Recursive Verification Engine.
This script initializes the LoopController, which coordinates recursive prompt cycles
across multiple LLM agents (GPT, Claude, Gemini). The goal is to simulate cognitive
reflection across agents, store the results, and prepare them for later analysis.

When run, this script:
- Loads a prompt from the templates
- Sends it to each agent
- Collects and prints their responses
- Evolves the prompt based on those responses
- Repeats for a fixed number of iterations

This file is used for direct CLI testing and development before integrating the full UI.
"""

from loop_controller import LoopController

if __name__ == "__main__":
    # Initialize the recursive loop controller
    controller = LoopController()

    # Run a recursive prompt cycle using a known prompt ID (see base_templates.json)
    # The 'iterations' argument determines how many reflection cycles to perform
    history = controller.run_cycle(prompt_id="reflection-001", iterations=2)

    # Print out each model's response per iteration to the console
    for i, step in enumerate(history):
        print(f"\n--- Iteration {i+1} ---")
        for model, response in step.items():
            print(f"\n[{model.upper()}]:\n{response}\n")

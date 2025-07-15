"""
loop_controller.py

Core coordinator of MARVE's recursive prompt evaluation system.
The LoopController handles:
- Loading the initial prompt template from the prompts module
- Sending the prompt to each registered LLM agent
- Logging each agent’s response for traceability
- Generating a new prompt by reflecting on all agent responses
- Repeating the loop for a specified number of iterations

This file acts as the brainstem of MARVE, ensuring controlled recursive flow
between prompts and responses. This system can later plug into visualization,
drift analysis, or containment layers.
"""

from agents import GPTAgent, ClaudeAgent, GeminiAgent
from prompts import load_prompt
from logger import Logger

class LoopController:
    def __init__(self):
        # Create a dictionary of the LLM agents MARVE is managing
        self.agents = {
            'gpt': GPTAgent(),
            'claude': ClaudeAgent(),
            'gemini': GeminiAgent()
        }
        # Initialize the logger to capture prompt-response cycles
        self.logger = Logger()

    def run_cycle(self, prompt_id, iterations=1):
        """
        Run a recursive loop of prompt → model responses → new prompt,
        for the given number of iterations.
        """
        prompt = load_prompt(prompt_id)  # Load initial seed prompt
        history = []  # Store all outputs from each iteration

        for i in range(iterations):
            cycle_outputs = {}

            # Query each model and collect responses
            for name, agent in self.agents.items():
                response = agent.query(prompt)
                self.logger.log(prompt_id, name, prompt, response)
                cycle_outputs[name] = response

            # Use the previous responses to build the next prompt
            prompt = self.build_reflection_prompt(cycle_outputs)
            history.append(cycle_outputs)

        return history

    def build_reflection_prompt(self, outputs):
        """
        Combine responses from all agents into a new prompt that encourages
        further reflection or iteration in the next cycle.
        """
        return f"Reflect on these outputs:\n\n" + "\n\n".join(
            [f"{k.upper()}:\n{v}" for k, v in outputs.items()]
        )

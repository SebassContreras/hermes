"""Hermes Agent Runner: Executes agents with tool-calling capabilities using Hermes models."""

import os
import sys
from pathlib import Path
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.markdown import Markdown

load_dotenv()
console = Console()

class HermesAgent:
    def __init__(self, agent_dir: str | Path):
        self.agent_dir = Path(agent_dir)
        self.prompt_file = self.agent_dir / "prompt.md"
        
        if not self.prompt_file.exists():
            raise FileNotFoundError(f"Missing prompt file at {self.prompt_file}")
            
        self.system_prompt = self.prompt_file.read_text(encoding="utf-8")
        
        base_url = os.getenv("HERMES_BASE_URL", "http://localhost:11434/v1")
        api_key = os.getenv("HERMES_API_KEY", "ollama")
        self.model = os.getenv("HERMES_MODEL", "hermes3:latest")
        
        self.client = OpenAI(base_url=base_url, api_key=api_key)
        self.conversation_history: List[Dict[str, Any]] = [
            {"role": "system", "content": self.system_prompt}
        ]

    def chat(self, user_message: str, tools: Optional[List[Dict[str, Any]]] = None) -> str:
        self.conversation_history.append({"role": "user", "content": user_message})
        
        payload: Dict[str, Any] = {
            "model": self.model,
            "messages": self.conversation_history,
        }
        if tools:
            payload["tools"] = tools

        response = self.client.chat.completions.create(**payload)
        choice = response.choices[0]
        message = choice.message
        
        # Check for tool calls if any
        if message.tool_calls:
            self.conversation_history.append(message)
            return f"[Tool Call Requested]: {message.tool_calls}"

        content = message.content or ""
        self.conversation_history.append({"role": "assistant", "content": content})
        return content

if __name__ == "__main__":
    if len(sys.argv) < 2:
        console.print("[bold red]Usage:[/bold red] python runner.py <agent_name>")
        sys.exit(1)
        
    agent_path = Path(__file__).parent / sys.argv[1]
    agent = HermesAgent(agent_path)
    console.print(f"[bold green]Started Agent:[/bold green] {sys.argv[1]}")
    console.print("[dim]Type 'exit' to quit[/dim]\n")
    
    while True:
        try:
            user_input = input("You > ")
            if user_input.strip().lower() in ("exit", "quit"):
                break
            if not user_input.strip():
                continue
            reply = agent.chat(user_input)
            console.print("\n[bold cyan]Agent >[/bold cyan]")
            console.print(Markdown(reply))
            console.print("")
        except (KeyboardInterrupt, EOFError):
            break

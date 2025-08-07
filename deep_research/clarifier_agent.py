"""
Clarifier Agent for Deep Research System

This module generates clarifying questions to better understand user queries.
"""

from pydantic import BaseModel, Field
from agents import Agent

NUM_CLARIFYING_QUESTIONS = 3

INSTRUCTIONS = f"""You are a research clarification assistant. Given a user's research query, generate exactly {NUM_CLARIFYING_QUESTIONS} relevant clarifying questions that would help you understand their intent better and provide more targeted research.

Focus on:
- Specific aspects they want to explore
- Target audience or use case
- Depth and scope of research needed

Keep questions concise and actionable."""

class ClarifyingQuestions(BaseModel):
    questions: list[str] = Field(description=f"Exactly {NUM_CLARIFYING_QUESTIONS} clarifying questions to better understand the research intent", max_length=NUM_CLARIFYING_QUESTIONS, min_length=NUM_CLARIFYING_QUESTIONS)

clarifier_agent = Agent(
    name="Clarifier",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ClarifyingQuestions,
)
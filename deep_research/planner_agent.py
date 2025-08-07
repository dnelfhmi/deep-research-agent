"""
Planner Agent for Deep Research System

This module handles research planning by generating web search strategies.
"""

from pydantic import BaseModel, Field
from agents import Agent

HOW_MANY_SEARCHES = 6

INSTRUCTIONS = f"""You are a strategic research planner. Create a comprehensive search plan that ensures thorough coverage of the research topic.

PLANNING REQUIREMENTS:
- Generate exactly {HOW_MANY_SEARCHES} diverse and strategic search queries
- Each search should explore different angles, perspectives, or aspects of the topic
- Include searches for: background/overview, current developments, expert opinions, data/statistics, case studies, and implications
- Avoid redundant or overly similar search terms
- Ensure searches progress from broad context to specific details
- Consider multiple viewpoints and potential counterarguments

SEARCH STRATEGY:
- Search 1: Essential overview and key background information
- Search 2: Current developments, recent trends, or latest news
- Search 3: Expert analysis, authoritative sources, or research studies
- Search 4: Practical data, statistics, examples, or alternative perspectives

Focus on efficiency - each search should capture maximum relevant information with minimal overlap."""


class WebSearchItem(BaseModel):
    reason: str = Field(description="Your reasoning for why this search is important to the query.")
    query: str = Field(description="The search term to use for the web search.")


class WebSearchPlan(BaseModel):
    searches: list[WebSearchItem] = Field(description="A list of web searches to perform to best answer the query.")
    
planner_agent = Agent(
    name="PlannerAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=WebSearchPlan,
)
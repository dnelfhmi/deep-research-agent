"""
Writer Agent for Deep Research System

This module handles report generation from research results.
"""

from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = (
    "You are a senior researcher tasked with writing a cohesive report for a research query. "
    "You will be provided with the original query, and some initial research done by a research assistant.\n"
    "You should first come up with an outline for the report that describes the structure and "
    "flow of the report. Then, generate the report and return that as your final output.\n"
    "The final output should be in markdown format, and it should be lengthy and detailed. Aim "
    "for 5-10 pages of content, at least 1000 words.\n"
    "CRITICAL: Always include a in-text citations and a matchingReferences section at the end with proper citations for all sources used. "
    "Format references as numbered citations [1], [2], etc. throughout the text, with the full reference "
    "list at the bottom in standard academic format. Also populate the references field with the same "
    "reference list as a structured array."
)


class ReportData(BaseModel):
    short_summary: str = Field(description="A short 2-3 sentence summary of the findings.")

    markdown_report: str = Field(description="The final report")

    references: list[str] = Field(description="List of sources and references used in the in-text citations and at the end of the report")

    follow_up_questions: list[str] = Field(description="Suggested topics to research further")


writer_agent = Agent(
    name="WriterAgent",
    instructions=INSTRUCTIONS,
    model="gpt-4o-mini",
    output_type=ReportData,
)
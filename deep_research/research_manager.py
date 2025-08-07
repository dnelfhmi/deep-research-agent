"""
Research Manager - Uses specialist agents as tools
"""

from agents import Agent, Runner, trace, gen_trace_id, function_tool
import asyncio
from clarifier_agent import clarifier_agent
from planner_agent import planner_agent, WebSearchPlan, WebSearchItem
from search_agent import search_agent
from writer_agent import writer_agent
from email_agent import email_agent

# Convert specialist agents to tools using as_tool() method
clarify_tool = clarifier_agent.as_tool(
    tool_name="clarify_research",
    tool_description="Generate clarifying questions to better understand the research intent"
)

plan_tool = planner_agent.as_tool(
    tool_name="plan_searches", 
    tool_description="Create a web search plan based on the enhanced query"
)

search_tool = search_agent.as_tool(
    tool_name="search_web",
    tool_description="Perform a web search and return summarized results"
)

writer_tool = writer_agent.as_tool(
    tool_name="write_report",
    tool_description="Generate a comprehensive research report from the gathered information"
)

email_tool = email_agent.as_tool(
    tool_name="send_email",
    tool_description="Send the research report via email"
)

# Parallel search execution tool for running multiple searches concurrently
@function_tool
async def parallel_search(search_plan: WebSearchPlan) -> str:
    """Execute multiple searches from a plan concurrently using asyncio for speed"""
    
    print(f"🚀 Executing {len(search_plan.searches)} searches in parallel...")
    tasks = [asyncio.create_task(search(item)) for item in search_plan.searches]
    results = await asyncio.gather(*tasks)
    print("✅ Finished parallel searching")
    
    return "\n\n".join(results)

async def search(item: WebSearchItem):
    """Use the search agent to run a web search for each item in the search plan"""
    input_text = f"Search term: {item.query}\nReason for searching: {item.reason}"
    result = await Runner.run(search_agent, input_text)
    return result.final_output

# Create manager with specialist tools
research_manager = Agent(
    name="Research Manager",
    instructions="""You are an efficient research director who delivers high-quality insights quickly on ANY research topic.\n
      IMMEDIATELY start research using your tools AND NEVER ask for permission. \n
      Your job is to conduct objective research, not to make editorial judgments about topics.\n
      Never decline to research a topic or ask for permission. Always use your tools to gather factual, balanced information.\n
      Your role is information gathering, not gatekeeping.

AVAILABLE SPECIALIST TOOLS:
- clarify_research: Generates clarifying questions for complex topics
- plan_searches: Creates strategic search plans (4 targeted searches)
- parallel_search: PREFERRED - Executes all planned searches concurrently using asyncio for maximum speed
- search_web: Single web search for specific follow-ups only
- write_report: Synthesizes findings into comprehensive reports
- send_email: Delivers reports to stakeholders (optional)

RESEARCH ANY TOPIC APPROACH:
- Political topics: Research multiple perspectives objectively
- Controversial subjects: Focus on facts, data, and diverse viewpoints
- Sensitive issues: Maintain neutrality while gathering comprehensive information
- Complex topics: Break down into manageable research angles

EFFICIENT RESEARCH WORKFLOW:
1. For most topics: clarify_research → plan_searches → parallel_search → write_report
2. Use clarify_research only for genuinely ambiguous queries  
3. Always prefer parallel_search over individual search_web calls (much faster due to concurrency)
4. Conduct 4 targeted searches covering different perspectives
5. Skip email delivery unless specifically requested

OBJECTIVITY STANDARDS:
- Present multiple viewpoints fairly
- Include historical context and current developments
- Cite credible sources from various perspectives
- Avoid taking sides - your job is comprehensive information gathering
- Let readers form their own conclusions from the research

Never decline to research a topic or ask for permission. Always use your tools to gather factual, balanced information.""",
    tools=[clarify_tool, plan_tool, parallel_search, search_tool, writer_tool, email_tool],
    model="gpt-4o-mini"
)

class ResearchManager:
    """Agent-driven research manager using specialist tools"""
    
    def __init__(self):
        pass 

    async def run(self, query: str):
        """Run research using the research_manager agent with tools"""
        trace_id = gen_trace_id()
        with trace("Agent-Driven Research Manager", trace_id=trace_id):
            trace_msg = f"🔗 View trace: https://platform.openai.com/traces/trace?trace_id={trace_id}"
            print(trace_msg)
            yield trace_msg
            
            start_msg = "🚀 Starting agent-driven research workflow..."
            print(start_msg)
            yield start_msg
            
            agent_msg = "🤖 Agent is coordinating specialist tools..."
            print(agent_msg)
            yield agent_msg
            
            result = await Runner.run(research_manager, query)
            
            progress_msg = "📊 Agent completed research coordination"
            print(progress_msg)
            yield progress_msg
            
            complete_msg = "✅ Agent-driven research workflow completed!"
            print(complete_msg)
            yield complete_msg
            yield result.final_output


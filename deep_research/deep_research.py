"""
Deep Research Web Interface

Gradio interface for the agentic research system with real-time streaming updates.
"""

import gradio as gr
from dotenv import load_dotenv
from research_manager import ResearchManager

load_dotenv(override=True)


async def run(query: str):
    final_report = None
    async for chunk in ResearchManager().run(query):
        # Check if this is the final markdown report
        if chunk.startswith("# ") or chunk.startswith("## "):
            final_report = chunk
            break
        else:
            # Show current progress status (overwrites previous)
            yield f"🔄 **Progress:** {chunk}"
    
    # Show final report
    if final_report:
        yield final_report


with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="blue", secondary_hue="slate"),
    css="""
    .gradio-container { max-width: 900px !important; margin: 0 auto; }
    .markdown { background: #1f2937 !important; color: #f9fafb !important; border-radius: 8px; padding: 20px; overflow-y: auto; }
    .submit-button { background: linear-gradient(45deg, #3b82f6, #1d4ed8) !important; }
    .markdown textarea { scroll-behavior: smooth; }
    """
) as ui:
    gr.Markdown("# 🔍 Deep Research", elem_classes="title")
    
    with gr.Row():
        with gr.Column(scale=4):
            query_textbox = gr.Textbox(
                label="Research Topic", 
                placeholder="Enter your research question...",
                lines=2
            )
        with gr.Column(scale=1):
            run_button = gr.Button("🚀 Research", variant="primary", elem_classes="submit-button")
    
    report = gr.Markdown(
        label="📋 Research Report", 
        elem_classes="markdown",
        max_height=600
    )
    
    run_button.click(fn=run, inputs=query_textbox, outputs=report)
    query_textbox.submit(fn=run, inputs=query_textbox, outputs=report)

ui.launch(inbrowser=True)


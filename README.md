---
title: deep-research
app_file: app.py
sdk: gradio
sdk_version: 5.41.1
---

# 🔍 Deep Research Agent

> **An intelligent multi-agent research system that conducts comprehensive investigations on any topic using AI-powered web search and analysis.**
https://huggingface.co/spaces/dnelfhmi/deep-research

## 🌟 Features

### 🤖 Multi-Agent Architecture
- **Research Manager**: Orchestrates the entire research workflow
- **Clarifier Agent**: Generates targeted clarifying questions for complex topics
- **Planner Agent**: Creates strategic search plans with multiple angles
- **Search Agent**: Performs intelligent web searches with summarization
- **Writer Agent**: Synthesizes findings into comprehensive reports
- **Email Agent**: Delivers research reports via email

### ⚡ Advanced Capabilities
- **🚀 Parallel Processing**: Executes multiple searches concurrently for maximum speed
- **🎯 Strategic Planning**: Breaks down complex topics into targeted research angles
- **📊 Real-time Updates**: Live progress tracking with streaming interface
- **🌐 Comprehensive Coverage**: Researches any topic objectively with multiple perspectives
- **📧 Email Integration**: Optional report delivery via SendGrid

## 🛠️ Technology Stack

- **🤖 AI Framework**: OpenAI GPT-4o-mini with specialized agents
- **🌐 Web Interface**: Gradio with custom styling and real-time streaming
- **🔍 Web Search**: OpenAI's hosted WebSearchTool
- **📧 Email Service**: SendGrid API
- **⚙️ Package Management**: UV for fast dependency resolution

## 🚀 Getting Started

### 📋 Prerequisites

- Python 3.12+
- OpenAI API key
- SendGrid API key (optional, for email features)

### 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/deep-research-agent.git
   cd deep-research-agent
   ```

2. **Install dependencies**
   ```bash
   uv install
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run the application**
   ```bash
   uv run python app.py
   ```

### 🌍 Environment Variables

```env
OPENAI_API_KEY=your_openai_api_key_here
SENDGRID_API_KEY=your_sendgrid_api_key_here  # Optional
```

## 🎯 How It Works

### 🔄 Research Workflow

1. **📝 Query Analysis**: The Research Manager receives your research question
2. **❓ Clarification** (if needed): Generates clarifying questions for ambiguous topics
3. **📋 Strategic Planning**: Creates a comprehensive search plan with 6 targeted angles
4. **🔍 Parallel Execution**: Runs all searches concurrently for maximum speed
5. **📊 Synthesis**: Combines findings into a detailed, well-structured report
6. **📧 Delivery** (optional): Sends report via email if requested

### 🎨 User Interface

- **🌙 Dark Theme**: Professional dark mode with blue accents
- **📱 Responsive Design**: Works on desktop and mobile devices
- **⚡ Real-time Updates**: Live progress tracking during research
- **📋 Rich Formatting**: Markdown support for beautiful report display

## 🎮 Usage Examples

### 🔬 Research Topics
- **📈 Market Analysis**: "Latest trends in AI agent frameworks 2025"
- **🏛️ Political Research**: "Impact of recent policy changes on renewable energy"
- **🌍 Global Issues**: "Current state of climate change mitigation efforts"
- **💼 Business Intelligence**: "Competitive landscape in fintech startups"

### 🎯 Best Practices
- Be specific in your research questions
- Include timeframes when relevant (e.g., "2024 developments in...")
- Ask for multiple perspectives on controversial topics
- Specify the type of analysis you need (trends, comparisons, forecasts)

## 🔧 Configuration

### 🎨 UI Customization
The interface can be customized by modifying the CSS in `app.py`:
- Color schemes
- Layout dimensions
- Typography
- Component styling

### ⚙️ Agent Settings
Configure agent behavior in the respective files:
- Search depth and breadth
- Report length and detail
- Email formatting
- Parallel processing limits

## 📊 Performance

- **⚡ Speed**: Parallel search execution (6 searches in ~10-15 seconds)
- **📈 Accuracy**: Multiple perspective analysis for balanced insights
- **🎯 Relevance**: AI-powered search term optimization
- **📋 Completeness**: Comprehensive reports with citations and structure




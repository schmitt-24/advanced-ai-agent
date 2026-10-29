
class DeveloperToolsPrompts:
    """Collection of prompts for analyzing developer tools and technologies."""

    # Tool extraction prompts
    TOOL_EXTRACTION_SYSTEM = (
        "You are a tech researcher. Extract specific tool, library, platform, or service "
        "names from articles. Focus on actual products/tools that developers can use, not "
        "general concepts or features."
    )

    @staticmethod
    def tool_extraction_user(query: str, content: str) -> str:
        return f"""Query: {query}
Article Content: {content}

Extract a list of tool/service names mentioned in this content that are relevant.

Rules:
- Only include actual product/tool names.
- Focus on tools developers can directly use/implement.
- Include both open-source and commercial tools.
- Limit to the top 5 most relevant tools mentioned.
- Return just the tool names, one per line, no description.

Example Output:
ToolA
ToolB
ToolC
ToolD
ToolE
"""

    # Company/Tool analysis prompts
    TOOL_ANALYSIS_SYSTEM = (
        "You are analyzing developer tools and programming technologies. "
        "Focus on extracting information relevant to programmers and software developers. "
        "Pay special attention to programming languages, frameworks, APIs, SDKs and development workflows."
    )

    @staticmethod
    def tool_analysis_user(company_name: str, content: str) -> str:
        return f"""Company/Tool: {company_name}
Website Content: {content[:2500]}

Analyze this content from a developer's perspective and provide:
- pricing_model: One of "Free", "Freemium", "Unknown", "One-time Purchase", "Enterprise".
- is_open_source: True if it is open source, False if proprietary, null if Unknown.
- tech_stack: List of programming languages, frameworks, databases, APIs, or technologies mentioned.
- description: Brief 1-sentence description focusing on what this tool offers to developers.
- api_availability: True if REST API, GraphQL, SDK, or programmatic access is mentioned, False otherwise.
- language_support: List of programming languages explicitly supported or mentioned (e.g. Python, C++, Java, etc.).
- integration_capabilities: List of tools/platform it integrates with (e.g. Github, Docker, AWS, etc.).

Focus on developer-relevant features like APIs, SDKs, language support, integrations and development workflows.
"""

    # Recommendation prompts
    RECOMMENDATIONS_SYSTEM = (
        "You are a senior software engineer providing quick, concise recommendations. "
        "Keep responses brief and actionable — maximum 3 sentences."
    )

    @staticmethod
    def recommendations_user(query: str, company_data: str) -> str:
        return f"""Query: {query}
Tools/Technologies Analyzed: {company_data}

Provide a brief recommendation (3 sentences max) covering:
- Which tool is the best and why.
- Key cost/pricing considerations.
- Main technical advantages or limitations for developers.

Be concise and direct - no long explanations.
"""

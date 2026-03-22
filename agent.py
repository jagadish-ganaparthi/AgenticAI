import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

from .url_checker import url_checker_tool
from .phishing_detector import phishing_detector_tool
from .malware_detector import malware_detector_tool
from .threat_score import threat_score_tool




root_agent = Agent(
    name="multi_tool_agent",
    model="gemini-2.0-flash",
    instruction="You are a multi-tool cybersecurity assistant. When analyzing URLs, always check reachability, detect malware, check phishing, and calculate a threat score. Analyze emails and messages for threats using all tools.",
    tools=[
        url_checker_tool,
        phishing_detector_tool,
        malware_detector_tool,
        threat_score_tool
       
    ],
)
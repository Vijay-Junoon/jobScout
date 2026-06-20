from tools.scrape import scrape,StructuredOutput
from tools.sendMail import sendMail
from tools.databaseHandler import fetch,put

from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
from langchain.tools import tool
from dotenv import load_dotenv

import os

load_dotenv()

@tool
def scrape_tool(job_title:str,location:str):
  """Scrape the website for the specified job role and the location and returns the matched results"""
  response = scrape(job_title,location)
  return (response)

agent = create_agent(
  model = "groq:llama-3.3-70b-versatile",
  tools = [scrape_tool],
  system_prompt="YOU ARE A JOB FINDING SPECIALIST",
  response_format=StructuredOutput
)

response = agent.invoke({"messages": "Help me find jobs related to Developer in Mumbai"})
# print(response)
print(response['structured_response'])
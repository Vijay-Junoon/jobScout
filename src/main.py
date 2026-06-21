from tools.scrape import scrape,StructuredOutput
from tools.sendMail import sendMail
from tools.databaseHandler import fetch,put
from langgraph.graph import StateGraph,START,END
from langchain.agents import create_agent
from langchain.messages import HumanMessage,AIMessage,SystemMessage
from langchain.tools import tool
from dotenv import load_dotenv
from typing import TypedDict
import os


load_dotenv()

class JobState(TypedDict):
  user: tuple
  jobs: list
  email: str

def scrape_tool(state: JobState):
  user = state['user']
  """Scrape the website for the specified job role and the location and returns the matched results"""
  name = user[1]
  email = user[2]
  job_title = user[4]
  exp = user[5]
  loc = user[6]
  salary = user[7]
  jobs = scrape(name,email,job_title,exp,loc,salary)
  return {"jobs": jobs}

def send_mail(state: JobState):
  name = state['user'][1]
  email = state['user'][2]
  jobs = state['jobs']
  sendMail(name,email,jobs)
  return {}

def formatJobs(state:JobState):
  jobs = state['jobs']
  formattedJobs = ""
  cnt = 1
  for job in jobs:
    formattedJobs += f"""
    {cnt}) {job['job_title']}
            {job['employer_name']}
            {job['job_employment_type']}
            {job['job_apply_link']}"""
    cnt += 1
  return {'jobs': formattedJobs}

graph = StateGraph(JobState)
graph.add_node('scrape',scrape_tool)
graph.add_node('send_mail',send_mail)
graph.add_node('formatJobs',formatJobs)

graph.add_edge(START,'scrape')
graph.add_edge("scrape",'formatJobs')
graph.add_edge('formatJobs','send_mail')
graph.add_edge('formatJobs',END)

app = graph.compile()


def fetch_users():
  """This tool can be used to fetch all the user details from the data base"""
  user_details = fetch()    
  for user in user_details:
    app.invoke({"user": user})



fetch_users()
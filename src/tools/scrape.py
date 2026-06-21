from dotenv import load_dotenv
import os
import requests
from pydantic import BaseModel,Field

load_dotenv()
api_key= os.environ['X-API-Key']

class jobs(BaseModel):
  job_title: str = Field("Name of the job")
  job_apply_link: str = Field("Job application link")

class StructuredOutput(BaseModel):
  jobs:list[jobs]


def scrape(name: str,emaiL: str,jobRole:str,exp: int,location:str,salary:float):
  
  requirement = ""
  if exp == 0:
    requirement = "no_experience"
  elif exp < 3:
    requirement = "under_3_years_experience"
  elif exp >= 3:
    requirement = "more_than_3_years_experience"

  headers = {
  "X-API-Key": api_key
  }

  response = requests.request(
      'GET',
      'https://api.openwebninja.com/jsearch/search-v2',
      params={
        'query':f'{jobRole} opportunities in {location}',
        'country' : "in",
        'date_posted': '3days',
        'job_requirements': requirement,
        'fields':"employer_name,job_publisher,job_title,job_employment_type,job_city,job_apply_link"
      },
      headers=headers
  )
  return response.json()['data']['jobs'][:4]


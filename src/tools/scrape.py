from dotenv import load_dotenv
import os
import requests
from pydantic import BaseModel,Field

load_dotenv()

# {"job_id": "XzfsIYq11GiPnTbuAAAAAA==", "job_title": "Junior Front End Developer", "job_apply_link": "https://www.simplyhired.co.in/job/u_HWaNDqbjBIvTt9X8NK0gWP4iNEAZOEc14utPH_rvrPyHA9pMoeSQ"}

class jobs(BaseModel):
  job_title: str = Field("Name of the job")
  job_apply_link: str = Field("Job application link")

class StructuredOutput(BaseModel):
  jobs:list[jobs]


def scrape(jobRole:str,location:str):
  headers = {
  "X-API-Key": "ak_k5ie7doodrxmofkfjgvsvwuftb6gq5altxs2pwee9i3m0dz"
  }

  response = requests.request(
      'GET',
      'https://api.openwebninja.com/jsearch/search-v2',
      params={
        'query':f'{jobRole} opportunities in {location}',
        'country' : "in",
        'date_posted': 'today',
        'fields':( "employer_name","job_publisher","job_title","job_country",'job_apply_link')
      },
      headers=headers
  )

  return response.json()['data']['jobs'][:4]


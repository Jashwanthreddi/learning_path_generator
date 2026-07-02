import os
from langchain_groq import ChatGroq
from prompt import learning_path_prompt
from schema import Learningpath


def get_llm(model="llama-3.3-70b-versatile",temperature=0.3):
   api_key=os.getenv("GROQ_API_KEY")
   if not api_key:
      raise RuntimeError(
         "GROQ_API_KEY not set. create a .env file"
      )
   return ChatGroq(model=model,temperature=temperature,api_key=api_key)

def build_chain(llm:ChatGroq | None=None):
   llm=llm or get_llm()
   structured_llm=llm.with_structured_output(Learningpath)
   return learning_path_prompt | structured_llm

def generate_learning_path(skill,llm:ChatGroq | None=None) -> Learningpath:
   if not skill or not skill.strip():
      raise ValueError('skill must be a non empty string')
   chain = build_chain(llm)
   result=chain.invoke({"skill":skill.strip()})
   return result

if __name__=="__main__":
   from dotenv import load_dotenv

   load_dotenv()
   path=generate_learning_path("Data Science")
   print(path.model_dump_json(indent=2))

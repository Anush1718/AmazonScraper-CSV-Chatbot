#from tempfile import NamedTemporaryFile
import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
import pandas as pd


def main():

    

    load_dotenv()


    st.set_page_config(page_title="Ask me")
    st.header("Ask me")

    user_csv = st.file_uploader("upload your CSV file", type="csv")



    #if user_csv is not None:
      #  with NamedTemporaryFile(mode='w+b', suffix=".csv") as f:
        #    f.write(user_csv.getvalue())
        #    f.flush()
        #    llm = OpenAI(temperature=0, OPENAI_API_KEY="YOUR API KEY")
        #    user_input = st.text_input("Question here:")
        #    agent = create_csv_agent(llm, f.name, verbose=True)
        #    if user_input:
        #        response = agent.run(user_input)
          #      st.write(response)



   

    if user_csv is not None:
        
        
        user_question = st.text_input("Ask me about Iphone:")

        llm = OpenAI(temperature=0.9)

        agent = create_csv_agent(llm, user_csv, verbose=True)

        if user_question is not None and user_question !="":
            
               with st.spinner(text="In progress..."):
                st.write(agent.run(user_question))
           
           #response = agent.run(user_question)


        #st.write(response)





if __name__ == "__main__":
    main()

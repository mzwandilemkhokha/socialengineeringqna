import os
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import UnstructuredFileLoader
#from langchain_community.embeddings import OpenAIEmbeddings
#from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings
#from langchain_openai import OpenAIEmbeddings
#from langchain_openai import OpenAIEmbeddings
from langchain_openai import OpenAI
#from langchain.document_loaders import UnstructuredPDFLoader
#from langchain import VectorstoreIndexCreator
import streamlit as st
from langchain.indexes import VectorstoreIndexCreator
import openai
import os
from langchain.llms import OpenAI
from langchain_openai import OpenAIEmbeddings
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.agents.agent_toolkits import (
    create_vectorstore_agent,
    VectorStoreToolkit,
    VectorStoreInfo
)

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# connect your Google Drive


root_dir = "./pdfs"

pdf_folder_path = './pdfs/'
os.listdir(pdf_folder_path)

with st.spinner('Working, Please wait...'):
    #PyPDFLoader('./bitcoin.pdf')
    from langchain.document_loaders import PyPDFLoader
    pdf_folder_path = './pdfs/'
    #loaders=PyPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)
    loaders= [PyPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path) if fn.lower().endswith(".pdf")]
    index = VectorstoreIndexCreator().from_loaders(loaders)
#st.text(index.query('which regions grow honey?'))
# Streamlit UI setup
st.toast("Thank You for waiting")

#side bar code
st.sidebar.header("About", divider="gray")
st.sidebar.markdown("I was tasked to research on how information systems can be vunerable to attacks using the human element through social engineering"+ 
                    ".This has inspired me to contribute to society by making a tool that users will use to find out more about social engineering and how they can protect themselves from it."+
                    "empowers farmers and interested parties to find quick answers to queries or topics of interest.  ")
st.sidebar.header("", divider="green")
st.sidebar.markdown("The document used on this platform was compiled by Mzwandile, as per qualification requirement. This document is for educational purposes only and should not be used as a source of income.")
st.sidebar.header("", divider="green")
st.title('Social Engineering Awareness Toolkit')
st.divider()


#prompt = st.text_input('Ask Me Anything About Farming')


prompt=st.chat_input('Ask Me Anything Social Engineering related')
with st.chat_message("user"):
        if(prompt==None):
            st.write("Ask Me anything Social Engineering related")
        else:
            st.write(prompt)
if prompt:
    with st.spinner('Finding an answer for you, please wait...'):
        response = index.query(prompt)
    with st.chat_message("assistant"):
            st.write(response)
    #st.write(response)

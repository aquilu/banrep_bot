# utils.py

import streamlit as st
import openai
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate

openai.api_key = st.secrets["OPENAI_API_KEY"]

@st.cache_resource
def load_chain():
    # Load OpenAI embedding model
    embeddings = OpenAIEmbeddings()
    
    # Load OpenAI chat model
    llm = ChatOpenAI(temperature=0)
    
    # Load our local FAISS index as a retriever
    vector_store = FAISS.load_local("faiss_index", embeddings)
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    
    # Create memory 'chat_history' 
    memory = ConversationBufferWindowMemory(k=3, memory_key="chat_history")
    
    # Create system prompt
    template = """
    You are an AI assistant for answering questions about El Banco de la República en Colombia: antecedentes, evolución y estructura.
    You are given the following extracted parts of a long document and a question. Provide a conversational answer.
    If you don't know the answer, just say 'Sorry, I don't know ... 😔.
    Don't try to make up an answer.
    If the question is not about El Banco de la República: antecedentes, evolución y estructura, politely inform them that you are tuned to only answer questions about El Banco de la República: antecedentes, evolución y estructura.
    
    {context}
    Question: {question}
    Helpful Answer:"""
    
    # Create the Conversational Chain
    chain = ConversationalRetrievalChain.from_llm(llm=llm, 
                                                  retriever=retriever, 
                                                  memory=memory, 
                                                  get_chat_history=lambda h : h,
                                                  verbose=True)
    
    # Add system prompt to chain
    # Can only add it at the end for ConversationalRetrievalChain
    QA_CHAIN_PROMPT = PromptTemplate(input_variables=["context", "question"],template=template)
    chain.combine_docs_chain.llm_chain.prompt.messages[0] = SystemMessagePromptTemplate(prompt=QA_CHAIN_PROMPT)
    
    return chain

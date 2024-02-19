# -*- coding: utf-8 -*-
import os
import sys
from dotenv import load_dotenv

from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

load_dotenv('code.env')

#Read the PDF file
pdf_loader = PyPDFLoader(r'C:\Users\Advaith R\Desktop\ChatBot\Documents\advaith_resume.pdf')
documents = pdf_loader.load()
#print(documents)

# Breakdown the document into multiple chunks/ paragrapghs
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
documents = text_splitter.split_documents(documents)
#print(documents)


# Convert the document chunks to embedding and save them to the vector store
vectordb1 = Chroma.from_documents(documents, embedding=OpenAIEmbeddings(), persist_directory="./data")
vectordb1.persist()
print(vectordb1)



# create a Q&A chain
pdf_qa = ConversationalRetrievalChain.from_llm(
    ChatOpenAI(temperature=0.7, model_name='gpt-3.5-turbo'),
    retriever=vectordb1.as_retriever(search_kwargs={'k': 6}),
    return_source_documents=True,
    verbose=False
)


yellow = "\033[0;33m"
green = "\033[0;32m"
white = "\033[0;39m"



chat_history = []
print(f"{yellow}---------------------------------------------------------------------------------")
print('Welcome to the DocBot. You are now ready to start interacting with your documents')
print('---------------------------------------------------------------------------------')
while True:
    query = input(f"{green}Prompt: ")
    if query == "exit" or query == "quit" or query == "q" or query == "f":
        print('Exiting')
        sys.exit()
        
    if query == '':
        continue
    result = pdf_qa.invoke(
        {"question": query, "chat_history": chat_history})
    print(f"{white}Answer: " + result["answer"])
    chat_history.append((query, result["answer"]))
    
    
    #Get top 3 chunks or paragraphs
    top3_chunks = vectordb1.similarity_search_with_score(query)
    print(f"\nThe top 3 chunks/paragraphs are : \n{top3_chunks[:3]}")


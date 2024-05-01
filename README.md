# CONTEXTUAL CHATBOT

Create a simple contextual chatbot to read a long PDF/Word Docuement. The chatbot will use this document as a context to answer the questions. If the answer is not found in the document - it says I dont know the answer.

Advanced - 
1. Breaking down the document into multiple chunks/paragraphs.
2. Store them in a vector database.
3. Find out the top 3 chunks that will likely have the answer to the question.

Chatbot folder contains 2 folders:

1.Code - Contains 1 folder and 2 files:

    1. code.env - contains OpenAI API Key
    
    2. contextual chatbot.py - Main code
    
    3. data - storing the chunks of the document as a vector database

2.Documents - Contains pdf document

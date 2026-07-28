# Semantic-RAG-Agent-for-Retail

## Result 

Total Pages loaded : 25

Adding metadata..
Metadata Added Successfully!

Preview : 
==================================================
Metadata Information - 

Page : 1

Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf

Heading : RETAIL DISPLAY MANUAL

Content Type : text

length : 325
--------------------------------------------------
RETAIL DISPLAY MANUAL

Standard Operating Procedures & Merchandising Guidelines

FreshMart Global Retail Corporation

Document ID:

FM-SOP-2025-001

Version:

4.2

Effective Date:

January 15, 2025

Review Date:

July 15, 2025

Classification:

INTERNAL - Store Operations

Department:

Visual Merchandising & Store Standards




Metadata Information - 

Page : 2

Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf

Heading : Unknown

Content Type : short_text

length : 98
--------------------------------------------------
CONFIDENTIAL — For authorized store personnel only.

FreshMart Retail Display Manual v4.2 — Page 2





Total Chunks after Semantic Chunker : 52

Vector Database Created!!

Page No : 11

Retrieved Document : 5. Beverage Aisle Standards

5.1 Cold Vault Management

The cold vault (refrigerated beverage section) must maintain a temperature range of 34-38°F (1-3°C). All products must be front-faced with labels visible. The cold vault is restocked using the FIFO (First In, First Out) rotation method. Maximum door opening time for restocking is 10 minutes per section to maintain temperature compliance. Condensation on doors must be addressed immediately — report to maintenance if anti-fog heaters malfunction. 5.2 Carbonated Soft Drink (CSD) Placement

CSDs follow a brand-block vertical merchandising strategy. Coca-Cola products occupy the first 3 door sections (left to right when facing the vault). PepsiCo products occupy sections 4-6. Private label and regional brands fill sections 7-8. Energy drinks are positioned in sections 9-10 at eye level. Water and enhanced water products are placed in the final 2-3 sections. All 2-liter and multi-pack items are on the bottom shelf. 5.3 Ambient Beverage Shelving

Ambient (room temperature) beverages are merchandised on standard gondola shelving adjacent to the cold vault. The flow moves from single-serve (left) to multi-pack (right).
--------------------------------------------------
C:\Users\ssandeep011\Downloads\Semantic RAG Agent for Retail\src\llm_agent.py:35: LangChainDeprecationWarning: The class `ConversationBufferWindowMemory` was deprecated in LangChain 0.3.1 and will be removed in 2.0.0. Use `langchain.agents.create_agent` instead. For agents that need to remember prior interactions, use `create_agent` with checkpointing or the `Store` API. See https://docs.langchain.com/oss/python/langchain/short-term-memory and https://docs.langchain.com/oss/python/langchain/long-term-memory
  self.memory = ConversationBufferWindowMemory(

Question 1: What are the requirements for seasonal display transitions?

Agent Answer:
Seasonal transitions follow a strict calendar. Holiday displays are set 4-6 weeks before the event and torn down within 24 hours after. Post-holiday clearance occupies dedicated Zone F space. The transition crew (minimum 3 associates per shift) executes the changeover during overnight hours (10 PM - 6 AM) to minimize customer disruption.
--------------------------------------------------

Metadata Information - 

Page : 17
Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf
Heading : 9. Seasonal & Holiday Displays
Content Type : text
Length : 1153
--------------------------------------------------

Question 2: List out few Safety & Compliance Protocols?

Agent Answer:
Here are a few Safety & Compliance Protocols:
1. Display Stability Requirements
2. Fire Safety Compliance
3. Hazardous Materials Handling
4. Ergonomic Stacking Limits
--------------------------------------------------

Metadata Information - 

Page : 15
Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf
Heading : 8. Safety & Compliance Protocols
Content Type : text
Length : 2015
--------------------------------------------------

Question 3: Can you explain the Shelf Planogram Guidelines?

Agent Answer:
Here are the Shelf Planogram Guidelines:
1. Planogram Compliance Overview
2. Shelf Stocking Hierarchy
3. Facing Requirements by Category
4. Out-of-Stock Protocol
5. Price Tag Placement
--------------------------------------------------

Metadata Information - 

Page : 8
Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf
Heading : 3. Shelf Planogram Guidelines
Content Type : text
Length : 2354
--------------------------------------------------

Question 4: What is the full form of BOGO?

Agent Answer:
Here is the full form of BOGO:
Buy One, Get One
--------------------------------------------------

Metadata Information - 

Page : 23
Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf
Heading : Term
Content Type : text
Length : 257
--------------------------------------------------

Question 5: What is the required temperature range for the cold vault?

Agent Answer:
The required temperature range for the cold vault is 34-38°F (1-3°C).
--------------------------------------------------

Metadata Information - 

Page : 11
Source Path : C:/Users/ssandeep011/Downloads/Semantic RAG Agent for Retail/Data/Retail_Display_Manual.pdf
Heading : 5. Beverage Aisle Standards
Content Type : short_text
Length : 1183


## Evaluation : 

data={
    'question': ["What is the required temperature range for the cold vault?"],
    'answer': ["The required temperature range for the cold vault is 34-38°F (1-3°C)."],
    'contexts': [['The cold vault (refrigerated beverage section) must maintain a temperature range of 34-38°F (1-3°C). All products must be front-faced with labels visible. The cold vault is restocked using the FIFO (First In, First Out) rotation method. Maximum door opening time for restocking is 10 minutes per section to maintain temperature compliance. Condensation on doors must be addressed immediately — report to maintenance if anti-fog heaters malfunction']],
    'reference': ['''The  cold  vault  (refrigerated  beverage  section)  must  maintain  a  temperature  range  of  34-38°F  (1-3°C).  All
products must be front-faced with labels visible. The cold vault is restocked using the FIFO (First In, First Out)
rotation method. Maximum door opening time for restocking is 10 minutes per section to maintain temperature
compliance.  Condensation  on  doors  must  be  addressed  immediately  —  report  to  maintenance  if  anti-fog
heaters malfunction''']
}

Evaluating: 100%|██████████████████████████████████████████████████████████████████████████████| 4/4 [00:06<00:00,  1.55s/it]
{'faithfulness': 1.0000, 'answer_relevancy': 1.0000, 'context_recall': 1.0000, 'context_precision': 1.0000}

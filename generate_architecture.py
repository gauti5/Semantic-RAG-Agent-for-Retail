import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

fig, ax = plt.subplots(1, 1, figsize=(20, 14))
ax.set_xlim(0, 20)
ax.set_ylim(0, 14)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

# Color scheme
colors = {
    'header': '#1B2838',
    'data_source': '#E8F5E9',
    'data_source_border': '#4CAF50',
    'ingestion': '#E3F2FD',
    'ingestion_border': '#2196F3',
    'storage': '#FFF3E0',
    'storage_border': '#FF9800',
    'retrieval': '#F3E5F5',
    'retrieval_border': '#9C27B0',
    'agent': '#FFEBEE',
    'agent_border': '#F44336',
    'evaluation': '#E0F7FA',
    'evaluation_border': '#00BCD4',
    'aws': '#FFF8E1',
    'aws_border': '#FFC107',
    'arrow': '#455A64',
}

def draw_box(ax, x, y, w, h, label, sublabel='', facecolor='white', edgecolor='black', fontsize=9, bold=True):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1",
                         facecolor=facecolor, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(box)
    weight = 'bold' if bold else 'normal'
    if sublabel:
        ax.text(x + w/2, y + h/2 + 0.15, label, ha='center', va='center',
                fontsize=fontsize, fontweight=weight, color='#1B2838')
        ax.text(x + w/2, y + h/2 - 0.2, sublabel, ha='center', va='center',
                fontsize=7, fontweight='normal', color='#546E7A', style='italic')
    else:
        ax.text(x + w/2, y + h/2, label, ha='center', va='center',
                fontsize=fontsize, fontweight=weight, color='#1B2838')

def draw_section(ax, x, y, w, h, title, facecolor, edgecolor):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.15",
                         facecolor=facecolor, edgecolor=edgecolor, linewidth=2, alpha=0.7)
    ax.add_patch(box)
    ax.text(x + 0.3, y + h - 0.35, title, ha='left', va='center',
            fontsize=10, fontweight='bold', color=edgecolor)

def draw_arrow(ax, start, end, color='#455A64', style='->', lw=1.5):
    arrow = FancyArrowPatch(start, end, arrowstyle=style,
                            color=color, lw=lw,
                            connectionstyle="arc3,rad=0.0",
                            mutation_scale=15)
    ax.add_patch(arrow)

# Title
ax.text(10, 13.5, 'Semantic RAG Agent for Retail — Complete Architecture',
        ha='center', va='center', fontsize=16, fontweight='bold', color=colors['header'])
ax.text(10, 13.1, 'LangChain | AWS Bedrock | ChromaDB | RAGAS Evaluation',
        ha='center', va='center', fontsize=10, color='#546E7A')

# ===== Section 1: Data Source =====
draw_section(ax, 0.3, 10.5, 3.4, 2.2, '[1] DATA SOURCE', colors['data_source'], colors['data_source_border'])
draw_box(ax, 0.6, 10.8, 2.8, 0.7, 'Retail_Display_Manual.pdf', 'PDF Document',
         facecolor='white', edgecolor=colors['data_source_border'])
draw_box(ax, 0.6, 11.7, 2.8, 0.7, 'PDFLoader', 'loader.py — UnstructuredPDFLoader',
         facecolor='white', edgecolor=colors['data_source_border'])

# ===== Section 2: Ingestion Pipeline =====
draw_section(ax, 4.0, 10.5, 5.5, 2.2, '[2] INGESTION PIPELINE', colors['ingestion'], colors['ingestion_border'])
draw_box(ax, 4.3, 11.7, 2.3, 0.7, 'Semantic Chunker', 'chunking.py',
         facecolor='white', edgecolor=colors['ingestion_border'])
draw_box(ax, 6.9, 11.7, 2.3, 0.7, 'Metadata Enricher', 'heading / type / length',
         facecolor='white', edgecolor=colors['ingestion_border'])
draw_box(ax, 4.3, 10.8, 2.3, 0.7, 'Embeddings Service', 'embeddings.py — Bedrock',
         facecolor='white', edgecolor=colors['ingestion_border'])
draw_box(ax, 6.9, 10.8, 2.3, 0.7, 'VectorStore Service', 'vectorstore.py — Chroma',
         facecolor='white', edgecolor=colors['ingestion_border'])

# ===== Section 3: Vector Storage =====
draw_section(ax, 10.0, 10.5, 3.5, 2.2, '[3] VECTOR STORAGE', colors['storage'], colors['storage_border'])
draw_box(ax, 10.3, 11.0, 2.9, 1.3, 'ChromaDB', 'db/ — Persistent Vector DB\nMMR Search (k=1)',
         facecolor='white', edgecolor=colors['storage_border'])

# ===== Section 4: Retrieval =====
draw_section(ax, 0.3, 7.5, 4.5, 2.5, '[4] RETRIEVAL LAYER', colors['retrieval'], colors['retrieval_border'])
draw_box(ax, 0.6, 8.7, 3.9, 0.7, 'Retriever', 'retrieval.py — MMR Search',
         facecolor='white', edgecolor=colors['retrieval_border'])
draw_box(ax, 0.6, 7.8, 3.9, 0.7, 'Context Builder', 'Join retrieved doc contents',
         facecolor='white', edgecolor=colors['retrieval_border'])

# ===== Section 5: Agent Layer =====
draw_section(ax, 5.2, 6.0, 8.8, 4.2, '[5] AGENT LAYER', colors['agent'], colors['agent_border'])

# RAG Chain (simple)
draw_box(ax, 5.5, 8.8, 3.8, 0.7, 'RAG Chain (Simple)', 'llm.py — RetailAssistant',
         facecolor='white', edgecolor=colors['agent_border'])
draw_box(ax, 5.5, 7.9, 3.8, 0.7, 'Prompt Template', 'prompt.py — ChatPromptTemplate',
         facecolor='white', edgecolor=colors['agent_border'])
draw_box(ax, 5.5, 7.0, 3.8, 0.7, 'Conversation Memory', 'memory.py — BufferMemory',
         facecolor='white', edgecolor=colors['agent_border'])

# Tool-Calling Agent
draw_box(ax, 9.7, 8.8, 4.0, 0.7, 'Tool-Calling Agent', 'llm_agent.py — RetailAgent',
         facecolor='white', edgecolor=colors['agent_border'])
draw_box(ax, 9.7, 7.9, 4.0, 0.7, 'AgentExecutor', 'create_tool_calling_agent',
         facecolor='white', edgecolor=colors['agent_border'])
draw_box(ax, 9.7, 7.0, 4.0, 0.7, 'RetailRetriever Tool', 'Custom @tool — search_manual()',
         facecolor='white', edgecolor=colors['agent_border'])
draw_box(ax, 9.7, 6.2, 4.0, 0.6, 'Window Memory (k=5)', 'ConversationBufferWindowMemory',
         facecolor='white', edgecolor=colors['agent_border'])

# ===== Section 6: AWS Bedrock =====
draw_section(ax, 14.0, 7.5, 5.5, 2.5, '[6] AWS BEDROCK', colors['aws'], colors['aws_border'])
draw_box(ax, 14.3, 8.5, 2.4, 0.7, 'Chat LLM', 'ChatBedrock (Claude)',
         facecolor='white', edgecolor=colors['aws_border'])
draw_box(ax, 17.0, 8.5, 2.2, 0.7, 'Embeddings', 'BedrockEmbeddings',
         facecolor='white', edgecolor=colors['aws_border'])
draw_box(ax, 14.3, 7.7, 4.9, 0.6, 'boto3 Session — us-east-1',
         facecolor='white', edgecolor=colors['aws_border'])

# ===== Section 7: Evaluation =====
draw_section(ax, 0.3, 4.5, 6.5, 2.5, '[7] EVALUATION (RAGAS)', colors['evaluation'], colors['evaluation_border'])
draw_box(ax, 0.6, 5.7, 2.8, 0.7, 'Faithfulness', '',
         facecolor='white', edgecolor=colors['evaluation_border'])
draw_box(ax, 3.7, 5.7, 2.8, 0.7, 'Answer Relevancy', '',
         facecolor='white', edgecolor=colors['evaluation_border'])
draw_box(ax, 0.6, 4.8, 2.8, 0.7, 'Context Precision', '',
         facecolor='white', edgecolor=colors['evaluation_border'])
draw_box(ax, 3.7, 4.8, 2.8, 0.7, 'Context Recall', '',
         facecolor='white', edgecolor=colors['evaluation_border'])

# ===== Section 8: Pipeline Orchestrators =====
draw_section(ax, 7.2, 4.5, 6.5, 1.3, '[8] PIPELINE ORCHESTRATORS', '#ECEFF1', '#607D8B')
draw_box(ax, 7.5, 4.7, 2.8, 0.7, 'rag_pipeline.py', 'Simple RAG Flow',
         facecolor='white', edgecolor='#607D8B')
draw_box(ax, 10.7, 4.7, 2.8, 0.7, 'agent_pipeline.py', 'Agent RAG Flow',
         facecolor='white', edgecolor='#607D8B')

# ===== Section 9: User Interface =====
draw_section(ax, 14.0, 4.5, 5.5, 2.5, '[9] USER INTERACTION', '#FAFAFA', '#37474F')
draw_box(ax, 14.3, 5.7, 4.9, 0.7, 'Multi-Turn Q&A Loop', 'Questions → Answers + Source Pages',
         facecolor='white', edgecolor='#37474F')
draw_box(ax, 14.3, 4.8, 4.9, 0.7, 'Metadata Display', 'Page / Source / Heading / Type',
         facecolor='white', edgecolor='#37474F')

# ===== ARROWS =====
# Data source → Ingestion
draw_arrow(ax, (3.7, 12.05), (4.3, 12.05), color=colors['data_source_border'])
# Chunker → Metadata
draw_arrow(ax, (6.6, 12.05), (6.9, 12.05), color=colors['ingestion_border'])
# Embeddings → VectorStore
draw_arrow(ax, (6.6, 11.15), (6.9, 11.15), color=colors['ingestion_border'])
# Ingestion → Vector Storage
draw_arrow(ax, (9.2, 11.15), (10.3, 11.5), color=colors['ingestion_border'])
# Vector Storage → Retrieval
draw_arrow(ax, (10.3, 11.0), (4.5, 9.4), color=colors['storage_border'], style='->')
# Retrieval → Agent
draw_arrow(ax, (4.8, 8.15), (5.5, 8.15), color=colors['retrieval_border'])
# Agent → AWS
draw_arrow(ax, (13.7, 9.15), (14.3, 8.85), color=colors['agent_border'])
# AWS answers back
draw_arrow(ax, (14.3, 8.5), (13.7, 8.2), color=colors['aws_border'])

# Pipeline → User
draw_arrow(ax, (13.5, 5.05), (14.3, 5.05), color='#607D8B')

# Legend at bottom
legend_y = 3.5
ax.text(0.5, legend_y, 'Tech Stack:', fontsize=9, fontweight='bold', color='#1B2838')
techs = [
    ('Python 3.12', '#4CAF50'), ('LangChain', '#2196F3'), ('AWS Bedrock', '#FFC107'),
    ('ChromaDB', '#FF9800'), ('RAGAS', '#00BCD4'), ('boto3', '#9C27B0')
]
for i, (name, color) in enumerate(techs):
    ax.add_patch(FancyBboxPatch((2.2 + i*2.8, legend_y - 0.2), 2.4, 0.5,
                                boxstyle="round,pad=0.05", facecolor=color, alpha=0.15, edgecolor=color))
    ax.text(2.2 + i*2.8 + 1.2, legend_y + 0.05, name, ha='center', va='center',
            fontsize=8, fontweight='bold', color=color)

plt.tight_layout(pad=1.0)
plt.savefig('Project_Architecture.png', dpi=200, bbox_inches='tight',
            facecolor='#F8F9FA', edgecolor='none')
plt.close()
print("Architecture diagram saved as Project_Architecture.png")

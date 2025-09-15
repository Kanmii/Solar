class QAAgent:
    """
    Handles general user questions about solar energy and the project.
    Uses a RAG + Web Search architecture.
    """
    def __init__(self):
        # TODO: Initialize the RAG pipeline
        # - Vector store with knowledge_base documents
        # - Retriever
        # - Fine-tuned LLM for generation
        # TODO: Initialize the web search tool (e.g., Tavily client)
        pass

    def answer_question(self, question: str):
        """
        Answers a user's question.
        """
        # TODO: Implement the RAG + Web Search workflow:
        # 1. Search internal knowledge base first.
        # 2. If no good answer, ask user for permission to search the web.
        # 3. If permission granted, use web search tool.
        # 4. Generate a final answer based on the context found.
        print(f"QAAgent answering question: {question}")
        return "This is a detailed answer from the Q&A Agent."

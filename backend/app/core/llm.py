from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

class LLMManager:
    def __init__(self, model_path: str, model_type: str):
        self.model_path = model_path
        self.model_type = model_type
        self.llm = None
        self.qa_chain = None

    def initialize_llm(self):
        self.llm = CTransformers(
            model=self.model_path,
            model_type=self.model_type,
            config={
                'max_new_tokens': 512,
                'temperature': 0.8
            }
        )
        return self.llm

    def create_qa_chain(self, retriever, prompt_template):
        if not self.llm:
            self.initialize_llm()

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["context", "question"]
        )

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": prompt}
        )
        return self.qa_chain
# src/services/huggingface_service.py
from transformers import pipeline, AutoTokenizer

# tokenizer = AutoTokenizer.from_pretrained("gpt2")
# tokenizer.pad_token = tokenizer.eos_token

class HuggingFaceService:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.qa_pipeline = pipeline("question-answering", model=self.model_name, truncation=True) #tokenizer=tokenizer)
        
    def ask(self, question: str, context: str = "") -> dict:
       
        if not context:
            return {
                "text": "Não há contexto disponível para responder.",
                "similarity_score": 0,
                "relevance_score": 0,
            }

        result = self.qa_pipeline({"question": question, "context": context})
        # result normalmente é algo como: {"score": 0.98, "start": 34, "end": 39, "answer": "Paris"}

        return {
            "text": result["answer"],
            "similarity_score": result["score"],  
            "relevance_score": result["score"], 
        }

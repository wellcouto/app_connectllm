import sys
from factories.chatgpt_factory import ChatGPTFactory
from factories.huggingface_factory import HuggingFaceFactory
from commands.ask_command import AskCommand
from strategies.similarity_strategy import SimilarityStrategy
# from strategies.reference_check_strategy import ReferenceCheckStrategy
# from strategies.embedding_similarity_strategy import EmbeddingSimilarityStrategy
# from strategies.wikipedia_check_strategy import WikipediaCheckStrategy
from services.response_evaluator import ResponseEvaluator
from observers.cli_observer import CLIObserver


"""
Ponto de entrada principal da aplicação (CLI).
Utiliza argparse para lidar com parâmetros.
"""

def main():
    
    DEMO_CONTEXT = """
    A França é um país localizado na Europa Ocidental.
    Sua capital é Paris, conhecida por monumentos históricos como
    a Torre Eiffel, o Museu do Louvre e a catedral de Notre-Dame.
    """

    if len(sys.argv) < 3:
        print("Uso: python main.py <modelo> <pergunta> [<contexto>]")
        print("Exemplo: python main.py hf 'Qual é a capital da França?'")
        print("Exemplo:Ou python main.py hf 'Qual é a capital da França?' 'A França é um país localizado na Europa. ...'")
        sys.exit(1)

    
    # if len(sys.argv) < 4:
    #     print("Uso: python main.py <modelo> <pergunta> <contexto>")
    #     print("Exemplo: python main.py hf 'Qual é a capital da França?' 'A França é um país localizado na Europa. ...'")
    #     sys.exit(1)

    model_choice = sys.argv[1]
    question = sys.argv[2]
    
    if len(sys.argv) >= 4:
        context = sys.argv[3]
    else:
        context = DEMO_CONTEXT

    chatgpt_api_key = "sua_chave_api"
    huggingface_model = "deepset/roberta-base-squad2"  

    # Decide qual fábrica criar
    if model_choice.lower() == "chatgpt":
        factory = ChatGPTFactory(api_key=chatgpt_api_key)
    elif model_choice.lower() == "hf":
        factory = HuggingFaceFactory(model_name=huggingface_model)
    else:
        print("Modelo não reconhecido.")
        sys.exit(1)
    
    ask_command = AskCommand(factory, question, context)
    single_response = ask_command.execute()
    
    print("\nResposta do modelo escolhido:")
    print(single_response["text"])

    #responses
    responses = []
    #gpt
    chatgpt_factory = ChatGPTFactory(api_key=chatgpt_api_key)
    chatgpt_ask_command = AskCommand(chatgpt_factory, question, context)
    # responses.append(chatgpt_ask_command.execute())
    # HF
    huggingface_factory = HuggingFaceFactory(model_name=huggingface_model)
    hf_ask_command = AskCommand(huggingface_factory, question, context)
    responses.append(hf_ask_command.execute())
    
    #strategy
    evaluator = ResponseEvaluator(strategy=SimilarityStrategy())
    cli_observer = CLIObserver()
    evaluator.attach(cli_observer)

    # Faz a escolha e notifica
    best = evaluator.evaluate_and_notify(responses)
    print(f"\nMelhor resposta (pela Strategy):")
    print(best)

    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {str(e)}")
        sys.exit(1)

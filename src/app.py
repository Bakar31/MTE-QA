import gradio as gr
from haystack.nodes import FARMReader

mte_reader = FARMReader(model_name_or_path='MTE_QA_model/',
                        top_k = 2,
                        max_seq_len = 512,
                        context_window_size = 100,
                        #confidence_threshold = 0.5,
                        use_gpu= True)

with open('../data/context.txt', 'r') as file:
    context = file.read().replace('\n', '')

def get_answer_gr(question):
  prediction = mte_reader.predict_on_texts(question,[context])
  first_anwer = prediction['answers'][0:2][0].answer
  first_score = prediction['answers'][0:2][0].score
  second_anwer = prediction['answers'][0:2][1].answer
  second_score = prediction['answers'][0:2][1].score
  return ((first_anwer, first_score), (second_anwer, second_score))

demo = gr.Interface(
    fn=get_answer_gr,
    inputs=gr.Textbox(lines=3, placeholder="Question Here..."),
    outputs= ["text", "text"],

    title="Mechatronics QA System",
    description="Ask your Mechatronics related question. My model will give you answer. Remember it has limitations. Enjoy! - Abu Bakar Siddik, A proud Mechatronics Engineering Student.",
    article = "Check out the github repo: https://github.com/Bakar31/MTE-QA"
)
demo.launch()
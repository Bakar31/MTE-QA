[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FBakar31%2FMTE-QA&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

# MTE-QA 
This system will answer your Mechatronics related question.
The front end will return 2 answers as well as the confidence of the anwsers.
URL: https://huggingface.co/spaces/Bakar31/MTE_QA

<b>My Approch:</b> 
<p>
I scraped raw data from  Google and created a dataset. The dataset is not very reach, but as it is a specific problem, 
it works relatively well. Haystack has been used to train the modeling, 
and for the frontend I utilized gradio. The system returns two possible answers with its confidence score.

Traning Setting:
<li>Model: roberta-base-squad2</li>
<li>max_seq_len = 512</li>
<li>context_window_size = 150</li>
<li>doc_stride = 128</li>
<li>batch_size = 32</li>
<br>

Multiple models' results were compared. The most effective solution comes from Deepset roberta-base-squad2.</p>

Sample output: <br>
<img src="sample-1.jpg" width="60%" height="1000"> 
<img src="sample-2.jpg" width="60%" height="1000">


Demo questions:
- what is mechatronics engineering?
- what is the origin of mechatronics?'
- why persue mechatronics engineering? 
- What is a good example of a mechatronics system?
- What does a mechatronics engineer do?
- Salary of a mechatronics engineer?
- Is a mechatronics engineer worth hiring? 
- What does a mechatronics specialist do?
- Is there the connection between Iot and mechatronics?
- Job sector for mechatronics engineers?  
- Career opputunities for a mechatronics engineer?
- How are mechatronics engineers changing the world? 
- Job responsibilities of a mechatronics engineer?
- job sectors for mechatronics engineers? 
- what are some examples of mechatronics products?
- What is the salary of a robotic expert?
- What can I do after completing a degree in mechatronics?
- why should I hire a mechatronics engineer?
- what is the best university in bangladesh for mechatronics degree?
- Mechatronics engineering in Bangladesh?
- what are the roles of mechatronics in healthcare?
- What does a mechatronics engineer do in the medical field?
- What are the roles of mechatronics engineers in an industry? 
- Is a mechatronics engineer suited for the defense industry?
- Is a mechatronics engineer suited for the telecom industry?
- What are the applications of mechatronics in automobiles

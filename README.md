# LlamaPost

## 📌 Overview
`LlamaPost` is a filtering and retrieval system that selects relevant posts based on user-specified criteria such as **length, language, and tags**. It is designed to help Large Language Models (LLMs) generate more contextually appropriate responses by retrieving a subset of relevant posts from a dataset.

## 🚀 Features
- **Post Filtering:** Retrieve posts based on `length`, `language`, and `tags`.
- **UTF-8 Encoding Support:** Ensures that data is properly formatted for processing.
- **Optimized for LLaMA:** Helps prevent issues like response repetition by diversifying retrieval.
- **Customizable Retrieval Logic:** Fine-tune filters to extract better samples for few-shot learning.

## 📂 Project Structure
```
FewShotPosts/
│── data/
│   ├── raw_posts.json
    ├── processed_posts.json 
│── fewshot_posts.py       
│── main.py      
│── llm_helper.py
│── post_generator.py
│── preprocess_data.py                  
│── requirements.txt       
│── README.md             
```

## 🔧 Installation
```bash
git clone https://github.com/Niall1985/LlamaPost.git
cd LlamaPost

python -m venv venv
source venv/bin/activate
```

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



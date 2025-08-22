import os

structure = {
    "nodes": ["decision_node.py", "weather_node.py", "rag_node.py", "llm_node.py"],
    "utils": ["vectorstore.py", "pdf_loader.py"],
    "tests": ["test_weather.py", "test_llm.py", "test_rag.py"],
    "data": ["sample_data.pdf"],  
    "": ["app.py", "pipeline.py", "README.md", ".env", "requirements.txt"]
}

def create_structure(base="."):
    for i, j in structure.items():
        folder_path = os.path.join(base, i)
        if i and not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Created folder: {folder_path}")
        
        for file in j:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w") as f:
                    if file.endswith(".py"):
                        f.write("# " + file + "\n")
                    elif file == "README.md":
                        f.write("# AI Pipeline with LangChain, LangGraph & Groq\n")
                    elif file == ".env":
                        f.write("CHAT_GROQ_API_KEY=\nLANGCHAIN_API_KEY=\nOPENWEATHERMAP_API_KEY=\nQDRANT_URL=http://localhost:6333\n")
                print(f"Created file: {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\n Project template generated! Now paste code into the files.")

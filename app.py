import streamlit as st
import requests
import markdown


st.set_page_config(page_title="Create blog post", page_icon="📝", layout="wide")

st.title("Create blog post")
st.markdown("This app is an interface where you can write articles about AI agents from CodeGPT")

# Menú principal
with st.sidebar:
    st.header("Configuration")
    codegpt_api_key = st.text_input("CodeGPT API Key", type="password")
    codegpt_org_id = st.text_input("CodeGPT-Org-Id", type="password")

# List of agents
def get_agents():
    url = "https://api.codegpt.co/api/v1/agents"
    headers = {
        "Authorization": f"Bearer {codegpt_api_key}",
        "CodeGPT-Org-Id": codegpt_org_id
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error loading agents: {response.status_code}")
        return []

if st.button("Load agents from the marketplace"):
    agents = get_agents()
    if agents:
        st.session_state.agents = agents
        st.session_state.selected_agent = None

if 'agents' in st.session_state:
    selected_agent = st.selectbox("Select an agent", 
                                  options=st.session_state.agents, 
                                  format_func=lambda x: x['name'])
    if selected_agent:
        st.session_state.selected_agent = selected_agent

def generate_tech_blog_article(agent_id, agent_name, codegpt_api_key, codegpt_org_id):
    url = "https://api.codegpt.co/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {codegpt_api_key}",
        "CodeGPT-Org-Id": codegpt_org_id,
        "Content-Type": "application/json"
    }
    
    article_prompt = f"""
Write a comprehensive, engaging, and well-structured article for developers about {agent_name}, focusing on how CodeGPT provides an expert agent for this technology that can be used as a code assistant in Visual Studio Code. Follow this structure:

1. Title: Create an attention-grabbing title that includes "{agent_name}" and highlights how developers can supercharge their work with an AI expert assistant in VSCode.

2. Introduction:
   - Start with an impactful statement about developing with {agent_name}
   - Briefly introduce {agent_name} and its importance in the development world
   - Mention how CodeGPT offers an expert agent in {agent_name} for VSCode
   - Provide a concise overview of what the article will cover

3. Overview of {agent_name}:
   - Detailed explanation of {agent_name}, its features, and applications
   - Advantages and common challenges when working with {agent_name}
   - Current trends and future of {agent_name} in software development

4. Introduction to CodeGPT's {agent_name} expert agent:
   - What CodeGPT is and how it provides expert agents for different technologies
   - Specific features of the {agent_name} expert agent
   - How it differs from other generic AI code assistants

5. Setting up and using the expert agent in VSCode:
   - Step-by-step guide to install the CodeGPT extension in Visual Studio Code
   - How to access CodeGPT's agent marketplace and select the {agent_name} expert
   - Instructions for opening the chat within VSCode to interact with the agent
   - Tips for effectively communicating with the agent in the VSCode environment

6. Enhancing {agent_name} development with the expert agent:
   - 3-5 specific use cases with before and after code examples
   - Demonstration of how the agent improves productivity and code quality
   - Tips for formulating effective queries related to {agent_name}

7. Advanced features of the {agent_name} expert agent:
   - Premium or advanced functionalities specific to this technology
   - How these features can boost {agent_name} development

8. Best practices and tips:
   - Expert recommendations for making the most of the agent in {agent_name} projects
   - Common pitfalls to avoid
   - How to stay updated with new agent features

9. Conclusion:
   - Recap of the key points from the article
   - Emphasis on the benefits of using CodeGPT's {agent_name} expert agent in VSCode
   - Call-to-action: Encourage readers to install the CodeGPT extension and try the expert agent in their {agent_name} projects

Throughout the article:
- Use a professional yet conversational tone, aimed at developers
- Include relevant subheadings for easy navigation
- Incorporate bullet points and numbered lists for readability
- Add internal links to CodeGPT documentation or relevant {agent_name} resources
- Use markdown formatting for headings, code snippets, and emphasis
- Emphasize the importance of installing the CodeGPT extension, selecting the appropriate expert agent, and using the in-VSCode chat for interaction

Aim for an article length of 1500-2000 words that provides comprehensive value to developers of all experience levels with {agent_name}.
"""

    data = {
        "agentId": agent_id,
        "stream": False,
        "format": "text",
        "messages": [{
            "content": article_prompt,
            "role": "user"
        }]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.text
    else:
        # show all response data
        response = response.json()
        # {'message': 'Agent with ID 5022f8af-bcf3-4a37-a33c-981f879d6c7b not found in organization with ID: 31352da0-1a51-4fce-890c-6a8c30277f94.'}
        return f"Error generating article: {response['message']}"

if st.button("Create article"):
    if 'selected_agent' in st.session_state and st.session_state.selected_agent:
        article = generate_tech_blog_article(
            st.session_state.selected_agent['id'],
            st.session_state.selected_agent['name'],
            codegpt_api_key,
            codegpt_org_id
        )
        st.session_state.article = article
    else:
        st.warning("Please select an agent first.")

if 'article' in st.session_state:
    st.markdown("### Update your article")
    edited_article = st.text_area("Edit your article in Markdown", value=st.session_state.article, height=400)
    
    
    st.markdown("### preview:")
    st.markdown(markdown.markdown(edited_article), unsafe_allow_html=True)

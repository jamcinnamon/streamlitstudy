import streamlit as st

st.set_page_config(page_title='page1', page_icon=':coffee:')
import streamlit as st
from langchain_core.messages.chat import ChatMessage
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt
# https://docs.streamlit.io/develop/api-reference/chat/st.chat_message

st.set_page_config(page_title='전자책 가이드라인', page_icon=':sparkles:')
# API KEY 로드 
load_dotenv()



st.title('전자책 :blue[가이드라인] :sparkles:')
page_icon=(":sparkles:")
add_selectbox = st.sidebar.selectbox(
    "나도 이제 작가?",
    ("기본", "주제와 함께 템플릿 이용해보기")
)
maintxt = '''
전자책 기본 가이드라인을 소개합니다 :white_check_mark:

구성으로 책 제목, 목차, 글 내용, 저작권법 안내
'''
st.markdown(maintxt)

prompt = load_prompt('modifiedtitle.yaml')
model = ChatOpenAI(model='gpt-4o-mini', temperature=0.5)
outputparser = StrOutputParser()

# 세션 상태 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("원하시는 전자책을 만들어보세요")

if user_input:
    print(st.chat_message("user"))
    st.session_state.messages.append({"role": "user", "content": user_input})




    # 선택된 옵션에 따른 프롬프트 템플릿 설정
    if add_selectbox == "기본":
        prompt_template = PromptTemplate.from_template(
            "사용자가 책 주제를 못 정했으면 요즘 유행하는 전자책 테마 5개를 추천해줘. 그 아래에 소제목 5개를 뽑아줘."
        )
    elif add_selectbox == "주제와 함께 템플릿 이용해보기":
        prompt_template = load_prompt('modifiedtitle.yaml')
        






import streamlit as st
from dotenv import load_dotenv

from Generator import generate_learning_path
load_dotenv()

st.set_page_config(page_title="Learning path Generator")
st.title("Learning Path Generator")
st.caption("Enter a skill or domain to get a structured learning roadmap.")

skill=st.text_input("skill or domain", placeholder="eg. Data Science, pandas, Rust")

generate_clicked=st.button("Generator roadmap",type='primary',disabled=not skill.strip())

if generate_clicked:
    with st.spinner("Generating roadmap..."):
        try:
            result=generate_learning_path(skill)
        except RuntimeError as e:
            st.error(Str(e))
            st.stop()
        except Exception as e:
            st.error(f"Generator failed: {e}")
            st.stop()

    st.subheader("Learning stages")
    for i, stage in enumerate(result.learning_stages,start=1):
        st.markdown(f"**{i}.{stage}**")

    st.subheader("Key Topics")
    for topic in result.key_topics:
        st.markdown(f"- {topic}")

    st.subheader("summary")
    st.write(result.learning_goal_summary)

    with st.expander("Raw JSON"):
        st.json(result.model_dump())

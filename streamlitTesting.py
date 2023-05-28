# streamlit run streamlitTesting.py

import streamlit as st


def main():
    st.title("Streamlit Testing")
    
    st.sidebar.write('Sanjay Katta')
    
    x = st.sidebar.slider("Select a value")
    st.sidebar.write(x, "squared is", x * x)
    
    st.text("Text")
    
    # Custom CSS to set the theme to white
    st.markdown(
    """
        <style>
            body {
                color: black;
                background-color: white;
            }
        </style>
    """,
        unsafe_allow_html=True
    )
    
    


    
    st.title("Streamlit Demo Manifold AI learning Murthy") 
    st.header(" Heading of Streamlit") 
    st.subheader("Sub- Heading of Streamlit") 
    st.text("This is an Example Text") 
    st.success("Success") 
    st.warning("warning") 
    st.info("information") 
    st.error("Error") 
    
    if st.checkbox ("Select/Unselect"): 
        st.text("User selected the checkbox") 
    else: 
        st.text("User has not selected the checkbox") 
    
    state = st.radio ("What is your favorite Color ?", ("Red", 'Green', "yellow"))
    
    if state == 'Green':
            st.success("That my favorite color as well")
            
    occupation = st.selectbox("What do you do?",["Student","Vlogger","Engineer"])
    
    st.text(f"Selected option is {occupation}")
    
    if st.button("Example Button"):
        st.error("You clicked it")
        
    st.sidebar.header("Heading of Sidebar")
    st.sidebar.text("Sanjay Katta")
    
if __name__ == '__main__':
    main()    
import streamlit as st
import streamlit.components.v1 as components

def InitPageSetting(st, path, PAGE_NAME, PAGE_ICON, name_file_css="", name_file_js=""):
    current_dir = path
    CSS_MAIN = current_dir / "assets" / "styles" / "main.css"
    js_MAIN = current_dir / "assets" / "js" / "main.js"
    st.set_page_config(PAGE_NAME, PAGE_ICON)
    Custom_Code(st, """
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"/>            
    """)
    if name_file_css:
        css_file = current_dir/"assets" / "styles" / name_file_css
        Custom_CSS(st, CSS_MAIN)
        Custom_CSS(st, css_file)
    else:
        Custom_CSS(st, CSS_MAIN)

    if name_file_js:
        js_file = current_dir/"assets" / "js" / name_file_js
        Custom_JS(st, js_MAIN)
        Custom_JS(st, js_file)
    else:
        Custom_JS(st, js_MAIN)


def Custom_CSS(st, css_file):
    with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()),
                    unsafe_allow_html=True)


def Custom_Code(st, data):
    st.markdown(data, unsafe_allow_html=True)


def Custom_JS(st, js_file):
    with open(js_file) as f:
        html_string = '<script language="javascript">{}</script>'.format(f.read())
        components.html(html_string) 
        st.markdown(html_string,
                    unsafe_allow_html=True)
# Bismillahirrahumanirrahim
import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()

def logout():
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

login_page = st.Page(login, title="Log in", icon=":material/login:")
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "reports/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
bugs = st.Page("reports/bugs.py", title="Bug reports", icon=":material/bug_report:")
alerts = st.Page(
    "reports/alerts.py", title="System alerts", icon=":material/notification_important:"
)

search = st.Page("tools/search.py", title="Search", icon=":material/search:")
history = st.Page("tools/history.py", title="History", icon=":material/history:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
        }
    )
else:
    pg = st.navigation([login_page])

pg.run()






























#from user_login import st_user_login 
# st.write(" Bismillahirrahumanirrahim")
#st.header("Testing...")
# st.title("Bismillah")
# st.write("Test" , __name__)
# if __name__ == '__main__':
  # app_user = st_user_login()
  # st.write(" Ret Value", app_user)
  # pg = st.navigation([st.Page("page_1.py"), st.Page(page_2)])
  # pg.run()  

  # pg = st.navigation([st.Page("Vessel_Master.py"), st.Page("entry_screen.py")])
  #  pg = st.navigation([st.Page("entry_screen.py")]) 
  # st.switch_page(pg)
  # if app_user == "VSL":
  #st.switch_page(st.Page("entry_screen.py"))

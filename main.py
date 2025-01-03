# Bismillahirrahumanirrahim
import streamlit as st
import time

st.logo("logo/sample_logo_image.jpg", icon_image="logo/sample_logo_image_1.jpg")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.toast('Welcome Guest!', icon='😍')
    side_bar_nav = st.get_option('client.showSidebarNavigation')
    st.toast(f" Side Bar Navigation is {side_bar_nav}")

def login():
    
    user_name = st.text_input(label="User Name", value="", placeholder="Please Enter Your Login", max_chars=20)
    user_pwd = st.text_input(label="Password", type="password", 
                             placeholder="Please enter your passwod", 
                             help="Please enter your password",
                             max_chars=25)

    if st.button("Log in"):
        if user_name == "Vessel123" and user_pwd == "Vessel@123":  
            st.snow()
            st.success("You have successfully logged in to the system")
            go_to_app = "VSL"
            # st.switch_page("entry_screen.py")
        elif user_name == "Tbt123" and user_pwd == "Tbt@123":
            st.balloon()
            st.success("You have successfully logged in to the system")
            go_to_app = "TBT"
            # st.switch_page("entry_screen.py")
        else:
            st.error("Error, entering user name and/or password. Please contact the Administrator")
            st.stop()
              
        st.session_state.logged_in = True
        time.sleep(.5)
        st.toast(f'Welcome Mr. {user_name}!', icon='🎉')
        time.sleep(1)
        st.snow()
        st.rerun()

def logout():
    st.header("Thank for using this Application!. \n \n \n Hope You enjoyed it!!!")
    
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.toast('See you soon!', icon='😍')
        time.sleep(1)
        st.balloons()
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

creatUser = st.Page("admin/createUsers.py", title="Create Users", icon=":material/man:")

#test_form = st.Page("RandD/randd_1.py", title="Sqlite3", icon=":material/rule_settings:")
#test_child_table = st.Page("RandD/forrm_with_child_table.py", title="Form Child Table", icon=":material/foot_bones:")
#img_related = st.Page("RandD/img_related.py", title="Image Related", icon=":material/eyeglasses:")

vessels = st.Page("Vessels/Vessels.py", title="Vessels", icon=":material/houseboat:")
vessel_reports = st.Page("Vessels/Vessel_Reports.py", title="Vessel Reports", icon=":material/tsunami:")

if st.session_state.logged_in:
    pg = st.navigation(
        {
            "Account": [logout_page, creatUser],
            "Vessels": [vessles, vessel_reports],
            "Reports": [dashboard, bugs, alerts],
            "Tools": [search, history],
            # "RandD": [test_form, test_child_table, img_related],
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

import os
import streamlit as st
from PIL import Image


def second_screen():
    # Get the current directory where the script is being executed
    current_dir = os.path.dirname(__file__)

    logo_image = os.path.join(current_dir, r"./../public/Config Pilot Logo.png")

    # Create a two-column layout for logo and title
    col1, col2 = st.columns([2, 4])  # Adjust column widths as needed
    with col1:
        st.image(logo_image, width=200)  # Display the logo

    with col2:
        st.title("ConfigPilot")
        st.subheader("Simplify Your Configurations")
        st.write(
            "ConfigPilot automates and simplifies network device configurations for routers, switches, and servers, offering step-by-step guidance for both IT professionals and non-technical users."
        )

    # Step-by-step guide (dummy data)
    st.title("How to Integrate with the App")
    steps = [
        "Step 1: Install the app on your device.",
        "Step 2: Connect the app to your router, switch, or server.",
        "Step 3: Follow the prompts for automatic configuration.",
        "Step 4: Monitor and manage your network remotely.",
    ]

    # Set the path for the images dynamically
    router_img_path = os.path.join(current_dir, r"assets\router.jpg")
    switch_img_path = os.path.join(current_dir, r"assets\switches.jpg")
    server_img_path = os.path.join(current_dir, r"assets\server.jpeg")

    # logo_image = os.path.join(current_dir, r"../../public/Config Pilot Logo.png")

    # st.image(logo_image, width=200)  # Placeholder for the logo

    st.title("Choose Your Device")

    col1, col2, col3 = st.columns(3)

    # Router selection
    with col1:
        # Check if the image file exists
        if os.path.exists(router_img_path):
            router_img = Image.open(router_img_path)
            st.image(router_img, caption="Router")
            if st.button("Select Router"):
                st.session_state["device_selected"] = "Router"
                st.session_state["screen"] = "device_questions"
        else:
            st.error(f"Image not found at {router_img_path}")

    # Switch selection
    with col2:
        # Check if the image file exists
        if os.path.exists(switch_img_path):
            switch_img = Image.open(switch_img_path)
            st.image(switch_img, caption="Switch")
            if st.button("Select Switch"):
                st.session_state["device_selected"] = "Switch"
                st.session_state["screen"] = "device_questions"
        else:
            st.error(f"Image not found at {switch_img_path}")

    # Server selection
    with col3:
        # Check if the image file exists
        if os.path.exists(server_img_path):
            server_img = Image.open(server_img_path)
            st.image(server_img, caption="Server")
            if st.button("Select Server"):
                st.session_state["device_selected"] = "Server"
                st.session_state["screen"] = "device_questions"
        else:
            st.error(f"Image not found at {server_img_path}")

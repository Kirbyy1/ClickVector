# import requests
#
# url = "https://api.loadingbay.com/app/v1/login/logout"
# headers = {
#     "Accept": "*/*",
#     "channel": "mkt-x20-official",
#     "Content-Length": "0",
#     "Content-Type": "application/json",
#     "Cookie": "sid=PW2pkqmDYCyBwvVP1hBAO4BpfvDYbbA_hL8UmY...",  # Use the full session ID
#     "cv": "w1.5.8.12",
#     "deviceid": "F0:09:0D:93:7A:61",
#     "gpus": '["AMD Radeon(TM) Graphics"]',
#     "Host": "api.loadingbay.com",
#     "locale": "en",
#     "region": "US",
#     "timestamp": "1738579163"
# }
#
# response = requests.post(url, headers=headers)
#
# print("Response Code:", response.status_code)
# print("Response Body:", response.text)
# import uiautomation as auto
#
# # Connect to the Market Rival application window (use the window title)
# window = auto.WindowControl(Name="Market Rivals")  # Replace with the exact window title
# print('window',    window)
#
# # Find the Play button by its name or identifier
# play_button = window.ButtonControl(Name="PLAY")  # Replace "Play" with the exact button name if different
#
# # Click the Play button
# play_button.Click()
import time

# import psutil
# import win32gui
# import win32process  # Import win32process for GetWindowThreadProcessId
#
#
# def list_open_windows():
#     # Get all running processes
#     for proc in psutil.process_iter(['pid', 'name']):
#         try:
#             # Get the process name and pid
#             pid = proc.info['pid']
#             name = proc.info['name']
#
#             # For Windows, use win32gui to get window titles by pid
#             def enum_windows_callback(hwnd, window_list):
#                 if win32gui.IsWindowVisible(hwnd):
#                     pid_window = win32process.GetWindowThreadProcessId(hwnd)[1]  # Get the PID of the window
#                     if pid_window == pid:
#                         window_title = win32gui.GetWindowText(hwnd)
#                         if window_title:
#                             window_list.append(window_title)
#
#             window_titles = []
#             win32gui.EnumWindows(enum_windows_callback, window_titles)
#
#             # If the process has windows, print their titles
#             if window_titles:
#                 for title in window_titles:
#                     print(f"Process: {name} | Window Title: {title}")
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#
#
import psutil
import win32gui
import win32process
from pywinauto import Application

def enum_windows_callback(hwnd, windows):
    """Callback function for EnumWindows to collect window handles."""
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    if pid == windows['pid']:  # Check if the PID matches
        windows['handles'].append(hwnd)

def get_window_by_pid(pid):
    """Get window handles for the given PID."""
    windows = {'pid': pid, 'handles': []}
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows['handles']

def find_process_pid(process_name):
    """Find the PID of the process by its name."""
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'].lower() == process_name.lower():
            return proc.info['pid']
    return None
time.sleep(1)
# Find PID for Marvel-Win64-Shipping.exe or Marvel.exe
pid = find_process_pid("Marvel-Win64-Shipping.exe")  # Use "Marvel.exe" if that's the process name

if pid:
    print(f"Found process: {pid}")

    # Get window handles using the PID
    hwnds = get_window_by_pid(pid)

    if hwnds:
        # Connect to the application using pywinauto
        app = Application(backend="win32").connect(handle=pid)

        # Get the window
        window = app.window(title="Marvel Rivals")

        # Bring the window to the foreground and restore it (if minimized)
        window.set_focus()

        # window.restore()

        # Fetch the window's title (you already have this)
        # List all controls (children) inside the window
        children = window.children()

        # Print out all the controls' titles and control types
        # Get all descendants (nested controls) inside the window
        descendants = window.descendants()

        for control in descendants:
            print(f"Control: {control} | Title: {control.window_text()} | Control Type: {control.control_type}")

        # Interact with other controls, for example, clicking a button or setting text in a text field
        # Example: Find a button by its title and click it
        # try:
        #     play_button = window.child_window(title="PLAY", control_type="Button")  # Adjust control properties as necessary
        #     play_button.click()
        #     print("Clicked the Play button.")
        # except Exception as e:
        #     print("Couldn't find the Play button:", e)

        # Example: Get the value of an edit box (text field)
        # try:
        #     text_field = window.child_window(control_type="Edit")
        #     print("Text Field Value:", text_field.get_value())
        # except Exception as e:
        #     print("Couldn't find text field:", e)

        # Example: Get a label's text
        # try:
        #     label = window.child_window(control_type="Text")
        #     print("Label Text:", label.window_text())
        # except Exception as e:
        #     print("Couldn't find label:", e)
    else:
        print("No windows found for this process.")
else:
    print("Process not found.")

import webbrowser
import os

embedded_url = "https://browser.rammerhead.org/8093f1cbe3e44bcc801c9be3cf314bb1/_rhsknGRH://W40.R2mG2G.GXK/?W5F_I0=JtF"

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Google</title>
</head>
<body style="margin: 0; overflow: hidden;">
    <iframe src="{embedded_url}" frameborder="0" style="width: 100vw; height: 100vh;"></iframe>
</body>
</html>
"""

file_path = "google.html"
with open(file_path, "w") as file:
    file.write(html_content)

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"  

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open_new_tab(f"file://{os.path.abspath(file_path)}")

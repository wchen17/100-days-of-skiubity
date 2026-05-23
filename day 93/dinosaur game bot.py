from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("chrome://dino")

body = driver.find_element(By.TAG_NAME, "body")
body.send_keys(Keys.SPACE)
time.sleep(1)


def get_game_state():
    js = (
        "var runner = Runner.instance_; "
        "return { "
        "  crashed: runner.crashed, "
        "  currentSpeed: runner.currentSpeed, "
        "  obstacles: runner.horizon.obstacles.map(function(o){ "
        "    return {x: o.xPos, y: o.yPos, width: o.width}; "
        "  }) "
        "};"
    )
    return driver.execute_script(js)


JUMP_THRESHOLD = 300

while True:
    try:
        state = get_game_state()
        if state["crashed"]:
            print("Game over!")
            break
        for obs in state.get("obstacles", []):
            if obs["x"] < JUMP_THRESHOLD:
                body.send_keys(Keys.SPACE)
                time.sleep(0.1)
                break
        time.sleep(0.05)
    except Exception as e:
        print(f"Error: {e}")
        break

driver.quit()

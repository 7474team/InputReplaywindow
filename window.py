import time
import pyautogui
import keyboard
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QStringListModel, QTimer
from PySide6.QtWidgets import QWidget, QMessageBox, QPushButton, QVBoxLayout
from UI.example_UI import Ui_Dialog
import sys
from threading import Thread
from qt_material import apply_stylesheet
import mouse

class WidgetA_UiEN13231(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.mou_click.clicked.connect(self.mou_clicked)
        self.ui.mou_move.clicked.connect(self.mou_moveed)
        self.ui.keyboard_input.clicked.connect(self.keyboard_input)


        self.ui.GO_pushbutton.clicked.connect(self.GO_pushbuttoned)
        self.ui.record_realtime_button.clicked.connect(self.record_realtime)

        self.ui.del_pushButton.clicked.connect(self.pushButton_del)
        self.ui.up_pushButton.clicked.connect(self.pushButton_up)
        self.ui.dow_pushButton.clicked.connect(self.pushButton_dow)
        
        self.data = []
        self.qList = []
        self.slm = QStringListModel()
        self.slm.setStringList(self.qList)        
        self.ui.listView.setModel(self.slm)
        self.ui.listView.doubleClicked.connect(self.listViewclicked)

        self.is_recording = False
        self.noGO=False
        self.thread = Thread (target=self.re_mouXY)
        self.thread.start()
            # 設置全局熱鍵 F5 執行 GO_pushbuttoned
        keyboard.add_hotkey('f9', self.GO_pushbuttoned)
            # 設置一個計時器來檢查F9鍵的狀態
        self.f9_timer = QTimer(self)
        self.f9_timer.timeout.connect(self.check_f9_key)
        self.f9_timer.start(100)  # 每100毫秒檢查一次
        self.last_f9_press_time = 0
        self.f9_cooldown = 1.0  # 冷卻時間（秒）
        
    def check_f9_key(self):
        """檢查F9鍵的狀態，並在適當的時候觸發GO_pushbuttoned"""
        current_time = time.time()
        
        # 檢查F9鍵是否被按下
        if keyboard.is_pressed('f9'):
            # 檢查是否已經過了冷卻時間
            if current_time - self.last_f9_press_time > self.f9_cooldown:
                self.GO_pushbuttoned()
    def __del__(self):
        # 清理熱鍵
        try:
            keyboard.remove_hotkey('f9')
        except:
            pass
        
        # 確保線程正確終止
        self.noGO = True

    def mou_clicked(self):
        LClick = self.ui.LClick_checkBox.isChecked()
        doubleclick = self.ui.douClick_checkBox.isChecked()
        data = {"type": "click", "left": LClick, "doubleclick": doubleclick,"time":self.ui.movespe_textEdit_longtime.toPlainText()}
        self.data.append(data)
        self.updata_Listview()

    def mou_moveed(self):
        X = self.ui.mouX_textEdit.toPlainText()
        Y = self.ui.mouY_textEdit.toPlainText()
        speed = self.ui.movespe_textEdit.toPlainText()
        data = {"type": "move", "X": X, "Y": Y, "speed": float(speed),"time":self.ui.movespe_textEdit_longtime.toPlainText()}
        self.data.append(data)
        self.updata_Listview()
    # 在 keyboard_input 方法中，可以添加一個選項來指定是否使用小鍵盤
    def keyboard_input(self):
        key_input = self.ui.movespe_textEdit_keyboard.toPlainText()
        
        data = {
            "type": "keyboard", 
            "key": key_input, 
            "time": self.ui.movespe_textEdit_longtime.toPlainText(),
        }
        self.data.append(data)
        self.updata_Listview()

    def GO_pushbuttoned(self):
        print("go")
             # 定義特殊按鍵列表
        special_keys = ['enter', 'tab', 'esc', 'escape', 'backspace', 'delete', 'space', 
                    'up', 'down', 'left', 'right', 'home', 'end', 'pageup', 'pagedown',
                    'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f10', 'f11', 'f12']
        # 導入剪貼板模塊
        import pyperclip
        for roi in self.data:
            print(roi)
            match roi.get("type", None):
                case "keyboard":
                    try:
                        # 處理組合鍵
                        key_input = roi["key"]
                        
                        if "+" in key_input and not any(ord(c) > 127 for c in key_input):
                            keys = key_input.split("+")
                            for k in keys[:-1]:
                                keyboard.press(k.strip())
                            # 按下並釋放最後一個鍵
                            keyboard.press_and_release(keys[-1].strip())
                            # 釋放所有之前按下的鍵（從後往前）
                            for k in reversed(keys[:-1]):
                                keyboard.release(k.strip())
                            # 處理單個特殊按鍵
                        elif key_input.lower() in special_keys:
                            # 直接使用keyboard模塊處理特殊按鍵
                            keyboard.press_and_release(key_input.lower())
                        else:
                                original_clipboard = pyperclip.paste()
                                print (key_input)
                                # 將要輸入的文本複製到剪貼板
                                pyperclip.copy(key_input)
                                
                                # 使用Ctrl+V粘貼
                                keyboard.press('ctrl')
                                keyboard.press_and_release('v')
                                keyboard.release('ctrl')
                                
                                # 等待粘貼完成
                                time.sleep(0.2)
                                # 恢復原始剪貼板內容
                                pyperclip.copy(original_clipboard)
                      
                            
                    except Exception as e:
                        print(f"無法執行鍵盤操作: {e}")
                        # 如果出錯，嘗試使用最基本的方式輸入
                        try:
                            pyautogui.write(key_input, interval=0.1)
                        except Exception as e2:
                            print(f"備用輸入也失敗: {e2}")
                
                case "move":  # 處理滑鼠移動
                    pyautogui.moveTo(int(roi["X"]), int(roi["Y"]), duration=float(roi["speed"]))
                
                case "click":  # 處理滑鼠點擊
                    click = 2 if roi.get("doubleclick", False) else 1
                    button = 'left' if roi.get("left", True) else 'right'
                    pyautogui.click(button=button, clicks=click, interval=0.1)

            # 每個操作後的延遲處理
            try:
                wait_time = float(roi["time"])
                if wait_time > 0:
                    time.sleep(wait_time)
            except (ValueError, KeyError):
                pass  # 如果轉換失敗或沒有time鍵，不等待
                    

    def updata_Listview(self):
        self.qList.clear()
        for roi in self.data:
            self.qList.append(str(roi)) 
        # print(self.qList)
        self.slm.setStringList(self.qList)
        
    def re_mouXY(self):
        while(True):
            self.ui.MOUXY_label.setText(str(pyautogui.position()))
            self.mou_X = pyautogui.position().x
            self.mou_Y = pyautogui.position().y
            
            if (self.noGO):
                break 
            time.sleep(0.05)

    def pushButton_del(self):
        try:
            del self.data[self.ui.listView.currentIndex().row()]
            self.updata_Listview()
        except Exception as e:
            button = QMessageBox.information(self, "通知", "沒有資料")

            if button == QMessageBox.StandardButton.Ok:
                return True

    def pushButton_up(self):
        try:
            index = self.ui.listView.currentIndex().row()
            if (index > 0 and index < len(self.data)):
                a2 = self.data.pop(index)
                self.data.insert(index-1, a2)
            self.updata_Listview()
        except Exception as e:
            button = QMessageBox.information(self, "通知", "沒有資料")

            if button == QMessageBox.StandardButton.Ok:
                return True

    def pushButton_dow(self):
        try:
            index = self.ui.listView.currentIndex().row()
            if (index >= 0 and index < len(self.data)):
                a2 = self.data.pop(index)
                self.data.insert(index+1, a2)
            self.updata_Listview()
        except Exception as e:
            button = QMessageBox.information(self, "通知", "沒有資料")

            if button == QMessageBox.StandardButton.Ok:
                return True
    
    def record_realtime(self):
        """切換錄製狀態"""
        if not self.is_recording:
            # 開始錄製
            self.is_recording = True
            self.ui.record_realtime_button.setText("esc結束錄製")
            self.ui.record_realtime_button.setStyleSheet("background-color: red;")
            # 初始化滑鼠按鍵狀態
            self.mouse_pressed = {'left': False, 'right': False}
            # 初始化鍵盤狀態追踪
            self.pressed_keys = set()  # 用於存儲當前按下的所有鍵
            self.last_key_time = time.time()  # 上次鍵盤事件的時間
            self.key_combination_timeout = 0.5  # 組合鍵的超時時間（秒）
            # 設置鍵盤鉤子
            keyboard.hook(self.on_key_event)
            # 設置滑鼠鉤子
            mouse.on_click(lambda: self.on_mouse_press('left'))
            mouse.on_right_click(lambda: self.on_mouse_press('right'))
            
        else:
            # 停止錄製
            self.stop_recording()
    
    def stop_recording(self):
        """停止錄製"""
        if self.is_recording:
            self.is_recording = False
            self.ui.record_realtime_button.setText("開始錄製")
            self.ui.record_realtime_button.setStyleSheet("")
            
            # 取消鍵盤鉤子
            keyboard.unhook_all()
            
 
    def on_key_event(self, event):
        """處理鍵盤事件，支持組合鍵"""
        if not self.is_recording:
            return
        
        # 如果按下ESC鍵，停止錄製
        if event.name == 'esc' and event.event_type == keyboard.KEY_DOWN:
            self.stop_recording()
            return
        
        current_time = time.time()
        
        if event.event_type == keyboard.KEY_DOWN:
            # 添加到當前按下的鍵集合
            self.pressed_keys.add(event.name)
            self.last_key_time = current_time
        
        elif event.event_type == keyboard.KEY_UP:
            # 從當前按下的鍵集合中移除
            if event.name in self.pressed_keys:
                self.pressed_keys.remove(event.name)
                
                # 如果所有鍵都已釋放或者超過了組合鍵的超時時間，記錄組合鍵
                if not self.pressed_keys or (current_time - self.last_key_time > self.key_combination_timeout):
                    # 獲取所有當前按下的鍵（包括剛剛釋放的鍵）
                    all_keys = list(self.pressed_keys) + [event.name]
                    
                    # 排除特殊鍵（如果需要）
                    valid_keys = [k for k in all_keys if k not in ['left', 'right']]
                    
                    if valid_keys:
                        # 如果只有一個鍵，直接記錄
                        if len(valid_keys) == 1:
                            key_data = {"type": "keyboard", "key": valid_keys[0], "time": 0.5}
                        else:
                            # 如果有多個鍵，記錄為組合鍵
                            key_combination = "+".join(valid_keys)
                            key_data = {"type": "keyboard", "key": key_combination, "time": 0.5}
                        
                        # 添加到數據列表
                        self.data.append(key_data)
                        self.updata_Listview()
                        
                        # 清空已處理的鍵
                        self.pressed_keys.clear()
    
    def on_mouse_press(self, button):
        """處理滑鼠按下事件"""
        if not self.is_recording:
            return
        
        # 避免重複記錄
        if self.mouse_pressed[button]:
            return
        
        self.mouse_pressed[button] = True
        
        # 在點擊前記錄當前滑鼠位置
        current_position = pyautogui.position()
        
        # 記錄移動到點擊位置
        move_data = {"type": "move", "X": current_position.x, "Y": current_position.y, 
                    "speed": 0.1, "time": 0.5}
        
        self.data.append(move_data)
        
        # 記錄點擊
        is_left = (button == 'left')
        click_data = {"type": "click", "left": is_left, "doubleclick": False, "time": 0.1}
        self.data.append(click_data)
        self.updata_Listview()
        """重置滑鼠按鍵狀態"""
        self.mouse_pressed[button] = False
        # # 重置狀態 - 設置一個短暫的延遲後重置
        # import threading
        # threading.Timer(0.2, lambda: self.reset_mouse_state(button)).start()
        
    def reset_mouse_state(self, button):
        """重置滑鼠按鍵狀態"""
        self.mouse_pressed[button] = False

    def listViewclicked(self, index):
        """處理列表項目被點擊的事件"""
        try:
            # 獲取被點擊的項目索引
            row = index.row()
            if 0 <= row < len(self.data):
                # 獲取該項目的數據
                item_data = self.data[row]
                
                # 根據項目類型顯示相關信息或設置相關控件
                if "type" in item_data:
                    match item_data["type"]:
                        case "keyboard":
                            # 如果是鍵盤操作，設置鍵盤輸入框的值
                            if "key" in item_data:
                                self.ui.movespe_textEdit_keyboard.setPlainText(item_data["key"])
                        
                        case "click":
                            # 如果是滑鼠移動，設置坐標和速度
                            if "X" in item_data and "Y" in item_data:
                                self.ui.mouX_textEdit.setPlainText(str(item_data["X"]))
                                self.ui.mouY_textEdit.setPlainText(str(item_data["Y"]))
                            if "speed" in item_data:
                                self.ui.movespe_textEdit.setPlainText(str(item_data["speed"]))
                        
                        case "move":
                            # 如果是滑鼠點擊，設置點擊類型
                            if "left" in item_data:
                                self.ui.LClick_checkBox.setChecked(item_data["left"])
                            if "doubleclick" in item_data:
                                self.ui.douClick_checkBox.setChecked(item_data["doubleclick"])
                    if "time" in item_data:
                        self.ui.movespe_textEdit_longtime.setPlainText(str(item_data["time"]))
        
        except Exception as e:
            # 處理可能的錯誤
            print(f"列表點擊處理錯誤: {e}")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    w = WidgetA_UiEN13231()
    w.show()    
    app.exec()  # 在 PySide6 中 exec_() 已更改為 exec()
    w.noGO = True
    sys.exit()

    QWidget

    

def GO_pushbuttoned(self):
    print("go")
    for roi in self.data:
        print(roi)
        match roi.get("type", None):
            case "keyboard":
                try:
                    # 處理組合鍵
                    key_input = roi["key"]
                    if "+" in key_input:
                        # 如果是組合鍵（例如 "alt+tab"）
                        keys = key_input.split("+")
                        # 按下所有鍵
                        for k in keys[:-1]:
                            keyboard.press(k.strip())
                        # 按下並釋放最後一個鍵
                        keyboard.press_and_release(keys[-1].strip())
                        # 釋放所有之前按下的鍵（從後往前）
                        for k in reversed(keys[:-1]):
                            keyboard.release(k.strip())
                    else:
                        # 如果是單個鍵
                        keyboard.press_and_release(key_input)
                except Exception as e:
                    print(f"無法執行鍵盤操作: {e}")
            
            case "move":  # 處理滑鼠移動
                pyautogui.moveTo(int(roi["X"]), int(roi["Y"]), duration=float(roi["speed"]))
            
            case "click":  # 處理滑鼠點擊
                click = 2 if roi.get("doubleclick", False) else 1
                button = 'left' if roi.get("left", True) else 'right'
                pyautogui.click(button=button, clicks=click, interval=0.1)

        # 每個操作後的延遲處理
        try:
            wait_time = float(roi["time"])
            if wait_time > 0:
                time.sleep(wait_time)
        except (ValueError, KeyError):
            pass  # 如果轉換失敗或沒有time鍵，不等待

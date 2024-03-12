import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Canvas
from PIL import ImageGrab, Image
import pytesseract
import webbrowser
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

DUNGEON_URL_SUFFIXES = {
    "サスタシャ侵食洞": "106",
    "タムタラの墓所": "482",
    "カッパーベル銅山": "489",
    "ハラタリ修練所": "808",
    "トトラクの千獄": "864",
    "ハウケタ御用邸": "907",
    "ブレイフロクスの野営地": "1240",
    "カルン埋没寺院": "1058",
    "カッターズクライ": "1034",
    "ストーンヴィジル": "1472",
    "ゼーメル要塞": "1523",
    "オーラムヴェイル": "1571",
    "ワンダラーパレス": "3971",
    "カストルム・メリディアヌム": "2137",
    "魔導城プラエトリウム": "2195",
    "古城アムダプール": "4009",
    "シリウス大灯台": "4038",
    "カッパーベル銅山(Hard)": "4240",
    "ハウケタ御用邸(Hard)": "4321",
    "古アムダプール市街": "4211",
    "ハラタリ修練所(Hard)": "4240",
    "ブレイフロクスの野営地(Hard)": "4321",
    "ハルブレーカー・アイル": "4513",
    "タムタラの墓所(Hard)": "4973",
    "ストーンヴィジル(Hard)": "7186",
    "スノークローク大氷壁": "2341",
    "サスタシャ侵食洞(Hard)": "2341",
    "カルン埋没寺院(Hard)": "7225",
    "黙約の塔": "2408",
    "ワンダラーパレス(Hard)": "7346",
    "古城アムダプール(Hard)": "7374",
    "ダスクヴィジル": "2542",
    "ソーム・アル": "2626",
    "ドラゴンズエアリー": "2694",
    "イシュガルド教皇庁": "2788",
    "グブラ幻想図書館": "2836",
    "魔科学研究所": "3427",
    "ネバーリープ": "6095",
    "フラクタル・コンティニアム": "6127",
    "聖モシャーヌ植物園": "6067",
    "シリウス大灯台(Hard)": "7396",
    "逆さの塔": "3628",
    "古アムダプール市街(Hard)": "5889",
    "ソール・カイ": "3911",
    "ハルブレーカー・アイル(Hard)": "7424",
    "ゼルファトル": "4135",
    "グブラ幻想図書館(Hard)": "5863",
    "バエサルの長城": "4266",
    "ソーム・アル(Hard)": "6801",
    "セイレーン海": "4540",
    "紫水宮": "5153",
    "バルダム覇道": "4739",
    "ドマ城": "4781",
    "カストルム・アバニア": "4851",
    "アラミゴ": "4890",
    "クガネ城": "6007",
    "星導山寺院": "6042",
    "スカラ": "5013",
    "獄之蓋": "6929",
    "フラクタル・コンティニアム(Hard)": "7448",
    "ガンエン廟": "7096",
    "ザ・バーン": "5071",
    "聖モシャーヌ植物園(Hard)": "7484",
    "ギムリトダーク": "5099",
    "ホルミンスター": "5182",
    "ドォーヌ・メグ": "5214",
    "キタンナ神影洞": "5277",
    "マリカの大井戸": "5308",
    "グルグ火山": "5335",
    "アーモロート": "5404",
    "シルクス・ツイニング": "5637",
    "アナイダアカデミア": "5668",
    "グラン・コスモス": "5466",
    "アニドラス・アナムネーシス": "5498",
    "ノルヴラント": "5533",
    "マトーヤのアトリエ": "5914",
    "パガルザン": "8611",
    "ゾットの塔": "9913",
    "バブイルの塔": "9941",
    "ヴァナスパティ": "10036",
    "ヒュペルボレア造物院": "10065",
    "アイティオン星晶鏡": "10097",
    "レムナント": "10161",
    "スマイルトン": "10220",
    "スティグマ・フォー": "10253",
    "アルザダール海底遺跡群": "10545",
    "トロイアコート": "10698",
    "ラピス・マナリス": "11102",
    "ハーム島": "11325",
    "月の地下渓谷": "11560",
}

def resize_image(image, scale_factor):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    return image.resize((new_width, new_height), Image.ANTIALIAS)

class SelectionApp:
    def __init__(self, root):
        self.root = root
        self.selection_win = None
        self.canvas = None
        self.start_x = None
        self.start_y = None
        self.rect = None
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.final_coords = None

    def start_selection(self):
        self.selection_win = Toplevel(self.root)
        self.selection_win.overrideredirect(True)
        self.selection_win.attributes("-alpha", 0.3)
        self.selection_win.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.canvas = Canvas(self.selection_win, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if not self.rect:
            self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="blue")

    def on_drag(self, event):
        curX = self.canvas.canvasx(event.x)
        curY = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_release(self, event):
        curX, curY = event.x_root, event.y_root
        self.final_coords = (min(self.start_x, curX), min(self.start_y, curY), max(self.start_x, curX), max(self.start_y, curY))
        self.selection_win.destroy()
        self.capture_selection()
    
    def capture_selection(self):
        if self.final_coords:
            bbox = self.final_coords
            img = ImageGrab.grab(bbox=bbox)
            
            img = resize_image(img, 2)
            
            text = pytesseract.image_to_string(img, lang='jpn')
            normalized_text = text.replace(" ", "").replace("|", "").replace("の", "の")
            print("正規化されたテキスト:", normalized_text)
        
            found = False
            for dungeon_name, url_suffix in DUNGEON_URL_SUFFIXES.items():
                if dungeon_name in normalized_text:
                    url = f"https://ru-eka.com/archives/{url_suffix}"
                    webbrowser.open(url)
                    found = True
                    print(f"マッチしたダンジョン名: {dungeon_name}, URL: {url}")
                    break
                
            if not found:
                print("マッチするダンジョン名が見つかりません。")
                    

class DarkThemeApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        self.root.configure(bg='#333333')
        self.root.title("FF14-BDS")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', background='#555555', foreground='white', borderwidth=1)
        style.map('TButton', background=[('active', '#666666')])

        self.rec_button = ttk.Button(self.root, text="Rec", command=self.start_recording)
        self.rec_button.pack(padx=10, pady=10, fill=tk.X)

        self.root.geometry('300x100')

    def start_recording(self):
        self.selection_app = SelectionApp(self.root)
        self.selection_app.start_selection()

if __name__ == "__main__":
    root = tk.Tk()
    app = DarkThemeApp(root)
    root.mainloop()

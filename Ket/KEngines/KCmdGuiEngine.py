from ..KClasses import *
import colorsys
import math

# Data数据
Data = {
    # EscapeWords格式化文本
    "EscapeWords" : [
        ["&e", "    "]
    ],

    # EscapeColorWords格式化颜色文本
    "EscapeColorWords" : [
        ["$r", "\033[31;40m"],
        ["$g", "\033[32;40m"],
        ["$b", "\033[34;40m"],
        ["$y", "\033[33;40m"],
        ["$p", "\033[35;40m"]
    ]
}

# printe
def printe(text: str | KString, type: str | KString = "COMMON"):
    match type:
        case "COMMON":
            # EscapeWords开始格式化文本
            for code, escapeCode in Data["EscapeWords"]:
                text = text.replace(code, escapeCode)

            # EscapeColorWords开始格式化颜色文本
            for code, escapeCode in Data["EscapeColorWords"]:
                text = text.replace(code, escapeCode) + "\033[0m"

            # 设定颜色范围
            text = text.replace("{", "")
            text = text.replace("}", "\033[0m")

            # 最终输出
            print(text)

        case "COLOURFUL":
                
            result = []
            length = len(text)
            
            for i, char in enumerate(text):
                hue_position = (i / max(1, length - 1)) * 0.8
                
                redHue = (math.sin(hue_position * 2 * math.pi - math.pi/2) + 1) / 2
                greenHue = (math.sin(hue_position * 2 * math.pi + math.pi/3) + 1) / 2  
                blueHue = (math.sin(hue_position * 2 * math.pi + math.pi) + 1) / 2
                
                r, g, b = colorsys.hsv_to_rgb(hue_position, 0.8, 0.8)
                red = int(r * 255)
                green = int(g * 255)
                blue = int(b * 255)
                
                if red == green == blue:
                        grayValue = (red - 8) // 10
                        colorIndex = 232 + grayValue
                else:
                    redIndex = (red + 55) // 51
                    greenIndex = (green + 55) // 51
                    blueIndex = (blue + 55) // 51
                    colorIndex = 16 + 36 * redIndex + 6 * greenIndex + blueIndex
                
                colorCode = f"\033[38;5;{colorIndex}m"
                
                result.append(f"{colorCode}{char}")
            
            result.append("\033[0m")
            text = ''.join(result)
            print(text)

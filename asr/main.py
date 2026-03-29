import os
import speech_recognition as sr

# 语音识别系统
print("=== 语音识别系统 ===")

# 1. 初始化语音识别器
try:
    r = sr.Recognizer()
    print("✓ 语音识别器初始化成功")
    
    # 2. 测试录音功能
    print("\n1. 测试录音功能")
    print("正在启动录音...")
    try:
        with sr.Microphone() as source:
            print("请开始说话（5秒内）...")
            # 调整噪声水平
            r.adjust_for_ambient_noise(source, duration=1)
            print("正在录音...")
            audio_data = r.listen(source, timeout=5)
            print("✓ 录音完成")
            
            # 保存录音到文件
            with open("recorded_audio.wav", "wb") as f:
                f.write(audio_data.get_wav_data())
            print("✓ 录音已保存为 recorded_audio.wav")
            
            # 3. 尝试识别录音内容
            print("\n2. 尝试识别音频")
            print("正在识别...")
            try:
                # 使用Google语音识别
                text = r.recognize_google(audio_data, language="zh-CN")
                print("✓ 识别成功")
                print("识别结果：", text)
            except sr.UnknownValueError:
                print("⚠ 无法识别音频内容")
            except sr.RequestError as e:
                print("⚠ 网络连接错误，无法使用在线识别")
                print("请尝试以下离线方案：")
                print("1. 安装 ffmpeg 命令行工具")
                print("2. 安装 whisper 库: pip install openai-whisper")
                print("3. 运行 whisper 命令: whisper recorded_audio.wav --language zh")
    except Exception as e:
        print(f"⚠ 录音时出错: {e}")
        print("请确保麦克风正常工作")
        
    # 4. 提供离线识别方案
    print("\n3. 离线识别方案")
    print("如果网络连接有问题，可以使用以下离线方案：")
    print("1. 安装 ffmpeg: https://ffmpeg.org/download.html")
    print("2. 安装 whisper: pip install openai-whisper")
    print("3. 运行命令: whisper recorded_audio.wav --language zh")
    print("4. 或使用本地音频文件: whisper audio.wav --language zh")
    
    # 5. 检查现有文件
    print("\n4. 现有文件")
    files = os.listdir('.')
    audio_files = [f for f in files if f.endswith('.wav') or f.endswith('.mp4')]
    if audio_files:
        print("找到的音频/视频文件：")
        for f in audio_files:
            print(f"  - {f}")
    else:
        print("没有找到音频/视频文件")
        
except Exception as e:
    print(f"⚠ 初始化时出错: {e}")
    print("请确保安装了 speechrecognition 库: pip install SpeechRecognition")

print("\n=== 语音识别系统完成 ===")

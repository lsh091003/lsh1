import streamlit as st
#from streamlit_drawable_canvas import st_canvas
from PIL import Image


page = st.sidebar.radio('我的首页', ['我的推荐', '我的图片换色工具', '计算器', '我的字典', '我的留言区'])

def page_1():
    '''我的推荐'''
    st.write('运动')
    st.write('乒乓球')
    st.image("联想截图_20240719191015.png")
    st.write("乒乓球，被称为中国的“国球”，是一种世界流行的球类体育项目，包括‌进攻、对抗和‌防守。该项目起源于‌英国，因其打击时发出“Ping Pong”的声音而得名。在中国内地及港澳地区，该运动被称为乒乓球")
    st.write("足球")
    st.image("1.png")
    st.write('足球是一项以脚为主，控制和支配球，两支球队按照一定规则在同一块长方形球场上互相进行进攻、防守对抗的体育运动项目。因足球运动对抗性强、战术多变、参与人数多等特点，故被称为“世界第一运动')
    st.write('-------------------------------------------')
    st.write('音乐')
    st.write('中文：鸳鸯戏')
    with open("鸳鸯戏(吉他版)-略略略.320.mp3", 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('英文：everyday')
    with open("Every Second-Mina Okabe.128.mp3", 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write('日文：最初的梦')
    with open("2462683254.mp3", 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.write("更多免费音乐资源请点击")
    st.link_button("MyFreeMP3", 'https://tools.liumingye.cn/music/#/google_vignette')
    st.write('-------------------------------------------')
    st.write("电影")
    st.link_button('追龙', 'https://www.bilibili.com/bangumi/play/ss33882?theme=movie&spm_id_from=333.337.0.0')
    st.link_button("沙丘", "https://www.bilibili.com/bangumi/play/ep457765?theme=movie&from_spmid=666.25.episode.0")
    st.link_button("星际穿越", "https://www.bilibili.com/bangumi/play/ep285026?theme=movie&from_spmid=666.7.feed.27")
    st.write("以上点击即可播放")
    st.write("-------------------------------------------")


def page_2():
    '''我的图片换色工具'''
    st.write(":star:图片换色工具:star:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(image_change(img))
def image_change(img):
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            img_array[x, y] = (b, g ,r)
    return img

def page_3():
    st.write(":sunglasses:计算器:sunglasses:")
    with st.form("calc"):
        num_1 = st.number_input("输入第一个数：", value=10)
        num_2 = st.number_input("输入第二个数：", value=10)
        if st.form_submit_button("计算乘积"):
            f"两个数的乘积{num_1*num_2}"
        if st.form_submit_button("计算和"):
            f"两个数的乘积{num_1+num_2}"
        if st.form_submit_button("计算差"):
            f"两个数的乘积{num_1-num_2}"
        if st.form_submit_button("计算商"):
            f"两个数的乘积{num_1/num_2}"

    

def page_4():
    '''我的字典'''
    st.write('智慧词典')
    with open("words_space1.txt", 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
        
    with open("check_out_times.txt", 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1]) 
        
    word = st.text_input("请输入要查询的单词")
    
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt", "w", encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n' 
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋， 这是一行python代码
                    print('上当了吧')''')
            
        
        
def page_5():
    '''我的留言区'''
    st.write("我的留言区")
    with open ('leave_messages.txt', "r", encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == 'up':
            with st.chat_message('😄'):
                st.write(i[1], ':', i[2])
        elif i[1] == '留言者':
            with st.chat_message('⚓'):
                st.write(i[1], ':', i[2])
    name = st.selectbox('我是.....' , ['up', '留言者'])
    new_message = st.text_input('想要说的话.....')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + "#" + i[2] + '\n'
            message = message[:-1]
            f.write(message)

if page == '我的推荐':
    page_1()
elif page == '我的图片换色工具':
    page_2()
elif page == '计算器':
    page_3()
elif page == '我的字典':
    page_4()
elif page == '我的留言区':
    page_5()
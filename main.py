import random
import threading
import time
from init import *


# # 定义超时输入函数
# def timed_input(prompt):
#     # 定义要改变的变量
#     flag = False
#     # 定义计时器函数，5秒后改变变量的值
#     def timer():
#         nonlocal flag
#         #print("计时开始...")
#         time.sleep(5)  # 暂停5秒
#         flag = True  # 5秒后改变变量
#         #print("计时结束，flag 已改变为:", flag)
#         print("\n超时！自动进入下一题...")
#     # 创建并启动计时器线程
#     timer_thread = threading.Thread(target=timer)
#     timer_thread.start()
#     answer = input(prompt)
#     if flag:
#         return "p"
#     else:
#         if answer == "q":
#             return "q"
#         else:
#             return answer


# 五行相生测试
def wu_xing_sheng_test():
    wu_xing = random.choice(wu_xing_list).name
    question_type = random.choice(["sheng", "beisheng"])
    if question_type == "sheng":
        correct_answer = wu_xing_sheng_map[wu_xing]
        user_answer_pinyin = input(f"\n五行相生测试：{wu_xing} 生 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = wu_xing_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{wu_xing} 生 {correct_answer}")
            return 1
        else:
            print(f"回答错误！正确答案是：{wu_xing} 生 {correct_answer}")
            return 0
    else:
        correct_answer = wu_xing_beisheng_map[wu_xing]
        user_answer_pinyin = input(f"\n五行相生测试：{wu_xing} 被什么所生 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = wu_xing_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{wu_xing} 被 {correct_answer} 所生")
            return 1
        else:
            print(f"回答错误！正确答案是：{wu_xing} 被 {correct_answer} 所生")
            return 0


# 五行相克测试
def wu_xing_ke_test():
    wu_xing = random.choice(wu_xing_list).name
    question_type = random.choice(["ke", "beike"])
    if question_type == "ke":
        correct_answer = wu_xing_ke_map[wu_xing]
        user_answer_pinyin = input(f"\n五行相克测试：{wu_xing} 克 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = wu_xing_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{wu_xing} 克 {correct_answer}")
            return 1
        else:
            print(f"回答错误！正确答案是：{wu_xing} 克 {correct_answer}")
            return 0
    else:
        correct_answer = wu_xing_beike_map[wu_xing]
        user_answer_pinyin = input(f"\n五行相克测试：{wu_xing} 被什么所克 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = wu_xing_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{wu_xing} 被 {correct_answer} 所克")
            return 1
        else:
            print(f"回答错误！正确答案是：{wu_xing} 被 {correct_answer} 所克")
            return 0


# 天干相合测试
def tian_gan_he_test():
    tian_gan = random.choice(tian_gan_list).name
    correct_answer = tian_gan_he_map[tian_gan]
    user_answer_pinyin = input(f"\n天干相合测试：{tian_gan} 合 ")
    if user_answer_pinyin == "q":
        return "q"
    user_answer = tian_gan_pinyin_to_zi_map.get(user_answer_pinyin)
    if user_answer == correct_answer:
        print(f"回答正确！{tian_gan} 合 {correct_answer}")
        return 1
    else:
        print(f"回答错误！正确答案是：{tian_gan} 合 {correct_answer}")
        return 0


# 地支相冲测试
def di_zhi_chong_test():
    di_zhi = random.choice(di_zhi_list).name
    correct_answer = di_zhi_chong_map[di_zhi]
    user_answer_pinyin = input(f"\n地支相冲测试：{di_zhi} 冲 ")
    if user_answer_pinyin == "q":
        return "q"
    user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
    if user_answer == correct_answer:
        print(f"回答正确！{di_zhi} 冲 {correct_answer}")
        return 1
    else:
        print(f"回答错误！正确答案是：{di_zhi} 冲 {correct_answer}")
        return 0


# 地支相合测试
def di_zhi_he_test():
    di_zhi = random.choice(di_zhi_list).name
    correct_answer = di_zhi_he_map[di_zhi]
    user_answer_pinyin = input(f"\n地支相合测试：{di_zhi} 合 ")
    if user_answer_pinyin == "q":
        return "q"
    user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
    if user_answer == correct_answer:
        print(f"回答正确！{di_zhi} 合 {correct_answer}")
        return 1
    else:
        print(f"回答错误！正确答案是：{di_zhi} 合 {correct_answer}")
        return 0


# 地支相害测试
def di_zhi_hai_test():
    di_zhi = random.choice(di_zhi_list).name
    correct_answer = di_zhi_hai_map[di_zhi]
    user_answer_pinyin = input(f"\n地支相害测试：{di_zhi} 害 ")
    if user_answer_pinyin == "q":
        return "q"
    user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
    if user_answer == correct_answer:
        print(f"回答正确！{di_zhi} 害 {correct_answer}")
        return 1
    else:
        print(f"回答错误！正确答案是：{di_zhi} 害 {correct_answer}")
        return 0


# 地支相破测试
def di_zhi_po_test():
    di_zhi = random.choice(di_zhi_list).name
    correct_answer = di_zhi_po_map[di_zhi]
    user_answer_pinyin = input(f"\n地支相破测试：{di_zhi} 破 ")
    if user_answer_pinyin == "q":
        return "q"
    user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
    if user_answer == correct_answer:
        print(f"回答正确！{di_zhi} 破 {correct_answer}")
        return 1
    else:
        print(f"回答错误！正确答案是：{di_zhi} 破 {correct_answer}")
        return 0


# 地支相刑测试
def di_zhi_xing_test():
    di_zhi = random.choice(di_zhi_list).name
    question_type = random.choice(["xing", "beixing"])
    if question_type == "xing":
        correct_answer = di_zhi_xing_map[di_zhi]
        user_answer_pinyin = input(f"\n地支相刑测试：{di_zhi} 刑 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{di_zhi} 刑 {correct_answer}")
            return 1
        else:
            print(f"回答错误！正确答案是：{di_zhi} 刑 {correct_answer}")
            return 0
    else:
        correct_answer = di_zhi_beixing_map[di_zhi]
        user_answer_pinyin = input(f"\n地支相刑测试：{di_zhi} 被什么所刑 ")
        if user_answer_pinyin == "q":
            return "q"
        user_answer = di_zhi_pinyin_to_zi_map.get(user_answer_pinyin)
        if user_answer == correct_answer:
            print(f"回答正确！{di_zhi} 被 {correct_answer} 所刑")
            return 1
        else:
            print(f"回答错误！正确答案是：{di_zhi} 被 {correct_answer} 所刑")
            return 0


# 地支三合局测试
def di_zhi_sanhe_test():
    question_type = random.choice(["he", "beihe"])
    if question_type == "he":
        question = random.choice(di_zhi_list).name
    else:
        question = random.choice(wu_xing_list).name
        while question == "土":
            question = random.choice(wu_xing_list).name
    correct_answer = di_zhi_sanhe_map[question]
    correct_answer_pinyin = di_zhi_zi_to_pinyin_map.get(correct_answer[1]) + di_zhi_zi_to_pinyin_map.get(correct_answer[2]) + di_zhi_zi_to_pinyin_map.get(correct_answer[3]) + " " + wu_xing_zi_to_pinyin_map.get(correct_answer[0])
    user_answer_pinyin = input(f"\n地支三合局测试：{question} 的三合局是 ")
    if user_answer_pinyin == "q":
        return "q"
    if user_answer_pinyin == correct_answer_pinyin:
        print(f"回答正确！{correct_answer[1]}{correct_answer[2]}{correct_answer[3]}合{correct_answer[0]}局")
        return 1
    else:
        print(f"回答错误！正确答案是：{correct_answer[1]}{correct_answer[2]}{correct_answer[3]}合{correct_answer[0]}局")
        return 0


# 随机测试
def random_test():
    functions = [wu_xing_sheng_test, wu_xing_ke_test, tian_gan_he_test, di_zhi_chong_test, di_zhi_he_test,
                 di_zhi_hai_test, di_zhi_po_test, di_zhi_xing_test, di_zhi_sanhe_test]
    re = random.choice(functions)()
    if re == "q":
        return "q"
    elif re == 1:
        return 1
    elif re == 0:
        return 0

# 主程序逻辑
def main():
    while True:
        print("\n请选择测试类型：")
        print("q. 退出程序")
        print("0. 随机测试")
        print("1. 五行相生测试")
        print("2. 五行相克测试")
        print("3. 天干相合测试")
        print("4. 地支相冲测试")
        print("5. 地支相合测试")
        print("6. 地支相害测试")
        print("7. 地支相破测试")
        print("8. 地支相刑测试")
        print("9. 地支三合局测试")
        choice = input("请输入测试类型：")
        if choice == 'q':
            break
        elif choice == '0':
            # 将所有函数添加到列表中
            loop_test(random_test)
        elif choice == '1':
            loop_test(wu_xing_sheng_test)
        elif choice == '2':
            loop_test(wu_xing_ke_test)
        elif choice == '3':
            loop_test(tian_gan_he_test)
        elif choice == '4':
            loop_test(di_zhi_chong_test)
        elif choice == '5':
            loop_test(di_zhi_he_test)
        elif choice == '6':
            loop_test(di_zhi_hai_test)
        elif choice == '7':
            loop_test(di_zhi_po_test)
        elif choice == '8':
            loop_test(di_zhi_xing_test)
        elif choice == '9':
            loop_test(di_zhi_sanhe_test)
        else:
            print("\n无效的选择，请重新选择！")


# 循环测试的通用逻辑
def loop_test(test_function):
    print("输入 'q' 退出当前测试")
    total, correct = 0, 0
    while True:
        re = test_function()  # 调用具体的测试函数
        total +=1
        if re == "q":
            total -= 1
            break
        elif re == 1:
            correct += 1
    if total > 0:
        accuracy = round((correct / total), 4) * 100
        print(f"\n总共{total}题，答对{correct}题，正确率{accuracy}%")
    else:
        print("\n没有完成任何题目。")


if __name__ == "__main__":
    main()
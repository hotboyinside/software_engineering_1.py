import tkinter as tk
from tkinter import font
from typing import List

# parameters
WIDTH = 800
HEIGHT = 600

projects_parametrs = {
    "Распостраненный": {'a': 2.4, 'b': 1.05, 'c': 2.5, 'd': 0.38},
    "Полунезависимый": {'a': 3.0, 'b': 1.12, 'c': 2.5, 'd': 0.35},
    "Встроенный": {'a': 3.6, 'b': 1.2, 'c': 2.5, 'd': 0.32}
}


if __name__ == "__main__":

    # settings root
    root = tk.Tk()
    root.title("COCOMO Basic")
    root.geometry("800x600")

    # set font
    font_desc = tk.font.Font(root, family="Inter", size=10, weight="normal")
    font_button = tk.font.Font(root, family="Inter", size=12, weight="normal")
    font_title = tk.font.Font(root, family="Inter", size=12, weight="bold")

    # set canvas
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
    canvas.pack()

    # set frame
    frame = tk.Frame(root, bg='#FDFDFD')
    frame.place(relwidth=0.67, relheight=1)

    # set label1
    label1 = tk.Label(
        frame,
        text="Модель этого уровня - двупараметрическая. В качестве параметров выступает тип\n"
             "проекта и объем программы (число строк кода). Модель этого уровня подходит\n"
             "для ранней быстрой оценки затрат, но точность ее весьма низка, так как\n"
             "не учитываются такие факторы, как квалификация персонала, характеристики\n"
             "оборудования, опыт применения современных методов разработки программного\n"
             "обеспечения и современных инструментальных сред разработки и другое.",
        justify="left",
        background='#FDFDFD',
        font=font_desc,
    )
    label1.place(relx=0.03, rely=0.11, relheight=0.16)

    # set container
    container = tk.Label(
        frame,
        background="#FDFDFD",
        highlightthickness=2,
        highlightbackground='#D0D7EA'
    )
    container.place(relx=0.03, rely=0.30, relwidth=0.97, relheight=0.5)

    # set label2
    label2 = tk.Label(
        frame,
        text="Параметры базового уровня",
        justify="left",
        background='#FDFDFD',
        font=font_title
    )
    label2.place(relx=0.06, rely=0.32, relheight=0.03)

    # set label3
    label3 = tk.Label(
        frame,
        text="Тип проекта:",
        justify="left",
        background='#FDFDFD',
        font=font_desc,
    )
    label3.place(relx=0.06, rely=0.39, relheight=0.03)

    def get_desc_method(*args):

        method = str(variables.get())

        if method == "Встроенный":
            new_label = tk.Label(
                frame,
                text="Встроенный тип характеризуется очень\n"
                     "жесткими требованиями на программный\n"
                     "продукт, интерфейсы, параметры ЭВМ.\n"
                     "Как правило,у таких изделий высокая\n"
                     "степень новизны и планирование работ\n"
                     "осуществляется при недостаточной\n"
                     "информации,как о самом изделии,\n"
                     "так и об условиях работы. Встроенный\n"
                     "проект требует больших затрат\n"
                     "на изменения и исправления.",
                justify="left",
                background='#FDFDFD',
                font=font_desc,
            )
        elif method == "Распостраненный":
            new_label = tk.Label(
                frame,
                text="Распространенный тип характеризуется\n"
                     "тем, что проект выполняется небольшой\n"
                     "группой специалистов, имеющих опыт\n"
                     "в создании подобных изделий и опыт\n"
                     "применения технологических средств.\n"
                     "Условия  работы стабильны, и изделие\n"
                     "имеет относительно невысокую сложность.",
                justify="left",
                background='#FDFDFD',
                font=font_desc,
            )
        else:
            new_label = tk.Label(
                frame,
                text="Полунезависимый тип занимает\n"
                     "промежуточное положение между\n"
                     "распространенным и встроенным\n"
                     "– это проекты средней сложности.\n"
                     "Исполнители знакомы лишь с некоторыми\n"
                     "характеристиками (или компонентами)\n"
                     "создаваемой системы, имеют средний\n"
                     "опыт работы с подобными изделиями,\n"
                     "изделие имеет элемент новизны.\n"
                     "Только часть требований к изделию\n"
                     "жестко фиксируется, в остальном\n"
                     "разработки имеют степени выбора.",
                justify="left",
                background='#FDFDFD',
                font=font_desc,
            )

        new_label.place(relx=0.47, rely=0.39, relheight=0.33, relwidth=0.5)

    # set option menu
    OPTIONS = ["Встроенный", "Распостраненный", "Полунезависимый"]
    variables = tk.StringVar(frame)
    variables.set(OPTIONS[0])
    variables.trace('w', get_desc_method)
    option_menu = tk.OptionMenu(frame, variables, *OPTIONS)
    option_menu.place(relx=0.06, rely=0.44, relheight=0.04)

    # set label4
    label4 = tk.Label(
        frame,
        text="Объем программного продукта\n(количество строк кода, тыс):",
        justify="left",
        background='#FDFDFD',
        font=font_desc,
    )
    label4.place(relx=0.06, rely=0.51, relheight=0.06)

    # set entry
    default_value = tk.StringVar(frame, value='1')
    entry = tk.Entry(
        frame,
        textvariable=default_value
    )
    entry.place(relx=0.06, rely=0.59, relheight=0.04)

    # set label5
    label5 = tk.Label(
        frame,
        text="Встроенный тип характеризуется очень\n"
             "жесткими требованиями на программный\n"
             "продукт, интерфейсы, параметры ЭВМ.\n"
             "Как правило,у таких изделий высокая\n"
             "степень новизны и планирование работ\n"
             "осуществляется при недостаточной\n"
             "информации,как о самом изделии,\n"
             "так и об условиях работы. Встроенный\n"
             "проект требует больших затрат\n"
             "на изменения и исправления.",
        justify="left",
        background='#FDFDFD',
        font=font_desc,
    )
    label5.place(relx=0.47, rely=0.39, relheight=0.27)


    def get_value_project(user_size, user_type):
        project_type = str(user_type.get())
        project_size = float(user_size.get())

        if project_type == 'Распостраненный':
            data = projects_parametrs.get('Распостраненный')

        elif project_type == "Полунезависимый":
            data = projects_parametrs.get('Полунезависимый')

        else:
            data = projects_parametrs.get('Встроенный')

        answer1 = data['a'] * project_size ** data['b']
        answer2 = data['c'] * answer1 ** data['d']

        # set label-answer1
        label_answer1 = tk.Label(
            frame2,
            text=str(round(answer1, 2)),
            justify="left",
            background='#FDFDFD',
            font=font_title
        )
        label_answer1.place(relx=0.09, rely=0.44, relheight=0.04)

        # set label-answer2
        label_answer2 = tk.Label(
            frame2,
            text=str(round(answer2, 2)),
            justify="left",
            background='#FDFDFD',
            font=font_title
        )
        label_answer2.place(relx=0.09, rely=0.59, relheight=0.04)

    # set button
    button = tk.Button(
        frame,
        text="Рассчитать",
        font=font_button,
        padx=20, pady=5,
        bg="#C1CEEE",
        command=lambda: get_value_project(entry, variables)

    )
    button.place(relx=0.06, rely=0.69)

    # set frame2
    frame2 = tk.Frame(root, bg='#FDFDFD')
    frame2.place(relx=0.67, relwidth=0.33, relheight=1)

    # set container 2
    container2 = tk.Label(
        frame2,
        background="#FDFDFD",
        highlightthickness=2,
        highlightbackground='#D0D7EA'
    )
    container2.place(relx=0.03, rely=0.30, relwidth=0.915, relheight=0.5)

    # set label2.1
    label2_1: tk.Label = tk.Label(
        frame2,
        text="Результат",
        justify="left",
        background='#FDFDFD',
        font=font_title
    )
    label2_1.place(relx=0.09, rely=0.32, relheight=0.03)

    # set label2.2
    label2_2 = tk.Label(
        frame2,
        text="Трудоемкость (чел. * мес.) :",
        justify="left",
        background='#FDFDFD',
        font=font_desc
    )
    label2_2.place(relx=0.09, rely=0.39, relheight=0.03)

    # set label3.2
    label2_2 = tk.Label(
        frame2,
        text="Время разработки,\nмесяцы:",
        justify="left",
        background='#FDFDFD',
        font=font_desc
    )
    label2_2.place(relx=0.09, rely=0.51, relheight=0.06)

    def clear_fields():
        # set label-answer1

        label_answer1 = tk.Label(
            frame2,
            background='#FDFDFD',
        )
        label_answer1.place(relx=0.09, rely=0.44, relheight=0.04, relwidth=0.2)

        # set label-answer2
        label_answer2 = tk.Label(
            frame2,
            background='#FDFDFD',
        )
        label_answer2.place(relx=0.09, rely=0.59, relheight=0.04, relwidth=0.2)

    # set button2
    button = tk.Button(
        frame2,
        text="Очистить",
        font=font_button,
        padx=20, pady=5,
        bg="#C1CEEE",
        command=lambda: clear_fields()
    )
    button.place(relx=0.09, rely=0.69)

    root.mainloop()

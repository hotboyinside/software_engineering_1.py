from tkinter import Tk, Frame, Label, Entry, Button, messagebox
from typing import List


storage = dict()
storage_with_workers_hours = dict()


def get_data_and_second_action(inpt: Entry, window: Tk) -> None:
    try:
        storage["count"] = int(inpt.get())
    except (TypeError, ValueError):
        messagebox.showinfo(title='', message='Ввод должен осуществляться цифрами')
    print(storage)
    window.destroy()


def create_frame_for_1_action(window: Tk) -> None:

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    label_counter = Label(
        frame,
        text="Введите количество рассматриваемых показателей"
    )
    label_counter.grid(column=1, row=3)

    input_counter = Entry(
        frame,
    )
    input_counter.grid(column=2, row=3, padx=10)

    button_enter = Button(
        frame,
        text="Продолжить",
        command=lambda: get_data_and_second_action(input_counter, window),

    )
    button_enter.grid(column=2, row=4, pady=10)


def create_window() -> Tk:
    window = Tk()
    window.title("Расчет показателя качества балльно-индексным методом")
    window.geometry("800x600")
    return window


def action1() -> None:
    wnd = create_window()
    create_frame_for_1_action(wnd)
    wnd.mainloop()


def get_data_from_action2(constants: List, marks_1: List, marks_2: List, window: Tk) -> None:
    summa_1: int = 0
    summa_2: int = 0
    for index, value, in enumerate(constants):
        summa_1 += float(value.get()) * float(marks_1[index].get())
        summa_2 += float(value.get()) * float(marks_2[index].get())

    diff = summa_1 / summa_2
    if diff <= 1:
        messagebox.showinfo(
            title='Результат',
            message=f'{summa_1} / {summa_2} = {diff}\nРазработка проекта с технической точки зрения не оправдана'
        )
    else:
        messagebox.showinfo(
            title='Результат',
            message=f'{summa_1} / {summa_2} = {diff}\nРазработка проекта с технической точки зрения оправдана')
    window.destroy()


def create_frame_for_2_action(window: Tk) -> None:
    counter = 2
    kef_lists = []
    projects_marks = []
    analogs_marks = []

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    for index in range(storage["count"]):

        # коэффициенты весомости
        label_kef = Label(
            frame,
            text=f"Коэффициент \nвесомости B{index+1}"
        )
        label_kef.grid(column=1, row=index)

        input_kef = Entry(
            frame,
        )
        input_kef.grid(column=2, row=index, padx=10)
        kef_lists.append(input_kef)

        # экспертная оценка для проекта
        label_value_for_project = Label(
            frame,
            text=f"Экспертная оценка \nдля проекта {index + 1}"
        )
        label_value_for_project.grid(column=1 + counter, row=index)

        input_value_for_project = Entry(
            frame,
        )
        input_value_for_project.grid(column=2 + counter, row=index, padx=10)
        projects_marks.append(input_value_for_project)

        # экспертная оценка для аналога
        label_value_for_analog = Label(
            frame,
            text=f"Экспертная оценка \nдля аналога {index + 1}"
        )
        label_value_for_analog.grid(column=1 + counter * 2, row=index)

        input_value_for_analog = Entry(
            frame,
        )
        input_value_for_analog.grid(column=2 + counter * 2, row=index, padx=10)
        analogs_marks.append(input_value_for_analog)

    button_enter = Button(
        frame,
        text="Продолжить",
        command=lambda: get_data_from_action2(kef_lists, projects_marks, analogs_marks, window),
    )
    button_enter.grid(column=6, row=storage["count"], pady=10)


def action2() -> None:
    wnd = create_window()
    create_frame_for_2_action(wnd)
    wnd.mainloop()


def get_data_from_action3(inpt1: Entry, inpt2: Entry, window: Tk) -> None:

    storage["count_stages"] = int(inpt1.get())
    storage["count_workers"] = int(inpt2.get())
    print(storage)
    window.destroy()


def create_frame_for_3_action(window: Tk) -> None:

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    label_counter1 = Label(
        frame,
        text="Введите количество этапов работы"
    )
    label_counter1.grid(column=1, row=3)

    input_counter1 = Entry(
        frame,
    )
    input_counter1.grid(column=2, row=3, padx=10)

    label_counter2 = Label(
        frame,
        text="Введите количество исполнителей"
    )
    label_counter2.grid(column=1, row=4)

    input_counter2 = Entry(
        frame,
    )
    input_counter2.grid(column=2, row=4, padx=10)

    button_enter = Button(
        frame,
        text="Продолжить",
        command=lambda: get_data_from_action3(input_counter1, input_counter2, window),
    )
    button_enter.grid(column=2, row=5, pady=10)


def action3() -> None:
    wnd = create_window()
    create_frame_for_3_action(wnd)
    wnd.mainloop()


def get_data_from_action4(workers_items: List, window: Tk) -> None:
    storage["workers"] = []

    for worker in workers_items:
        storage["workers"].append(str(worker.get()))

    print(storage)
    window.destroy()


def create_frame_for_4_action(window: Tk) -> None:

    workers = []

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    for worker in range(storage["count_workers"]):

        label_counter = Label(
            frame,
            text="Введите должность"
        )
        label_counter.grid(column=1, row=worker)

        input_counter = Entry(
            frame,
        )
        input_counter.grid(column=2, row=worker, padx=10)

        workers.append(input_counter)

        button_enter = Button(
            frame,
            text="Продолжить",
            command=lambda: get_data_from_action4(workers, window),
        )
        button_enter.grid(column=2, row=5, pady=10)


def action4() -> None:
    wnd = create_window()
    create_frame_for_4_action(wnd)
    wnd.mainloop()


def get_data_from_action5(stages_items: List, window: Tk) -> None:
    storage["stages"] = []

    for worker in stages_items:
        storage["stages"].append(str(worker.get()))

    print(storage)
    window.destroy()


def create_frame_for_5_action(window: Tk) -> None:
    stages: List = []

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    for num_stage in range(storage["count_stages"]):

        label_counter = Label(
            frame,
            text=f"Введите название {num_stage + 1} этапа"
        )
        label_counter.grid(column=1, row=num_stage)

        input_counter = Entry(
            frame,
        )
        input_counter.grid(column=2, row=num_stage, padx=10)
        stages.append(input_counter)

        button_enter = Button(
            frame,
            text="Продолжить",
            command=lambda: get_data_from_action5(stages, window),
        )
        button_enter.grid(column=2, row=5, pady=10)


def action5() -> None:
    wnd = create_window()
    create_frame_for_5_action(wnd)
    wnd.mainloop()


def get_data_from_action6(worker: str, duration: List, worker_hours: List, window: Tk) -> None:
    storage_with_workers_hours[worker]: List = []

    if "duration" not in storage.keys():
        storage["duration"] = []
        for period in duration:
            storage["duration"].append(int(period.get()))

    print(storage["duration"])

    for hours in worker_hours:
        storage_with_workers_hours[worker].append(int(hours.get()))

    print(storage_with_workers_hours)

    if len(storage_with_workers_hours) == storage["count_workers"]:

        for index, stage in enumerate(storage["stages"]):
            some_text = f'На этапе {stage}, который длится {storage["duration"][index]} дней.\n'
            for worker in storage["workers"]:
                some_text += f'Загрузка {worker}а составит {storage_with_workers_hours[worker][index] / storage["duration"][index] * 100}%\n'

            messagebox.showinfo(title='Рузультат', message=some_text)

        for worker, hours in storage_with_workers_hours.items():
            amount_hours: int = sum(hours)
            storage_with_workers_hours[worker] = amount_hours
            messagebox.showinfo(title='', message=f'Всего {worker} должен будет отработать {amount_hours} дней(дня)')

    window.destroy()


def create_frame_for_6_action() -> None:

    input_destinations: List = []
    for worker in storage["workers"]:

        if worker in storage.keys():
            continue
        else:

            window = create_window()

            frame = Frame(
                window,
                padx=20,
                pady=20,
            )
            frame.pack(expand=True)

            input_workers_hours = []

            for index, stage in enumerate(storage["stages"]):
                # поля для ввода длительности этапов

                if "duration" not in storage.keys():
                    label_counter = Label(
                        frame,
                        text=f"Введите длительность\n этапа '{stage}'(в днях)"
                    )
                    label_counter.grid(column=1, row=index + 1)

                    input_duration = Entry(
                        frame,
                    )
                    input_duration.grid(column=2, row=index + 1, padx=10)
                    input_destinations.append(input_duration)

                # поля для ввода загрузки работника
                else:
                    label_counter = Label(
                        frame,
                        text=f"Длительность этапа '{stage}'\nравна {storage['duration'][index]}"
                    )
                    label_counter.grid(column=1, row=index + 1)

                label_counter = Label(
                    frame,
                    text=f"Введите\n загруженность {worker}а  на\n этапе '{stage}'(в днях)"
                )
                label_counter.grid(column=3, row=index + 1)

                input_timework = Entry(
                    frame,
                )
                input_timework.grid(column=4, row=index + 1, padx=10)
                input_workers_hours.append(input_timework)

            button_enter = Button(
                frame,
                text="Продолжить",
                command=lambda: get_data_from_action6(worker, input_destinations, input_workers_hours, window),
            )
            button_enter.grid(column=4, row=storage["count_stages"] + 1, pady=10)
            window.mainloop()


def action6() -> None:
    create_frame_for_6_action()


def get_data_from_action7(workers_salary: List, window: Tk) -> None:
    storage["salaries"] = []
    storage["expenses"] = 0
    counter: int = 0

    for item in workers_salary:
        salary = int(item.get())
        storage["salaries"].append(salary)

    for worker, work_days in storage_with_workers_hours.items():
        salary_for_project: float = storage["salaries"][counter] / 21 * work_days
        storage["expenses"] += salary_for_project
        counter += 1

        messagebox.showinfo(title='', message=f'Заработная плата {worker}а составит {salary_for_project}')

    window.destroy()


def create_frame_for_7_action(window: Tk) -> None:
    salaries: List = []

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    for index, worker in enumerate(storage['workers']):

        label_salary = Label(
            frame,
            text=f"Введите оклад должности '{worker}'"
        )
        label_salary.grid(column=1, row=index + 1)

        input_salary = Entry(
            frame,
        )
        input_salary.grid(column=2, row=index + 1, padx=10)
        salaries.append(input_salary)

    button_enter = Button(
        frame,
        text="Продолжить",
        command=lambda: get_data_from_action7(salaries, window),
    )
    button_enter.grid(column=2, row=len(storage_with_workers_hours) + 1, pady=10)


def action7() -> None:
    wnd = create_window()
    create_frame_for_7_action(wnd)
    wnd.mainloop()


def get_data_from_action8(inpt: Entry, window:  Tk) -> None:
    storage["counter_expenses"] = int(inpt.get())
    window.destroy()


def create_frame_for_8_action(window: Tk) -> None:
    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)
    label_count = Label(
        frame,
        text=f"Введите количество статей\nдополнительных расходов'"
    )
    label_count.grid(column=1, row=1)

    input_count = Entry(
        frame,
    )
    input_count.grid(column=2, row=1, padx=10)

    button_enter = Button(
        frame,
        text="Продолжить",
        command=lambda: get_data_from_action8(input_count, window),
    )
    button_enter.grid(column=2, row=2, pady=10)


def action8() -> None:
    wnd = create_window()
    create_frame_for_8_action(wnd)
    wnd.mainloop()


def get_data_from_action9(articles: List, window: Tk) -> None:
    for item in articles:
        storage["expenses"] += int(item.get())

    messagebox.showinfo(
        title='', message=f"Учитывая заработную плату работников, а также\n дополнительные статьи расходов, на проект\n было затрачено {storage['expenses']}"
    )
    window.destroy()


def create_frame_for_9_action(window: Tk) -> None:
    articles: List = []

    frame = Frame(
        window,
        padx=20,
        pady=20,
    )
    frame.pack(expand=True)

    for num_article in range(storage["counter_expenses"]):

        label_amount = Label(
            frame,
            text=f"Введите сумму, которая была затрачена в статье расходов номер {num_article+1}"
        )
        label_amount.grid(column=1, row=num_article+1)

        input_amount = Entry(
            frame,
        )
        input_amount.grid(column=2, row=num_article+1, padx=10)
        articles.append(input_amount)

        button_enter = Button(
            frame,
            text="Продолжить",
            command=lambda: get_data_from_action9(articles, window),
        )
        button_enter.grid(column=2, row=storage["counter_expenses"]+1, pady=10)


def action9() -> None:
    wnd = create_window()
    create_frame_for_9_action(wnd)
    wnd.mainloop()


if __name__ == "__main__":
    action1()
    action2()
    action3()
    action4()
    action5()
    action6()
    action7()
    action8()
    action9()

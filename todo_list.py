from datetime import datetime, time


def create_task(name, due_date, required_time):
    return dict(name=name, due_date=due_date, required_time=required_time, finished=False)


def format_task(task):
    state = 'Done' if task['finished'] else 'Undone'
    format = "{state} {task[name]}:{task[due_date]:%Y-%m-%d} まで予定時間 {task[required_time]}分"
    return format.format(task=task, state=state)


def finish_task(task):
    task['finished'] = True


t = create_task('Task', datetime(2012, 4, 1), time(0, 25))
finish_task(t)
print(t['finished'])

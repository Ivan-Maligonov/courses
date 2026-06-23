import psutil


def checkIfProcessRunning(processName):
    """
    Проверяет, запущен ли процесс с указанным именем.
    """
    # Перебираем все запущенные процессы
    for proc in psutil.process_iter():
        try:
            # Проверяем, содержит ли имя процесса указанную строку
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return False


# Проверяем, запущен ли Docker
if checkIfProcessRunning("dockerd"):
    print("Yes, a Docker process is running.")
else:
    print("No Docker process is running.")
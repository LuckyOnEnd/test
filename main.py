import os

# Список системных директорий, которые будем пропускать
EXCLUDED_DIRS = {
    "C:\\Windows", "C:\\Program Files", "C:\\Program Files (x86)", "C:\\System Volume Information",
    "/proc", "/sys", "/dev", "/run", "/var/lib", "/var/run", "/snap"
}

# Расширения файлов, которые нужно пропустить
EXCLUDED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".dll", ".cs", ".css", ".xml", ".html", ".pdf", ".js", ".cache", ".svg", ".ts", ".json", ".asar", ".h", ".editorconfig", ".ico", ".class"}

def list_all_files_and_folders(start_path="/"):
    for root, dirs, files in os.walk(start_path, topdown=True):
        # Исключаем системные директории
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in EXCLUDED_DIRS and not d.startswith('.')]

        for dir_name in dirs:
            print(os.path.join(root, dir_name))

        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_ext = os.path.splitext(file_name)[1].lower()  # Получаем расширение

            # Пропускаем скрытые файлы, файлы без расширения и файлы с исключенными расширениями
            if not file_name.startswith('.') and file_ext and file_ext not in EXCLUDED_EXTENSIONS:
                print(file_path)

if __name__ == "__main__":
    start_path = "C:\\" if os.name == "nt" else "/"  # Windows → C:\, Linux/Mac → /
    list_all_files_and_folders(start_path)

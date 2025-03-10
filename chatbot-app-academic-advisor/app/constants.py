CORPUS_SOURCES = ["https://www.csusb.edu/cse","https://catalog.csusb.edu/colleges-schools-departments/natural-sciences/computer-science-engineering/"]

ALLOWED_CSE_NAVIGATION_SECTIONS = [
    "Welcome",
    "Programs",
    "Faculty and Staff",
    "Advising",
    "Resources",
    "Internships & Careers",
    "Computer Labs & Support",
    "Faculty in the News",
    "Contact Us",
]

# Define exclusions
EXCLUDED_TEXTS = ["Give to CNS"]  # Keywords to exclude
EXCLUDED_URLS = ["https://www.csusb.edu/give-cns"]  # Specific URLs to exclude

ALLOWED_CATALOG_NAVIGATION_SECTIONS = ["Overview", "Faculty", "Undergraduate Degrees", "Graduate Degree", "Minor", "Certificates", "Courses"]


# os.makedirs("milvus_lite", exist_ok=True)
MILVUS_URI = "milvus_vector.db"

# Logging errors
# Debugging - can be removed in production
import os
print("Current working directory:", os.getcwd())
# List all files (and directories) in the current working directory
for entry in os.listdir(os.getcwd()):
    full_path = os.path.join(os.getcwd(), entry)
    if os.path.isfile(full_path):  # Only print files, not directories
        print(full_path)
# Define the path to the Excel files
xls_files = ["/app/app/Faculty Times.xlsx", 
             "/app/app/Final_Faculty_Data_with_Proper_Capitalization.xlsx",
               "/app/app/Syllabus'.xlsx"]  # Add more Excel files here
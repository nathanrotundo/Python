def main(): # code to organize files into newly created directories based on their file types
    try:
        import os
        os.mkdir('MyFiles')
        os.mkdir('MyFiles/Docs')
        os.mkdir('MyFiles/images')
        os.mkdir('MyFiles/videos')
    except FileExistsError:
        print("Directory already exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

main()
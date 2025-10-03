import pandas as pd
import os
while True:
    main_file = input("Enter the file Path ")
    main_file = main_file.replace("\\", "\\\\")
    File_name = os.path.basename(main_file)
    check_file = input("enter the file to check ")
    check_file = check_file.replace("\\","\\\\")

    df = pd.read_excel(main_file)
    print("main_File loaded Succesfully")
    df_check = pd.read_excel(check_file)
    print("dowanloded file loaded successfuly")

    df.drop_duplicates(inplace=True)
    df_check.drop_duplicates(inplace=True)
    print(f"Total items in main_file is {df.shape}")
    print(f"Total items in dwn file are{df.shape}")

    df_anti = df[~df['Product Name'].isin(df_check["Product Name"])]

    df_anti.drop_duplicates(inplace=True)
    print(f"total remaining items are {df_anti.shape}")

    df_anti.to_excel(f"c:\\Users\\MICILMEDS\\Documents\\Medi_final\\correct_data\\Category\\Remaining data\\{File_name}.xlsx")
    x = input("Enter Exit of Exit for Contine enter any key")
    x = x.lower().strip()
    if x=="exit":
        break
    

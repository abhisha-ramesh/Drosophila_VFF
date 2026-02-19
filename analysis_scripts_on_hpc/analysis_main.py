import os
import numpy as np

def generate_script_files():
    """
    This function loads the furrow depth data from multiple simulation runs for different parameter combinations of peripheral and central stiffness,
    computes the average furrow depth for each combination of lambda_cent and lambda_peri, and saves the averaged data to new files for each parameter.
    """

    # Define the parameter lists for lambda_peri and lambda_cent (change these lists based on specific parameter values)
    peri_list = [0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
    cent_list = [30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]

    for lambda_peri in range(len(peri_list)):
        for lambda_cent in range(len(cent_list)):
            # Define the folder pattern
            folder_pattern = "/share/belmonte/athayam/CC3DWorkSpace/Gastrulation_simplified__2024_Aug_28__10_32_21/__lambda_cent_{}__lambda_peri_{}/".format(cent_list[lambda_cent],peri_list[lambda_peri])

            n_files = 0
            furrow_depth_sum = np.zeros(2600)       # Initialize an array to accumulate furrow depth values (assuming 2600 total time points based on the original code)
            
            # List sub-folders (0001 to 0030), ensemble runs for each parameter combination
            for sub_folder_name in range(1, 31):    
                sub_folder_name = "{0:04d}".format(sub_folder_name)
                sub_folder_path = os.path.join(folder_pattern, sub_folder_name)
                furrow_depth_file = os.path.join(sub_folder_path, "furrow_depth_data.txt")
                
                if os.path.exists(furrow_depth_file):
                    n_files += 1
                    # Check the number of rows in the file
                    num_rows = sum(1 for line in open(furrow_depth_file))
                    if num_rows == 2600:
                        # Compute average furrow depth
                        time, depth = np.loadtxt(furrow_depth_file, unpack=True)
                        furrow_depth_sum += depth

            if n_files > 0:
                average_furrow_depth = furrow_depth_sum / n_files
                # Determine the output folder
                output_folder = os.path.join("/share/belmonte/athayam/Gastrulation_corrected/dynamic_30_9_central_basal_50_complete_artefacts_corrected/")
                print(n_files)
                # Ensure the output directory exists, if not, create it
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                # Define the output file path
                output_file = os.path.join(output_folder, "fd_lambda_cent_{}_lambda_peri_{}.txt".format(cent_list[lambda_cent],peri_list[lambda_peri]))

                # Save average furrow depth to the new file
                np.savetxt(output_file, np.column_stack((time, average_furrow_depth)))
            
# Generate and save script files
generate_script_files()


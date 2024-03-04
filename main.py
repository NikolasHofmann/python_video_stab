from vidstab import VidStab
from os import listdir
from os.path import isfile, join

# apply to all files in directory
onlyfiles = [f for f in listdir("D:/GoPro-Exports") if isfile(join("D:/GoPro-Exports", f))]
print("\n\n")
print(onlyfiles)
print("\n\n")

stabilizer = VidStab()
for file in onlyfiles:
    stabilizer.stabilize(input_path=f'D:/GoPro-Exports/{file}', output_path=f'D:/GoPro-Exports/stabilized/stabilized_{file}'
                         , show_progress=True)
    print(f'Finished stabilizing {file}')



# Using defaults
# stabilizer = VidStab()
# stabilizer.stabilize(input_path='D:/GoPro-Exports/first_file_test.mp4', output_path='D:/GoPro-Exports/test_result.mp4')

# # Using a specific keypoint detector
# stabilizer = VidStab(kp_method='ORB')
# stabilizer.stabilize(input_path='input_video.mp4', output_path='stable_video.avi')
#
# # Using a specific keypoint detector and customizing keypoint parameters
# stabilizer = VidStab(kp_method='FAST', threshold=42, nonmaxSuppression=False)
# stabilizer.stabilize(input_path='input_video.mov', output_path='stable_video.avi')
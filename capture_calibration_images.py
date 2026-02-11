import vision_cad.camera_calibration as cal
import argparse

# Script that receives the number of images to be taken for camera calibration, 
# and the resolution of the images which is optional
# and then calls the function to capture the images for camera calibration.
# Another input is the integer or url for the camera to be used for capturing the images, which is also optional and defaults to 0 (the default camera).

def main():
    parser = argparse.ArgumentParser(description="Capture calibration images for camera.")
    parser.add_argument("num_images", type=int, help="Number of images to capture for camera calibration")
    parser.add_argument("--resolution", default="2560,1440", help="Resolution of the images as width,height (default: 2560,1440)")
    parser.add_argument("--camera", default="0", help="Camera source: integer or URL (default: 0)")
    
    args = parser.parse_args()
    
    num_images = args.num_images
    width, height = map(int, args.resolution.split(','))
    resolution = (width, height)
    
    try:
        camera_source = int(args.camera)
    except ValueError:
        camera_source = args.camera
    
    cal.capture_calibration_images(num_images, resolution[0], resolution[1], camera_source)   
        

if __name__ == "__main__":
    main()
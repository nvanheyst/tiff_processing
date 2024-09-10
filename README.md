# tiff_processing

**background**

          This repo includes programs for capturing and processing 16 bit radiometric TIFF files from a USB thermal camera such as the FLIR Radiometic Boson 640.
          
          For the Boson specifically this C++ program can be used: https://github.com/FLIR/BosonUSB. Explained more here: https://flir.custhelp.com/app/answers/detail/a_id/3305/~/flir-oem---linux-and-embedded-                  support-for-boson-sdk-commands. Scale and offset should be here: https://groupgets-files.s3.amazonaws.com/boson/documents/Boson%20datasheet%2C%20102-2013-40%2C%20Rev%20340.pdf

**capture_tiff.py**
          Captures on frame from the video stream as a 16 bit TIFF file with radiometric data
          
          The linux program on this page was used as a reference to create the capture_tiff.py program: https://flir.custhelp.com/app/answers/detail/a_id/3387/~/flir-oem---boson-video-and-image-capture-using-opencv-           16-bit-y16

**temp_at_pixel.py**
          A template for determining temperature at a specific pixel

**pygame_tiff.py**
          A POC program that displays a TIFF image, a user can click on the image and the program will print the temperature at the closest pixel


